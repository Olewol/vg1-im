#!/usr/bin/env python3
"""Validering av VG1 IM fagside-innhold.

Sjekker:
1. Alle KM-IDer i emner finnes i kompetansemaal.json
2. Alle 'relatert'-referanser peker til eksisterende emner
3. Ingen emner har dupliserte slugs
4. Alle emner har minimum 80 linjer innhold
5. Dekning per fag
"""
import os, sys, re, json

BASE = '/home/ole/workspace/vg1-im'
EMNER_DIR = os.path.join(BASE, 'src/content/emner')
KM_FILE = os.path.join(BASE, 'src/data/kompetansemaal.json')

errors = 0

# 1. Load KM data
with open(KM_FILE) as f:
    km_data = json.load(f)

# 2. Scan all emner
all_slugs = {}
emne_data = []
for root, dirs, files in os.walk(EMNER_DIR):
    for file in files:
        if not file.endswith('.md'):
            continue
        path = os.path.join(root, file)
        with open(path) as f:
            content = f.read()
        
        # Extract frontmatter
        fm_match = re.search(r'^---\n(.*?)\n---', content, re.DOTALL)
        if not fm_match:
            print(f'⚠️  Mangler frontmatter: {path}')
            errors += 1
            continue
        
        fm = fm_match.group(1)
        
        def get_fm(key):
            m = re.search(rf'^{key}:\s*(.+)$', fm, re.MULTILINE)
            return m.group(1).strip() if m else ''
        
        # Extract fields
        title = get_fm('title')
        emne = get_fm('emne')
        fag = get_fm('fag')
        
        # Parse kompetansemaal
        km_raw = get_fm('kompetansemaal')
        km_list = re.findall(r"['\"]?([a-z]{2}-\d+)[\"']?", km_raw)
        
        # Parse relatert
        rel_raw = get_fm('relatert')
        rel_list = re.findall(r"['\"]?([a-z-]+/[a-z-]+)[\"']?", rel_raw)
        
        # Parse kilder
        kilder_raw = get_fm('kilder')
        kilder_list = re.findall(r'https?://[^\s,\]]+', kilder_raw)
        
        # Count lines (excluding frontmatter)
        body = content[fm_match.end():].strip()
        line_count = len(body.split('\n'))
        
        slug = file.replace('.md', '')
        rel_path = os.path.relpath(path, EMNER_DIR)
        
        emne_data.append({
            'path': path,
            'slug': slug,
            'rel_path': rel_path,
            'title': title,
            'emne': emne,
            'fag': fag,
            'km_list': km_list,
            'rel_list': rel_list,
            'kilder_count': len(kilder_list),
            'line_count': line_count,
        })
        
        # Check for duplicate slugs
        if slug in all_slugs:
            print(f'❌ Duplikat slug: {slug} ({path} og {all_slugs[slug]})')
            errors += 1
        all_slugs[slug] = path

print(f'✓ Skanne {len(emne_data)} emnefiler\n')

# 3. Validate KM references
all_km_ids = set(km_data.keys())
for ed in emne_data:
    for km in ed['km_list']:
        if km not in all_km_ids:
            print(f'❌ {ed["rel_path"]}: ukjent KM-ID "{km}"')
            errors += 1

# 4. Validate relatert-referanser
for ed in emne_data:
    for rel in ed['rel_list']:
        # rel is like "teknologiforstaelse/personvern"
        parts = rel.split('/')
        if len(parts) >= 2:
            ref_fag = parts[0]
            ref_slug = parts[1]
            # Check if target file exists
            found = False
            for ed2 in emne_data:
                if ref_slug == ed2['slug']:
                    found = True
                    break
            if not found:
                print(f'⚠️  {ed["rel_path"]}: relatert "{rel}" -> ingen match')
                # This is a warning, not error — could point to fag page

# 5. Check line counts
thin = [ed for ed in emne_data if ed['line_count'] < 80]
if thin:
    print(f'\n📏 Tynne emner (<80 linjer):')
    for ed in sorted(thin, key=lambda x: x['line_count']):
        km_str = ', '.join(ed['km_list'])
        print(f'   {ed["rel_path"]}: {ed["line_count"]} linjer (KM: {km_str})')

# 6. KM dekning per fag
print(f'\n📊 KM-dekning per fag:')
km_per_fag = {}
for km_id in all_km_ids:
    prefix = km_id.split('-')[0]
    km_per_fag.setdefault(prefix, set()).add(km_id)

for prefix, kms in sorted(km_per_fag.items()):
    covered = set()
    for ed in emne_data:
        for km in ed['km_list']:
            if km.startswith(prefix):
                covered.add(km)
    missing = kms - covered
    if missing:
        print(f'   {prefix}: {len(covered)}/{len(kms)} dekket. MANGLER: {", ".join(sorted(missing))}')
    else:
        print(f'   {prefix}: {len(covered)}/{len(kms)} dekket ✅')

# 7. Kilder per emne
print(f'\n📚 Kilder per emne:')
no_kilde = [ed for ed in emne_data if ed['kilder_count'] == 0]
if no_kilde:
    for ed in no_kilde:
        print(f'   ⚠️  {ed["rel_path"]}: 0 kilder')
few_kilde = [ed for ed in emne_data if 0 < ed['kilder_count'] < 3]
if few_kilde:
    for ed in few_kilde:
        print(f'   📎 {ed["rel_path"]}: {ed["kilder_count"]} kilder')
many_kilde = [ed for ed in emne_data if ed['kilder_count'] >= 3]
if many_kilde:
    for ed in many_kilde:
        print(f'   ✅ {ed["rel_path"]}: {ed["kilder_count"]} kilder')

print(f'\n=== OPPPSUMMERING ===')
print(f'Emner totalt: {len(emne_data)}')
print(f'Feil: {errors}')
if errors == 0:
    print('🎉 Alt ser bra ut!')
else:
    print(f'⚠️  {errors} feil må fikses.')
