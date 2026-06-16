---
title: "Praktisk IT — Brukerenheter og administrasjon"
emne: praktisk-it
fag: teknologiforstaelse
uke: [8, 9]
kompetansemaal: [tf-04, tf-05]
kilder:
  - https://ndla.no/f/teknologiforstaelse-im-ikm-vg1/087c23101fc5
tags: [it-drift, administrasjon, brukerenheter, konfigurasjon]
relatert:
  - teknologiforstaelse/lokale-nettverk
---
# Praktisk IT — Brukerenheter og administrasjon

## 🎯 Hva skal du lære?

Du skal administrere brukerenheter og koble dem til sentrale administrasjonsplattformer. Du skal også kunne konfigurere datanettverk med egne subnett.

---

## 📘 Fagstoff

### Brukerenheter

En brukerenhet er en hvilken som helst enhet en person bruker for å få tilgang til IT-tjenester:

- **Stasjonære PC-er:** Windows, macOS
- **Bærbare PC-er:** Jobb-PC-er, skole-PC-er
- **Mobiler og nettbrett:** iOS, Android
- **Skrivere, projektorer, smart-TVer**

### Administrasjon av enheter

For å holde kontroll på mange enheter bruker man sentrale administrasjonsplattformer:

#### MDM (Mobile Device Management)
- Styrer innstillinger på mobiler og nettbrett
- Eksempler: Intune, Jamf, VMware Workspace ONE
- Kan: installere apper, slette data, låse enheter, policy-styring

#### Windows Domain / Active Directory
- Sentral brukeradministrasjon i Windows-nettverk
- Brukere logger inn med én bruker på alle PC-er
- Administratorer styrer rettigheter fra én server

#### Skybasert administrasjon
- **Microsoft Entra ID:** Skytjeneste for bruker- og enhetsadministrasjon
- **Google Admin Console:** Administrer Chromebooks og Google-kontoer
- **Apple Business Manager:** Administrer Apple-enheter

### Nettverkskonfigurasjon med subnett

Når du setter opp et nettverk for en virksomhet, deler du ofte nettverket i subnett:

**Eksempel — Skolenettverk:**
- Subnett A (192.168.10.0/24): Administrasjon — 20 enheter
- Subnett B (192.168.20.0/24): Lærere — 80 enheter
- Subnett C (192.168.30.0/24): Elever — 300 enheter
- Subnett D (192.168.40.0/24): Gjest/WiFi — 100 enheter

**Fordeler med subnett:**
- Bedre sikkerhet (trafikk isoleres)
- Mindre nettverkstrafikk (broadcast-domenet reduseres)
- Enklere å feilsøke
- Bedre kontroll med ressursbruk

---

## 💡 Praktiske eksempler

**Koble en PC til et domene:**
1. Åpne Innstillinger → Kontoer → Få tilgang til jobb eller skole
2. Velg "Koble til"
3. Skriv inn domenenavnet (f.eks. `skole.no`)
4. Skriv inn administratorbruker og passord
5. Start PC-en på nytt — nå kan elevene logge inn med skolebrukeren

---

## 🔗 Tverrfaglige koblinger

- **Programmering:** Scripting for automatisering av enhetsadministrasjon
- **Naturfag:** Forståelse av elektronikk i enheter

---

## 📚 Kilder

- NDLA — Praktisk IT
- [Microsoft Learn — Enhetsadministrasjon](https://learn.microsoft.com/nb-no/training/)
