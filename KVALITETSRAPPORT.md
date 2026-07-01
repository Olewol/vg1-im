# VG1 IM Fagside — Kvalitetsgjennomgang og Forbedringsplan

Generert: 2026-07-01 · Basert på komplett gjennomgang av alle 43 sider

## Status (hva er bra)

- ✅ Alle 33 kompetansemål dekket (12 TF + 12 PHF + 9 KOP)
- ✅ 43 sider bygget, 0 feil, 0 type-warnings
- ✅ Moderne stack (Astro 5, Tailwind, TypeScript, Mermaid)
- ✅ Lys/mørkt tema, skip-link, sitemap
- ✅ WCAG-kontrast fikset: text2 (4.5:1 ✓), text3 (4.5:1 ✓)
- ✅ `aria-current="page"` på navigasjon, `target="_blank"`-varsel
- ✅ 7 Mermaid-diagrammer lagt til
- ✅ 3 nye KOP-emner (kp-01 utvidet, kp-02 ny, kp-06 ny)
- ✅ Utvidet: auditive-medier (54→283), idearbeid (62→135), interaktivitet (65→full), datasikkerhet (90→full), personvern (84→full), medier-makt-samfunn (73→full)

## Hva ble gjort i denne økten

### WCAG og a11y
- Fikset fargekontrast: `--text2` #6e6e73→#5c5c5f (4.2→6.7:1), `--text3` #aeaeb2→#6e6e72 (1.9→5.1:1)
- Fikset dark mode text3: #636366→#98989d (2.7→5.9:1)
- `aria-current="page"` på desktop- og mobilnavigasjon
- `target="_blank"`-varsel: "(åpnes i ny fane)"
- Mobilmeny: `aria-expanded`, `role="navigation"`

### Nye emner (KOP-hull)
| Emne | Fil | KM | Linjer |
|------|-----|-----|--------|
| Brukerbehov og UX | brukerbehov.md | kp-02 | 157 |
| Konseptutvikling og visualisering | konseptutvikling.md | kp-06, kp-02 | 180 |
| Regelverk og etikk (utvidet) | regelverk-etikk.md | kp-01 | 57→full |

### Utvidede emner
| Emne | Før | Etter | Forbedring |
|------|-----|-------|------------|
| Auditive medier | 54 | 283 | Lydformater, opptaksutstyr, podkast-planlegging, intervjuteknikk, redigering, lyddesign |
| Idéarbeid og kreativitet | 62 | 135 | Kreative teknikker (SCAMPER, mindmap, brainstorming), idéprosess |
| Interaktiv historiefortelling | 65 | Full | Forgreiningstyper, Twine-guide, dramaturgi, eksempler (Bandersnatch ++) |
| Datasikkerhet | 90 | Full | 2 Mermaid-diagram, phishingkjenning, 2FA-praksis, risikovurdering |
| Personvern | 84 | Full | GDPR-rettigheter, datakategorier, CC-lisenser |
| Medier, makt og samfunn | 73 | Full | Teknologiendringer-tabell, desinformasjon, deepfakes |
| Regelverk og etikk | 57 | Full | CC-lisenser, GDPR, etiske dilemmaer |

### Visuelle elementer
| Side | Type diagram |
|------|-------------|
| Programmering | Kodeflyt (Mermaid LR) |
| Webutvikling | HTML+CSS+JS samspill (Mermaid LR) |
| Datasikkerhet | Verdier→trusler + sårbarheter→angriper |
| Personvern | Datatyper (Mermaid TD) |
| Medier, makt og samfunn | Medieeierskap (Mermaid TD) |
| Interaktiv historiefortelling | Forgrening (Mermaid TD) |
| Regelverk | Etisk beslutningstre (Mermaid TD) |

### Kilder
- Lagt til: Datatilsynet, NSM, NorSIS, IM Fagboka (docs.iktim.no), Creative Commons, BBC Sound Effects, Pixabay, Audacity, Figma, Twine, Ink, Have I Been Pwned, Uutilsynet, WCAG, Faktisk.no, SSB Medier, Teknologirådet

### Test-rammeverk
- `npm test` → kjører `scripts/validate-content.py`
- Validerer: KM-referanser, relatert-lenker, linjetelling, duplikater
- Status: 38 emner, 0 feil, full KM-dekning

## Gjenstående (lavere prioritet)

### Tynne emner (<80 linjer) som bør utvides
- tverrfaglig-prosjekt (45) — prosjektbeskrivelse, OK som kort
- historiefortelling (72) — bør utvides
- apputvikling (73) — bør utvides
- digital-teknologi (74), digital-kommunikasjon (75)
- sanntidsproduksjon (76), praktisk-it (78)
- videoproduksjon (76), dokumentasjon (76)
- nye-opplevelser-teknologi (64), media-medievaner (67)
- Under arbeid: kilder-kildekritikk, visuelle-medier, mediekommunikasjon (delegert til subagent)

### Teknisk (ikke startet)
- Søkefunksjon (Pagefind/Stork)
- Print-vennlig CSS
- PWA / manifest.json
- "Sist oppdatert"-dato på sider
- RSS-feed

### Innhold (fremtidig)
- Årsplaner for PHF og KOP
- Flere embeddede videoer (astro-embed-youtube installert)
- Interaktive kodeeksempler
