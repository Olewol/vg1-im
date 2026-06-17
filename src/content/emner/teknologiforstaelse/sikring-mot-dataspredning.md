---
title: "Sikring mot dataspredning"
emne: sikring-mot-dataspredning
fag: teknologiforstaelse
uke: [40, 41]
kompetansemaal: [tf-12]
kilder:
  - https://www.nsm.no/veiledere/
  - https://www.norsis.no/
  - https://www.datatilsynet.no/
  - https://ndla.no/f/teknologiforstaelse-im-ikm-vg1/
tags: [datasikkerhet, kryptering, backup, tilgangskontroll, risikostyring, mfa]
relatert:
  - teknologiforstaelse/datasikkerhet
  - teknologiforstaelse/personvern
  - teknologiforstaelse/brukerenheter-og-administrasjon
---

# Sikring mot dataspredning

## 🎯 Hva skal du lære?

Du skal kunne vurdere risiko for uønsket spredning av data, og du skal lære om konkrete tiltak du kan anbefale og kvalitetssikre for å redusere denne risikoen. Dette handler om å beskytte data — både for deg selv, for bedrifter og for samfunnet.

---

## 📘 Fagstoff

### Hva er dataspredning?

Dataspredning er når data kommer på avveie — enten ved et uhell eller med vilje. Det kan være:

- **Lekkasje:** En ansatt sender en fil til feil mottaker
- **Tyveri:** En hacker stjeler en kundedatabase
- **Tapping:** Uvedkommende får tilgang til data i et system
- **Ransomware:** Data låses og kreves løsepenger for

> **Visste du?** I 2024 ble over 10 milliarder poster lekket globalt. Gjennomsnittskostnaden for et datainnbrudd var over 50 millioner kroner for store bedrifter.

---

### Kryptering — datalås for det 21. århundre

Kryptering gjør data uleselige for alle som ikke har nøkkelen. Det er som å sette innholdet i en safe.

**Symmetrisk kryptering** — samme nøkkel brukes til både å låse og låse opp
- Raskt, effektivt for store datamengder
- Eksempler: AES, ChaCha20
- Utfordring: hvordan overlevere nøkkelen sikkert?

**Asymmetrisk kryptering** — to nøkler: én offentlig og én privat
- Den offentlige nøkkelen kan alle ha, den private er hemmelig
- Eksempler: RSA, ECC
- Brukes i HTTPS, epost-kryptering, signaturer

**Kryptering i forskjellige tilstander:**

| Tilstand | Hva betyr det? | Teknologi |
|----------|----------------|-----------|
| **Data i hvile** (at rest) | Lagret på disk, minnepenn, sky | BitLocker, FileVault, LUKS |
| **Data i transitt** | På vei over nettverket | TLS/SSL (HTTPS), VPN |
| **Data i bruk** | Behandles i minnet | FHE (under utvikling) |

En vanlig feil er å tro at skyen automatisk er kryptert. Sky-leverandører som Google og Microsoft krypterer data i hvile som standard, men du som bruker må ofte aktivere ekstra sikkerhet.

---

### Sikkerhetskopiering — backup og gjenoppretting

3-2-1-regelen er gullstandarden for backup:

| Regel | Forklaring |
|-------|-----------|
| **3** kopier av dataene | Original + minst 2 backup-kopier |
| **2** forskjellige medier | F.eks. ekstern disk + sky |
| **1** kopi utenfor bedriften | Brann, vann, tyveri i lokalet må ikke ta all data |

#### Typer backup

| Type | Hva lagres? | Lagringsplass | Gjenoppretting |
|------|------------|--------------|----------------|
| Full backup | Alt | Mye | Raskest |
| Inkrementell | Endringer siden siste backup | Lite | Trenger full + alle inkrementelle |
| Differensiell | Endringer siden siste full backup | Middels | Trenger full + siste differensielle |

**Husk:** En backup du aldri tester er ikke en backup. Hvis du aldri har prøvd å gjenopprette, vet du ikke om backupen faktisk fungerer.

---

### Tilgangskontroll

#### Minste privilegium (Principle of Least Privilege)

En bruker eller et system skal bare ha de tilgangene som er nødvendige for å utføre oppgaven — verken mer eller mindre.

- En kundeservicemedarbeider trenger å se kundeinformasjon, men ikke å endre lønnssystemet
- En fotograf trenger tilgang til bildearkivet, men ikke til regnskapssystemet

#### To-faktor-autentisering (2FA/MFA)

MFA (Multi-Factor Authentication) kombinerer minst to av disse:

| Faktor | Eksempel |
|--------|----------|
| Noe du **vet** | Passord, PIN-kode |
| Noe du **har** | Mobiltelefon, sikkerhetsnøkkel (YubiKey) |
| Noe du **er** | Fingeravtrykk, ansiktsgjenkjenning |

> Uten MFA er passordet ofte det eneste som stopper uvedkommende. Med MFA må en hacker både ha passordet OG telefonen din.

#### Rollebasert tilgangskontroll (RBAC)

RBAC grupperer rettigheter etter rolle:
- **Admin:** full tilgang til alt
- **Redaktør:** kan opprette og redigere innhold
- **Leser:** kan bare se innhold
- **Gjest:** minimal tilgang

---

### Brannmur og nettverkssikkerhet

En brannmur er en barriere mellom nettverk som kontrollerer hvilken trafikk som får passere.

| Type | Hva den gjør | Eksempel |
|------|-------------|----------|
| **Nettverksbrannmur** | Filtrerer trafikk mellom nettverk | Cisco ASA, pfSense |
| **Vertsbasert brannmur** | Kjører på enheten selv | Windows Defender Firewall |
| **Neste generasjon (NGFW)** | Dybdepakkeinspeksjon, applikasjonskontroll | Fortinet, Palo Alto |

#### VLAN-segmentering

Et VLAN (Virtual Local Area Network) deler opp et fysisk nettverk i flere logiske nettverk. Hvis en angriper kommer inn på gjeste-WiFi, skal de ikke automatisk ha tilgang til servere og printere.

---

### Oppdaterings- og patch-rutiner

De fleste angrep utnytter kjente sårbarheter — hull som allerede har en løsning (patch) fra produsenten. Å holde systemer oppdatert er derfor **det viktigste enkelttiltaket**.

- **Automatiske oppdateringer:** Slå på for OS og programvare
- **Patch-tirsdag:** Microsoft ruller ut oppdateringer annenhver tirsdag
- **Sårbarhetsdatabase:** CVE (Common Vulnerabilities and Exposures) viser kjente hull

---

## 💡 Praktiske eksempler

**Eksempel 1 — Angrep med ransomware**
En mellomstor bedrift blir rammet av ransomware. Alle filer krypteres, og det kreves 500 000 kr i løsepenger. Fordi de hadde 3-2-1-backup med ukentlig testing, kunne IT-sjefen si: "Vi gjenoppretter fra backup" — null løsepenger betalt.

**Eksempel 2 — Lekkasje av kundedata**
En ansatt i en kommune sender en e-post med vedlegg som inneholder personopplysninger om 2000 innbyggere. Feilen? Vedkommende skrev feil e-postadresse. Slike hendelser kan unngås med krypterte e-postløsninger og varsler før sending.

**Eksempel 3 — Skoles 2FA**
Skolen innfører MFA for alle lærere og elever. Når en elev mister mobilen, kan vedkommende fortsatt logge seg på via en reservekode eller en SMS. Skolen kombinerer passord med engangskoder, og risikoen for uautorisert tilgang går kraftig ned.

---

## 🔗 Tverrfaglige koblinger

- **KOP-01 Regelverk:** Ansvarlig håndtering av data, åndsverkloven
- **PHF-07 Etikk:** Etisk refleksjon rundt datahåndtering og overvåking
- **TF-11 Personvern:** GDPR og behandling av personopplysninger — nært beslektet med sikring mot dataspredning

---

## 📚 Kilder

- NSM (Nasjonal sikkerhetsmyndighet) — [nsm.no/veiledere](https://www.nsm.no/veiledere/)
- NorSIS — [norsis.no](https://www.norsis.no/)
- Datatilsynet — [datatilsynet.no](https://www.datatilsynet.no/)
- NDLA Teknologiforståelse
