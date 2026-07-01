---
title: "Konseptutvikling og visualisering"
emne: konseptutvikling
fag: konseptutvikling-programmering
uke: [40, 41]
kompetansemaal: ["kp-06", "kp-02"]
kilder:
  - https://ndla.no/f/konseptutvikling-og-programmering-im-ikm-vg1/7bc23d06d79d
tags: [konseptutvikling, visualisering, prototyping, wireframe, designprosess]
relatert:
  - produksjon-historiefortelling/idearbeid-kreativitet
  - produksjon-historiefortelling/visuelle-medier
  - konseptutvikling-programmering/webutvikling
---

# Konseptutvikling og visualisering

## 🎯 Hva skal du lære?

Du skal lære å ta en idé fra hodet ditt og helt fram til et ferdig konsept. Du får verktøy for å visualisere tanker, skissere løsninger og tilpasse ideer til ulike plattformer — enten det er en mobilapp, en nettside eller sosiale medier.

---

## 📘 Fagstoff

### Hva er konseptutvikling?

Konseptutvikling handler om å gjøre om en løs idé til et konkret produkt eller en løsning. Tenk på det som en trapp med fire trinn:

```
Idé → Skisse → Prototype → Ferdig produkt
```

**Trinn for trinn:**
1. **Idé:** Hva vil du lage? Hvem er det for? Hva er målet?
2. **Skisse:** Tegn ideen — det trenger ikke være pent, bare forståelig
3. **Prototype:** Lag en tidlig versjon som kan testes
4. **Ferdig produkt:** Bygg den ekte løsningen basert på det du har lært

> Hopp over skisse- og prototypefasen, og du risikerer å kode i flere uker før du innser at ingen trenger det du lager. Test tidlig, test ofte!

### Skisseteknikker

Det finnes flere måter å visualisere ideer på, alt fra papir til avanserte verktøy:

**Wireframe — «Skjelettet»**
En wireframe er en enkel, sort/hvitt-tegning som viser layout og struktur. Ingen farger, ingen bilder — bare bokser og tekst som viser hvor ting skal være.

```
+--------------------------------------------------+
|  LOGO                    Søk        Innlogg    |
+--------------------------------------------------+
|  Hjem | Om oss | Tjenester | Kontakt oss        |
+--------------------------------------------------+
|                                                    |
|  +------------------+  +------------------+       |
|  |                  |  |                  |       |
|  |  Bilde/grafikk   |  |  Bilde/grafikk   |       |
|  |                  |  |                  |       |
|  +------------------+  +------------------+       |
|                                                    |
+--------------------------------------------------+
```

**Mockup — «Sminken»**
En mockup er en mer detaljert versjon med farger, bilder, fonter og merkek. Det ser ut som det ferdige produktet, men er fortsatt bare en bildeserie — du kan ikke klikke på noe.

**Prototype — «Prøvekjøringen»**
En prototype er klikkbar. Du kan trykke på knapper, fylle ut skjemaer og navigere som om det var den ekte tingen. Perfekt for brukertesting!

| Metode | Grad av detalj | Tid å lage | Formål |
|--------|----------------|------------|--------|
| **Wireframe** | Lav → Sort/hvitt | Minutter/timer | Struktur og plassering |
| **Mockup** | Høy → Farger og bilder | Timer/dager | Design og utseende |
| **Prototype** | Høy → Klikkbar interaksjon | Dager/uker | Brukertesting |

### Verktøy

**Papir og penn (alltid tilgjengelig):**
- Best for tidlig idemyldring og raske skisser
- Null teknisk stress — bare tegn!

**Figma (gratis, nettbasert):**
- Lag wireframes, mockups og klikkbare prototyper
- Samarbeid i sanntid med teamet (som Google Docs, men for design)
- Inneholder ferdige komponenter du kan dra og slippe
- Eksporter kode (CSS, React) rett fra designet

**Andre verktøy:** Adobe XD (Figma-lignende), Balsamiq (håndtegnet stil), Sketch (Mac)

### Plattformtilpasning

En idé må tilpasses plattformen den skal leve på. En nettside er ikke det samme som en mobilapp, som ikke er det samme som en Instagram-story:

| Plattform | Format | Gode vaner |
|-----------|--------|------------|
| **Mobil** | Vertikalt, smal skjerm, trykk med fingeren | Store knapper, én kolonne, tommelvennlig |
| **Web** | Horisontalt, bred skjerm, mus/tastatur | Navigasjonsmeny, flere kolonner, hover-effekter |
| **Skjerm/TV** | Stor skjerm, fjernkontroll | Stor tekst, få klikk, kontrast |
| **Sosiale medier** | Korte videoer/bilder, scrollebasert | Fang oppmerksomhet på 3 sekunder, tekster |

**Huskeregel:** Design alltid for den plattformen brukeren faktisk sitter med. «Mobil først» er en god tommelfingerregel — hvis det fungerer på en liten skjerm, er det lett å skalere opp.

### Brukerhistorier og brukertester

**Brukerhistorier** er korte beskrivelser sett fra brukerens ståsted:

> *«Som elev vil jeg kunne sjekke timeplanen min på mobil, slik at jeg raskt ser hvor jeg skal være»*

Formatet er alltid: **Som [rolle] vil jeg [kunne gjøre] slik at [verdi].**

**Brukertester** handler om å se hvordan ekte mennesker bruker produktet ditt:
1. Gi brukeren en oppgave («Finn ut når du skal ha mattetime i morgen»)
2. Ikke hjelp dem — se hva de gjør naturlig
3. Noter hvor de stopper opp, blir forvirret eller trykker feil
4. Fiks problemene, test på nytt

---

## 💡 Praktiske eksempler

**Eksempel 1: Fra idé til prototype på én dag**
Mari vil lage en app som hjelper medelever å holde styr på lekser. Hun starter med å tegne wireframes på papir i friminuttet. Etter skolen lager hun en mockup i Figma med farger og knapper. Innen kvelden har hun en klikkbar prototype som hun lar venninna test — og oppdager at navigasjonen var altfor komplisert. Hun fikser det før hun skriver én linje kode.

**Eksempel 2: Plattformtilpasning — samme idé, ulike plattformer**
En skole skal lage en interaktiv guide for nye elever. På **web** får de en stor meny og mye informasjon på én side. På **mobil** brytes innholdet ned i korte steg med «sveip for neste». På **Instagram** blir det en karusell med 10 slides og en link i bio.

---

## 🔗 Tverrfaglige koblinger

- **Produksjon og historiefortelling:** Idéarbeid, kreative teknikker og visuell kommunikasjon er felles for begge fagene. SCAMPER og brainstorming fra ph-05 fungerer direkte i konseptutvikling (ph-05)
- **Teknologiforståelse:** Plattformkunnskap (operativsystemer, skjermstørrelser, nettverk) påvirker hvilke designvalg du tar (tf-02)

---

## 🛠️ Prøv selv!

**Oppgave 1: Papir-wireframe**
Velg en nettside eller app du bruker ofte (f.eks. Snapchat, Skolemelding, Spotify). Tegn en wireframe av startskjermen på papir — bare bokser og streker. Hvor er logoen? Hvor er navigasjonen? Hvor trykker du først?

**Oppgave 2: Lag en klikkbar prototype**
Bruk Figma (gratis) og lag en prototype med minst tre skjermer. Velg én av disse:
- En mobilapp for å bestille skolemat
- En nettside for en klubb eller forening du er med i
- En «sveip for å matche»-app for gruppeprosjekter på skolen

La en medelev teste prototypen og gi tilbakemelding.

**Oppgave 3: Plattformkrig**
Ta én og samme idé (f.eks. en skoleavis) og skisser hvordan den vil se ut på:
1. En PC-nettside (bred skjerm)
2. En mobiltelefon (smal skjerm)
3. En Instagram-story (vertikal video/bilde)

Hva må du endre? Hva kan du beholde? Skriv ned tre forskjeller for hver plattform.

---

## 📋 Nøkkelbegreper

| Begrep | Betydning |
|--------|-----------|
| **Konseptutvikling** | Prosessen fra idé til ferdig produkt |
| **Wireframe** | Enkel skisse som viser struktur og layout |
| **Mockup** | Detaljert design med farger, bilder og fonter |
| **Prototype** | Klikkbar testversjon av produktet |
| **Brukerhistorie** | Kort beskrivelse av hva en bruker trenger |
| **Brukertest** | Teste produktet på ekte brukere |
| **Plattformtilpasning** | Tilpasse design til mobil, web, skjerm eller sosiale medier |
| **Figma** | Verktøy for wireframing, mockup og prototyping |

---

## 📚 Kilder

- NDLA — [Konseptutvikling og programmering (IM-IKM VG1)](https://ndla.no/f/konseptutvikling-og-programmering-im-ikm-vg1/7bc23d06d79d)
- Figma — [Figma for begynnere (gratis)](https://www.figma.com/)
- NDLA — [Hva er en prototype? (video)](https://ndla.no/f/konseptutvikling-og-programmering-im-ikm-vg1/7bc23d06d79d)
- NMI — [Brukerhistorier og smidig utvikling](https://ndla.no/f/konseptutvikling-og-programmering-im-ikm-vg1/7bc23d06d79d)
