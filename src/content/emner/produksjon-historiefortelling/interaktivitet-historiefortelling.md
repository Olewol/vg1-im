---
title: "Interaktivitet og historiefortelling"
emne: interaktivitet-historiefortelling
fag: produksjon-historiefortelling
uke: [50]
kompetansemaal: ["ph-06", "ph-08"]
kilder:
  - https://ndla.no/f/produksjon-og-historiefortelling-im-ikm-vg1/6b4ff88031e7
  - https://docs.iktim.no/1IM/
tags: [interaktivitet, twine, historiefortelling, spill, branching, transmedia]
relatert:
  - produksjon-historiefortelling/historiefortelling
  - konseptutvikling-programmering/programmering
---

# Interaktivitet og historiefortelling

## 🎯 Hva skal du lære?

Du skal utforske hvordan interaktivitet i historiefortelling kan brukes for å
skape engasjement og nye uttrykk, og bruke dette i egen produksjon. Du skal
også kunne bruke dramaturgi og fortelleteknikker tilpasset interaktive medier.

---

## 📘 Fagstoff

### Hva er interaktiv historiefortelling?

I tradisjonell historiefortelling — en bok, en film, en podkast — er du en
**passiv mottaker**. Du sitter i sofaen og lar historien skylle over deg.
I interaktiv historiefortelling er du **aktiv deltaker**. Du tar valg som
påvirker hva som skjer videre. Historien blir *din* unike opplevelse.

**Forskjellen i ett bilde:**

| Tradisjonell historie | Interaktiv historie |
|----------------------|-------------------|
| Én lineær vei fra A til B | Flere mulige veier |
| Samme opplevelse hver gang | Unik opplevelse per spiller |
| Publikum er passive | Publikum er aktive |
| Forfatteren bestemmer alt | Spilleren er medforfatter |
| Ett sluttpunkt | Flere mulige slutter |

Interaktiv historiefortelling finnes i mange former:
- **Spill** (The Walking Dead, Life is Strange, Detroit: Become Human)
- **Strømme-opplevelser** (Black Mirror: Bandersnatch)
- **Escape rooms** (fysiske og digitale)
- **Dine-egne-eventyr-bøker** (Choose Your Own Adventure)
- **Larps** (Live Action Role Playing)

---

### Branching narratives — forgreninger i historien

Branching narratives (forgrenede fortellinger) er ryggraden i interaktiv
historiefortelling. Historien deler seg i flere grener basert på spillerens valg.

#### Tre typer forgrening

##### 1. Enkel forgrening (A → B eller C)
Spilleren tar ett valg, og historien går i én av to retninger. De to grenene
møtes igjen senere.

```
        ┌── B ──┐
Start ──┤       ├── Samlet slutt
        └── C ──┘
```

**Eksempel:** Skal du åpne døren til venstre (B) eller høyre (C)?
Uansett hva du velger, kommer du til neste rom til slutt.

##### 2. Kompleks forgrening (flere valg som bygger på hverandre)
Hvert valg åpner nye muligheter og stenger andre. Historien blir som et tre
med mange grener.

```
        ┌── B1 ── D1
        │        └── D2
Start ──┤
        │        ┌── E1
        └── C1 ──┤
                 └── E2
```

**Eksempel:** I *The Walking Dead*-spillet avgjør du hvem du redder,
og det påvirker hvem som er med deg senere. En karakter du reddet i episode 1,
dukker opp igjen i episode 4 og hjelper deg.

##### 3. Sirkulær forgrening (loop)
Spilleren må gjenta en del av historien inntil et bestemt mål er nådd.

**Eksempel:** I *Majora's Mask* har du tre dager på å redde verden.
Hvis du ikke rekker det, starter dagen på nytt — men du beholder utstyret
og kunnskapen din.

#### Utfordringer med forgrening

Å lage en forgrenet fortelling er mye mer arbeid enn en lineær. Hvis du har
3 valg per kapittel og 5 kapitler, må du skrive 3⁵ = 243 forskjellige
historiegrener! Derfor bruker de fleste en **blandingsmodell**:

- **Kritiske valg:** Få, men viktige valg som faktisk endrer historien
- **Tilsynelatende valg:** Valg som føles viktige, men som fører til samme
  punkt (illusjon av frihet)
- **Samlingspunkter:** Flere grener samles i samme scene (sparer arbeid)

---

### Verktøy for interaktiv historiefortelling

#### Twine — best for nybegynnere

[Twine](https://twinery.org/) er et gratis, nettbasert verktøy for å lage
interaktive fortellinger. Du trenger ikke å kunne kode for å komme i gang.

**Slik fungerer Twine:**
1. Opprett **passuser** (kort) — hver pasuse er én del av historien
2. Skriv innhold i hver pasuse
3. Koble passuser med **linker** ved å skrive `[[tekst→pasusenavn]]`
4. Spilleren klikker på linker for å ta valg
5. Historien forgrener seg basert på valgene

**Eksempel i Twine:**

```
Du står foran en mørk skog. Hva gjør du?
[[Gå inn i skogen→skogen]]
[[Snu og gå hjem→hjem]]
```

Twine støtter også **variabler** (Harlowe, SugarCube) for å holde styr på
spillerens valg:

```
Du har {$nøkkel} nøkler.
[[Bruk nøkkelen→dør]] (setter: $åpen = true)
```


#### Ink — for avanserte Twine-brukere og spillutvikling

[Ink](https://www.inklestudios.com/ink/) er et scriptspråk for interaktiv
fiksjon, utviklet av Inkle Studios (skaperne av *80 Days* og *Heaven's Vault*).
Det brukes ofte sammen med Unity for å lage interaktive dialoger i større spill.

**Slik ser Ink ut:**

```
VAR helse = 100

Du våkner i et mørkt rom.
+ [Rop på hjelp] -> rop
+ [Let etter lysbryter] -> lys

=== rop ===
Du roper, men ingen svarer. -> redusert_helse

=== redusert_helse ===
~ helse = helse - 10
Du mister pusten. -> fortsett

=== lys ===
Du finner bryteren og skrur på lyset. -> fortsett
```

Fordelene med Ink er at du har mer kontroll over logikken, og at du enkelt
kan integrere fortellingen i et Unity-spill.

#### ChoiceScript — dine-egne-eventyr

ChoiceScript er et enkelt scriptspråk for å lage interaktive romaner.
Det brukes av Choice of Games til å lage kommersielle interaktive bøker.

#### Ren'Py — visuelle romaner

Ren'Py er et gratis rammeverk for å lage visuelle romaner — interaktive
fortellinger med bilder, lyd og valg. Spill som *Doki Doki Literature Club*
er laget i Ren'Py.

---

### Brukervalg og konsekvenser — hva gjør et valg meningsfullt?

Det er lett å lage valg i en interaktiv fortelling. Det vanskelige er å gjøre
dem **meningsfulle**. Et valg som ikke har noen reell effekt, føles som juks.

#### Fire typer valg

| Valgtype | Forklaring | Eksempel |
|----------|------------|----------|
| **Moralvalg** | Velg mellom rett og galt | Redde en venn eller redde deg selv |
| **Strategivalg** | Velg den beste taktikken | Gå forsiktig eller løpe fort |
| **Personlighetsvalg** | Velg hvordan karakteren din er | Være snill eller sarkastisk |
| **Tidsvalg** | Velg hva du prioriterer | Hjelpe en venn eller gjøre lekser |

#### Hvordan skape meningsfulle valg?

1. **Valget må ha konsekvenser** — spilleren må merke forskjellen
2. **Konsekvensen må komme senere** — ikke alltid med en gang
3. **Valget må være uoversiktlig** — ikke åpenbart hva som er «rett» svar
4. **Begge valgene må være fristende** — hvis det ene er åpenbart bedre,
   er det ikke et reelt valg
5. **Valget må påvirke historien, ikke bare føles som den gjør det**

**Eksempel på et godt valg (The Walking Dead):**
Tidlig i spillet må du velge hvem av to overlevende du redder. Den du
ikke redder, dør. Men senere i spillet møter du en karakter som var i
familie med den du lot dø — og de husker det.

**Eksempel på et dårlig valg:**
«Vil du ha en kopp kaffe eller te?» — og så skjer nøyaktig det samme
uansett hva du svarer.

### Eksempler på interaktiv historiefortelling

#### Black Mirror: Bandersnatch (Netflix, 2018)

Bandersnatch var en av de første store interaktive filmene på Netflix.
Seeren tar valg for hovedpersonen Stefan, en ung programmerer som lager
et spill basert på en interaktiv bok.

**Hvorfor den fungerte:**
- Valgene føltes naturlige (skal du spise frokost eller ta medisiner?)
- Flere mulige slutter (5 hovedslutter)
- Meta-nivå: historien handler om interaktive valg
- «Skjulte» valg som bare noen oppdaget

**Hvorfor den var kontroversiell:**
- Ikke alle valg hadde like stor effekt
- Noen følte at historien «jukset» hvis du fikk samme scene uansett
- Netflix måtte bygge helt ny teknologi for å støtte branching

#### The Walking Dead-spillet (Telltale Games, 2012)

Telltales *The Walking Dead* er et av de mest kjente interaktive
fortellingsspillene. Du spiller Lee Everett, som må beskytte den unge
jenta Clementine i en zombieapokalypse.

**Nøkkelfunksjoner:**
- Valg har konsekvenser flere episoder senere
- «Clementine will remember that» — spilleren får beskjed om at valget
  ble lagret
- Ingen «riktige» svar — bare vanskelige valg
- Karakterer du redder eller svikter, dukker opp igjen

**Hvorfor det er viktig å kjenne til:**
Telltale-spillene viste at interaktiv historiefortelling kan nå et massivt
publikum og være like følelsesladet som film og TV.

#### Escape rooms — fysisk interaktiv historiefortelling

Escape rooms (rømningsrom) er en fysisk form for interaktiv historiefortelling.
Du og teamet ditt blir låst inn i et rom og må løse oppgaver for å komme ut
innen 60 minutter.

**Hvordan historiefortelling fungerer i escape rooms:**
- **Tema og setting:** Du er i et gammelt Egypt, på en romstasjon eller i
  et forlatt fengsel
- **Karakterer:** Noen escape rooms har skuespillere som gir deg hint
- **Progresjon:** Hver løst oppgave avslører mer av historien
- **Climax:** Den siste oppgaven avslører den store vrien

**Eksempel:** I escape rommet *The Control Room* må du aktivere en tidsmaskin.
Etter hvert som du løser oppgaver, får du vite hvem som bygde maskinen og
hvorfor — og om du stoler på stemmen som gir deg instruksjoner.

---

### Transmedia storytelling — en historie på tvers av plattformer

Transmedia storytelling betyr at én historie fortelles på tvers av flere
medier. Du må oppsøke flere plattformer for å få hele historien.

**Eksempler på transmedia:**

| Plattform | Rolle i historien | Eksempel |
|-----------|-------------------|----------|
| Film | Hovedhistorien | Star Wars-filmene |
| TV-serie | Bihistorier | The Mandalorian |
| Spill | Du opplever selv | Star Wars: Jedi Fallen Order |
| Nettside | Bakgrunnsinfo | Star Wars databank |
| Tegneserie | Ukjente kapitler | Star Wars: Darth Maul |
| Social media | Karakterenes dagbøker | In-universe Twitter-kontoer |

**Hvorfor bruke transmedia?**
1. **Dybde:** Historien blir rikere når du får flere perspektiver
2. **Engasjement:** Publikum kan dykke så dypt de vil
3. **Fellesskap:** Fans diskuterer teorier på tvers av plattformer
4. **Inntekter:** Flere produkter å selge

**Eksempel — The Matrix:**
- Filmene: Neo vs maskinene
- *Animatrix* (anime): Hvordan krigen startet
- Spillene (Enter the Matrix): Scener som ikke er med i filmene
- Tegneserier: Karakterenes bakgrunnshistorier

For deg som VG1-elev: transmedia storytelling er en perfekt måte å tenke
større rundt egne prosjekter. Kanskje podkasten din kan ha en Instagram-konto
der karakterene poster? Eller nettsiden har en blogg som utfolder historien?


---

### Spillfortelling — særtrekk ved narrativ i spill

Spill har noen unike fordeler når det gjelder historiefortelling:

**1. Miljøfortelling (environmental storytelling)**
Historien fortelles gjennom omgivelsene. I *The Last of Us* ser du et
nedlagt barnerom med en tegning på veggen — du trenger ikke en forteller
for å forstå tragedien.

**2. Systemisk historiefortelling**
Historien oppstår fra spillmekanikkene. I *Minecraft* eller *The Sims*
skaper spilleren sin egen historie gjennom handlinger.

**3. Dialogtrær**
Snakk med karakterer og velg svar. Hver samtale åpner eller stenger
muligheter.

**4. Cutscenes og QTEs**
Mellomsekvenser (cutscenes) driver historien, mens Quick Time Events
lar spilleren påvirke action-sekvenser. Men pass på — for mange QTE-er
kan føles som et avbrudd.

**5. Spilleren som karakter**
Jo mer spilleren føler at valgene *betyr* noe, jo sterkere blir
tilknytningen til historien. Derfor har mange spill «morality meters»
eller «reputation systems».

---

## 🛠️ Prøv selv!

### 1. Lag en mini-branching-fortelling i Twine
Åpne [Twinery.org](https://twinery.org/) og lag en fortelling med minst
8 passuser og 3 forskjellige slutter. Tema: «Du våkner på et romskip
og vet ikke hvem du er». Bruk variabler ($helse, $nøkkel) for å holde
styr på spillerens status. Test på en medelev.

### 2. Analyser et interaktivt verk
Velg ett av disse: Bandersnatch, The Walking Dead (spillet), Life is Strange
eller en escape room du har prøvd. Analyser:
- Hvilke typer valg får du? (Moral, strategi, personlighet?)
- Har valgene reelle konsekvenser? Hvordan merker du det?
- Hvordan skapes engasjement?
Skriv en analyse på ca. 200 ord.

### 3. Design en transmedia-opplevelse
Ta en historie du kjenner (en film, et spill, en bok) og design hvordan
du kunne fortalt den på tvers av 3 plattformer. Eksempel: Hva om Harry
Potter hadde en TikTok der Voldemort poster propagandavideoer? Lag en
enkel skisse/plan for hva hver plattform inneholder.

---

## 📋 Nøkkelbegreper

| Begrep | Forklaring |
|--------|------------|
| **Branching narrative** | Forgrenet fortelling der spilleren tar valg som påvirker historiens retning. |
| **Samlingspunkt** | Punkt i historien der flere forgreninger samles igjen. |
| **Kritisk valg** | Valg som faktisk endrer historiens forløp. |
| **Tilsynelatende valg** | Valg som føles viktige, men fører til samme punkt (illusjon av frihet). |
| **Transmedia storytelling** | Én historie fortalt på tvers av flere plattformer. |
| **Miljøfortelling** | Historien fortelles gjennom omgivelsene og objektene i dem. |
| **Dialogtre** | Grensesnitt for samtaler der du velger svaralternativer. |
| **QTE (Quick Time Event)** | Tidsbestemt knappetrykk under action-sekvenser. |
| **Systemisk fortelling** | Historien oppstår fra interaksjonen mellom spillmekanikker. |
| **Escape room** | Fysisk eller digital opplevelse der du løser oppgaver for å «rømme». |

---

## 📚 Kilder

- NDLA — Produksjon og historiefortelling: [Interaktivitet og historiefortelling](https://ndla.no/f/produksjon-og-historiefortelling-im-ikm-vg1/6b4ff88031e7)
- IM Fagboka — [docs.iktim.no/1IM/](https://docs.iktim.no/1IM/)
- [Twine](https://twinery.org/) — Interaktiv historiefortelling
- [Ink (Inkle Studios)](https://www.inklestudios.com/ink/) — Scriptspråk for interaktiv fiksjon
- [ChoiceScript](https://www.choiceofgames.com/make-your-own-games/choicescript-intro/) — Lag interaktive romaner
- [Ren'Py](https://www.renpy.org/) — Visuell roman-motor
- Netflix — [Black Mirror: Bandersnatch](https://www.netflix.com/title/80988062)
- Telltale Games — [The Walking Dead](https://telltale.com/)
- [Interactive Fiction Database](https://ifdb.org/) — Database over interaktive fortellinger
