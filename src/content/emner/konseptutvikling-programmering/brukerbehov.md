---
title: "Brukerbehov og brukeropplevelse — UX"
emne: brukerbehov
fag: konseptutvikling-programmering
uke: [38, 39]
kompetansemaal: ["kp-02"]
kilder:
  - https://ndla.no/f/konseptutvikling-og-programmering-im-ikm-vg1/7bc23d06d79d
  - https://www.uutilsynet.no/
tags: [ux, brukerbehov, målgruppe, tilgjengelighet, designthinking]
relatert:
  - teknologiforstaelse/bransjefaglige-metoder
  - konseptutvikling-programmering/webutvikling
---

# Brukerbehov og brukeropplevelse — UX

## 🎯 Hva skal du lære?

Du skal utforske og beskrive sammenhenger mellom løsninger, kundens behov og brukernes forutsetninger. Med andre ord: hvordan lager du noe som faktisk fungerer for dem som skal bruke det? Du lærer å sette deg i brukerens sted, analysere målgrupper, og forstå hvorfor universell utforming er viktigere enn du tror.

---

## 📘 Fagstoff

### Hva er brukerbehov?

Brukerbehov handler om hva mennesker trenger — ikke hva du *tror* de trenger. Det er lett å hoppe rett på koding og lage en løsning som gir mening for deg selv, men som forvirrer alle andre.

**Eksempel:** Tenk på Vipps. Du åpner appen, skriver inn telefonnummer og beløp, trykker «Send» — ferdig. Den er enkel fordi noen har brukt masse tid på å forstå hva brukeren faktisk vil gjøre. At den er enkel for deg er et tegn på hardt arbeid bak.

#### Empati i produktutvikling

Empati betyr å forstå andres følelser og perspektiv. I produktutvikling handler det om å stille spørsmål som:

- Hvem er brukeren?
- Hva prøver de å få til?
- Hva stopper dem?
- Hvordan føles det å bruke løsningen?

> "Du er ikke brukeren" — en av de viktigste innsiktene i UX-faget.

### Målgruppeanalyse

Målgruppeanalyse handler om å bli kjent med hvem du lager noe for. To vanlige verktøy:

#### Personas

En persona er en fiktiv person som representerer en brukergruppe. Du gir dem navn, alder, mål og frustrasjoner.

**Eksempel persona:**

> **Ali, 17 år — VG1 elev**  
> Mål: Finne ut hva han må gjøre for å bestå faget  
> Frustrasjon: Det er vanskelig å finne oversikt over vurderingskriterier  
> Trenger: Tydelig struktur, mobilvennlig innhold, eksempler

#### Brukerhistorier

En brukerhistorie (user story) beskriver et behov på en enkel måte:

> "Som **elev** vil jeg **kunne se fremdriftsloggen min** slik at **jeg vet hva jeg har gjort og hva som gjenstår**."

Formelen er alltid: **Som <rolle> vil jeg <funksjon> slik at <verdi>.**

### Universell utforming (UU)

Universell utforming betyr at produkter skal fungere for alle — uansett funksjonsevne. I Norge er dette regulert av lov (diskriminerings- og tilgjengelighetsloven), og nettsider i offentlig sektor må følge WCAG-standardene.

**WCAG 2.1 — korte versjonen:**

- **Oppfattbar:** Innhold må kunne oppfattes (alt-tekst på bilder, tekster for lyd)
- **Anvendbar:** Grensesnittet må kunne brukes (tastaturnavigasjon, nok tid)
- **Forståelig:** Innhold og grensesnitt må være forutsigbart (tydelig språk, feilmeldinger)
- **Robust:** Løsningen må fungere med ulike teknologier (skjermlesere, ulike nettlesere)

**Eksempler du kjenner igjen:**

- Gul tekst på hvit bakgrunn — vanskelig å lese (dårlig kontrast)
- Autospill av video med lyd — overraskende og stressende
- Knapper som er for små å trykke på mobil — irriterende
- Alt-tekst på bilder — gjør Instagram brukbart for blinde

> Sjekk [uutilsynet.no](https://www.uutilsynet.no/) for norske krav og verktøy.

### Brukertesting og tilbakemeldinger

Brukertesting betyr å observere ekte mennesker mens de bruker produktet ditt. Du trenger ikke et laboratorium — fem testbrukere er nok til å finne de fleste problemene.

**Slik tester du:**

1. Gi brukeren en oppgave (f.eks. «finn timeplanen din»)
2. Ikke hjelp eller forklar — observer
3. Noter hvor de stopper opp eller blir forvirret
4. Forbedre og test på nytt

**Iterasjon er nøkkelen:** Lag → Test → Lær → Forbedre → Gjenta.

---

## 💡 Praktiske eksempler

**Tenk på en app du bruker hver dag — Snapchat, Instagram, TikTok, eller Skolearena.**

- Hva er det første du ser når du åpner appen? Hvorfor tror du utviklerne valgte akkurat det?
- Hvordan vet appen hva du liker? (anbefalingsalgoritmer bygger på brukerdata)
- Hva irriterer deg med appen? Det irriterende er ofte et tegn på dårlig UX.

**Case: Vipps og SMS-betaling**

Før Vipps måtte du taste inn kontonummer, beløp og signere med BankID på mobil. Vipps så at behovet var: *«Jeg vil betale en venn så enkelt som å sende en SMS.»* Resultatet ble en app med tre trykk.

**Case: NAV.no**

NAV sine nettsider må fungere for alle — ungdom som søker sommerjobb, pensjonister, mennesker med lese- og skrivevansker, blinde. Derfor har de strenge krav til UU og brukertesting. Når det ikke fungerer, får NAV masse klager — fordi brukerne *er avhengige* av løsningen.

---

## 🔗 Tverrfaglige koblinger

- **Teknologiforståelse:** Bransjefaglige metoder som design thinking og smidig utvikling
- **Webutvikling:** Universell utforming og tilgjengelighet i HTML/CSS
- **Produksjon og historiefortelling:** Målgruppetenkning, visuell kommunikasjon

---

## 📚 Kilder

- NDLA — Konseptutvikling og programmering: [Brukerbehov og brukeropplevelse](https://ndla.no/f/konseptutvikling-og-programmering-im-ikm-vg1/7bc23d06d79d)
- [Uutilsynet.no](https://www.uutilsynet.no/) — Norsk tilsyn for universell utforming (WCAG-krav, verktøy, veiledning)
- [Design Thinking (IDEO)](https://www.ideo.com/) — Human-centered design-metodikk
- [WCAG 2.1 på norsk (uu-tilsynet)](https://www.uutilsynet.no/wcag-standarden/wcag-21-standarden/149)

---

## 🛠️ Prøv selv!

1. **Lag en persona.** Velg en medelev og lag en persona for en skole-app. Hva trenger de? Hva irriterer dem med dagens løsninger? Presenter personaen for en annen i klassen.

2. **Sjekk UU på en nettside du bruker.** Gå inn på en nettside og test: Kan du navigere kun med tastaturet (Tab-tasten)? Har bilder alt-tekst? Er kontrasten god nok? Bruk [WAVE-verktøyet](https://wave.webaim.org/) for å sjekke.

3. **Gjør en mini-brukertest.** Be en venn om å utføre en oppgave i en app (f.eks. «finn ut når bussen går»). Ikke hjelp dem — bare observer og notér. Hva ble de forvirret av? Hvordan kunne appen vært bedre?

---

## 📋 Nøkkelbegreper

| Begrep | Betydning |
|--------|-----------|
| **Brukerbehov** | Hva brukeren faktisk trenger, ikke hva du tror de trenger |
| **Persona** | Fiktiv person som representerer en målgruppe |
| **Brukerhistorie** | Kort beskrivelse av en funksjon sett fra brukerens ståsted |
| **Universell utforming (UU)** | Produkter som fungerer for alle, uansett funksjonsevne |
| **WCAG** | Web Content Accessibility Guidelines — standard for tilgjengelighet |
| **Brukertesting** | Observer ekte brukere for å finne problemer |
| **Iterasjon** | Gjenta prosessen: test, lær, forbedre |
| **Empati** | Evnen til å sette seg inn i brukerens situasjon |
