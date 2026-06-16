---
title: "Dokumentasjon — Hvorfor og hvordan dokumentere"
emne: dokumentasjon
fag: konseptutvikling-programmering
uke: [8]
kompetansemaal: ["kp-09"]
kilder:
  - https://ndla.no/f/konseptutvikling-og-programmering-im-ikm-vg1/7bc23d06d79d
tags: [dokumentasjon, feilsøking, prosesser]
relatert:
  - konseptutvikling-programmering/programmering
---
# Dokumentasjon — Hvorfor og hvordan dokumentere

## 🎯 Hva skal du lære?

Du skal bruke dokumentasjon og dokumentere faglige prosesser, samt bruke prinsipper for feilsøking og retting i arbeid med programmering.

---

## 📘 Fagstoff

### Hvorfor dokumentere?

Dokumentasjon hjelper deg og andre:
- **Husk:** Hva gjorde du og hvorfor?
- **Dele:** Kollegaer kan forstå arbeidet ditt
- **Gjenbruke:** Bruk samme løsning senere
- **Kvalitetssikre:** Andre kan sjekke arbeidet ditt

### Hva bør dokumenteres?

- **Krav:** Hva skal løsningen gjøre?
- **Arkitektur:** Hvordan er systemet bygget?
- **Installasjon:** Hvordan sette opp og kjøre?
- **Endringslogg:** Hva er endret når og av hvem?
- **Bruksanvisning:** Hvordan bruker man løsningen?

### Verktøy for dokumentasjon

- **README:** Prosjektets forsidedokument
- **Wiki:** Delt kunnskapsbase (Notion, Confluence)
- **Kodekommentarer:** Forklar koden i koden
- **Versjonskontroll (Git):** Hold oversikt over endringer

### Feilsøking (Debugging)

Systematisk tilnærming til feilsøking:

1. **Reproduser feilen:** Kan du få den til å skje igjen?
2. **Les feilmeldingen:** Hva sier den? Hvor peker den?
3. **Isoler problemet:** Hvilken del av koden feiler?
4. **Sjekk antagelser:** Stemmer det du tror om koden?
5. **Test én ting om gangen:** Endre én ting, test, gjenta
6. **Søk hjelp:** Google, forum, kollegaer

---

## 💡 Praktiske eksempler

**README-struktur:**
```markdown
# Prosjektnavn
En kort beskrivelse av prosjektet

## Installasjon
1. Klon repoet: `git clone ...`
2. Installer avhengigheter: `npm install`
3. Kjør: `npm start`

## Bruk
Beskriv hvordan prosjektet brukes

## Lisens
MIT
```

---

## 🔗 Tverrfaglige koblinger

- **Teknologiforståelse:** Bransjefaglige metoder, dokumentasjonskrav

---

## 📚 Kilder

- NDLA — Dokumentasjon
