"""
Fix kompetansemaal.json with correct Udir data, then update all content pages
with correct new KM IDs based on each page's topic.
"""
import json
import re
from pathlib import Path

BASE = Path("/home/ole/workspace/vg1-im")

# ========== 1. Correct competence goals from Udir ==========

TF = {
    "tf-01": "planlegge og gjennomføre sanntidsproduksjoner.",
    "tf-02": "reflektere over og beskrive hvordan media påvirker mennesker og deres medievaner.",
    "tf-03": "kjenne til og anvende bransjefaglige metoder og relevant utstyr i produksjon.",
    "tf-04": "beskrive, utforske og konfigurere datanettverk med egne subnett.",
    "tf-05": "administrere brukerenheter og koble dem til sentrale administrasjonsplattformer.",
    "tf-06": "utforske og beskrive hvordan teknologi kan formidle nye uttrykk og gi nye opplevelser.",
    "tf-07": "gjøre rede for hvordan hensynet til bærekraft påvirker anskaffelse, drift og avhending av utstyr og materiell.",
    "tf-08": "gjennomføre og dokumentere arbeid i tråd med gjeldende bestemmelser for helse, miljø og sikkerhet.",
    "tf-09": "gjøre rede for hvordan internett fungerer, og hvordan det blir brukt til kommunikasjon og lagring.",
    "tf-10": "utforske og beskrive digitale trusler, verdier og sårbarheter i samfunnet.",
    "tf-11": "gjøre rede for hvordan man behandler informasjon og personopplysninger i tråd med gjeldende regelverk.",
    "tf-12": "vurdere, anbefale og kvalitetssikre tiltak som reduserer risiko for uønsket spredning av data.",
}

PHF = {
    "ph-01": "produsere og kommunisere innhold innenfor ulike sjangre tilpasset visuelle og auditive medier.",
    "ph-02": "utvikle og presentere budskap tilpasset ulike målgrupper og kanaler.",
    "ph-03": "utforske og bruke komposisjonsprinsipper for å sikre god lesbarhet tilpasset budskap og målgruppe.",
    "ph-04": "velge og bruke virkemidler, typografi og layout som passer til ulike budskap og reflektere over effekten.",
    "ph-05": "bruke teknikker for idéutvikling, kreativitet og historiefortelling i produksjon.",
    "ph-06": "utforske og bruke fortelleteknikk og dramaturgi i egne produksjoner.",
    "ph-07": "utøve kildekritikk og etisk refleksjon og anvende relevante regelverk i egen produksjon.",
    "ph-08": "utforske hvordan interaktivitet i historiefortelling kan brukes for å skape engasjement og nye uttrykk.",
    "ph-09": "utforske og tilegne seg kunnskap om endringer innenfor teknologi og programvare ved å bruke ulike kilder.",
    "ph-10": "gjøre rede for hvordan medier kan påvirke meningene våre, hvordan vi oppfatter andre og hvordan andre oppfatter oss.",
    "ph-11": "forstå hvordan teknologi og sikkerhet kan påvirke åpne og demokratiske prosesser og utøve etisk refleksjon.",
    "ph-12": "gjøre rede for og vurdere hvordan partene i arbeidslivet samarbeider for å utvikle et bedre arbeidsliv.",
}

KOP = {
    "kp-01": "anvende regelverk for bruk og formidling av innhold i egen produksjon og reflektere over ansvar og etikk.",
    "kp-02": "utforske og beskrive sammenhenger mellom løsninger, kundens behov og brukernes forutsetninger og erfaringer.",
    "kp-03": "bruke programmering til å løse praktiske utfordringer og til å fortelle interaktive historier.",
    "kp-04": "utforske og anvende verktøy for datamodellering i oppbygging av databaser.",
    "kp-05": "bruke oppmerkingsspråk og stilsett i ulike produksjoner.",
    "kp-06": "visualisere og utvikle konsepter og ideer tilpasset ulike plattformer.",
    "kp-07": "beskrive hvordan teknologi behandler data, algoritmer og statistikk.",
    "kp-08": "bruke prinsipper for feilsøking og retting i arbeid med programmering.",
    "kp-09": "bruke dokumentasjon og dokumentere faglige prosesser.",
}

combined = {**TF, **PHF, **KOP}

with open(BASE / "src" / "data" / "kompetansemaal.json", "w", encoding="utf-8") as f:
    json.dump(combined, f, indent=2, ensure_ascii=False)
    f.write("\n")
print(f"✅ Written {len(combined)} competence goals to kompetansemaal.json")

# ========== 2. Correct KM refs per content page ==========

# Manual mapping: file_path → [correct new IDs]
# Based on page topic and correct new KOP/PHF goals
CORRECTIONS = {
    # --- KOP pages ---
    "konseptutvikling-programmering/programmering.md": ["kp-03", "kp-08", "kp-07"],
    "konseptutvikling-programmering/webutvikling.md": ["kp-05", "kp-09", "kp-01"],
    "konseptutvikling-programmering/database.md": ["kp-04"],
    "konseptutvikling-programmering/apputvikling.md": ["kp-06", "kp-02"],
    "konseptutvikling-programmering/dokumentasjon.md": ["kp-09"],
    "konseptutvikling-programmering/regelverk-etikk.md": ["kp-01"],
    # --- PHF pages ---
    "produksjon-historiefortelling/videoproduksjon.md": ["ph-01", "ph-02", "ph-06"],
    "produksjon-historiefortelling/visuelle-medier.md": ["ph-03", "ph-04"],
    "produksjon-historiefortelling/historiefortelling.md": ["ph-06", "ph-08"],
    "produksjon-historiefortelling/idearbeid-kreativitet.md": ["ph-05"],
    "produksjon-historiefortelling/auditive-medier.md": ["ph-01"],
    "produksjon-historiefortelling/medier-makt-samfunn.md": ["ph-10", "ph-11"],
    "produksjon-historiefortelling/mediekommunikasjon.md": ["ph-02"],
    "produksjon-historiefortelling/kilder-kildekritikk.md": ["ph-07", "ph-10"],
    "produksjon-historiefortelling/interaktivitet-historiefortelling.md": ["ph-08"],
    # --- Tverrfaglig ---
    "tverrfaglig/tverrfaglig-prosjekt.md": ["tf-01", "ph-01", "kp-03"],
}

def update_frontmatter_km(content, new_km_list):
    """Replace kompetansemaal line in YAML frontmatter."""
    km_str = json.dumps(new_km_list)
    # Replace pattern like: kompetansemaal: [kp-03, kp-08, kp-07]
    # or: kompetansemaal: [ph-10]
    pattern = r'^kompetansemaal:\s*\[.*?\]'
    replacement = f'kompetansemaal: {km_str}'
    new_content = re.sub(pattern, replacement, content, count=1, flags=re.MULTILINE)
    return new_content

updated = 0
for rel_path, new_km_ids in CORRECTIONS.items():
    file_path = BASE / "src" / "content" / "emner" / rel_path
    if not file_path.exists():
        print(f"  ❌ Not found: {rel_path}")
        continue
    
    content = file_path.read_text(encoding="utf-8")
    old_km_line = re.search(r'^kompetansemaal:\s*\[.*?\]', content, re.MULTILINE)
    new_content = update_frontmatter_km(content, new_km_ids)
    
    if new_content != content:
        file_path.write_text(new_content, encoding="utf-8")
        old = old_km_line.group(0) if old_km_line else "N/A"
        print(f"  ✅ {rel_path}: {old} → kompetansemaal: {new_km_ids}")
        updated += 1
    else:
        print(f"  ⏭️  {rel_path}: no change needed")

print(f"\n✅ Updated {updated} content files")
