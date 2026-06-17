---
title: "Brukerenheter og administrasjon"
emne: brukerenheter-og-administrasjon
fag: teknologiforstaelse
uke: [38, 39]
kompetansemaal: [tf-05]
kilder:
  - https://docs.iktim.no/1IM/
  - https://learn.microsoft.com/nb-no/training/
  - https://www.jamf.com/
  - https://ndla.no/f/teknologiforstaelse-im-ikm-vg1/
tags: [klientadministrasjon, mdm, enhetsbehandling, it-drift, datamaskiner]
relatert:
  - teknologiforstaelse/praktisk-it
  - teknologiforstaelse/operativsystemer-og-programvare
  - teknologiforstaelse/lokale-nettverk
  - teknologiforstaelse/datasikkerhet
---

# Brukerenheter og administrasjon

## 🎯 Hva skal du lære?

Du skal forstå hva en brukerenhet er, hvordan ulike enheter er bygget opp, og hvordan IT-avdelinger administrerer hundrede eller tusenvis av enheter på en effektiv og sikker måte. Du lærer om komponentene i en datamaskin, administrasjonsplattformer og hvordan enheter kobles til sentrale systemer.

---

## 📘 Fagstoff

### Hva er en brukerenhet?

En brukerenhet er enhver enhet som en person bruker for å utføre arbeid, læring eller underholdning. I en IT-sammenheng snakker vi gjerne om:

| Type enhet | Eksempler | Typisk bruk |
|------------|-----------|-------------|
| Stasjonær PC | Windows-stasjoner, iMac | Kontor, produksjon, gaming |
| Bærbar PC | Dell Latitude, MacBook Pro | Fleksibelt arbeid, skole |
| Nettbrett | iPad, Microsoft Surface | Presentasjon, feltoppdrag |
| Smarttelefon | iPhone, Android | Kommunikasjon, apper |
| Printer/MFP | Xerox, HP LaserJet | Utskrift, scanning |
| IoT-enheter | Kameraer, sensorer | Overvåking, automasjon |

**Hvorfor er det viktig å kunne administrere disse?** Jo flere enheter en organisasjon har, desto viktigere er det å ha kontroll. Uten administrasjon kan enheter bli utdaterte, usikrede eller komme på avveie.

### Datamaskinens komponenter

For å forstå brukerenheter må du kjenne til hva som er inni dem:

| Komponent | Funksjon | Eksempler |
|-----------|----------|-----------|
| **CPU** (prosessor) | Utfører instruksjoner og beregninger | Intel Core i5/i7/i9, AMD Ryzen |
| **RAM** (minne) | Midlertidig lagring av aktive programmer | 8 GB, 16 GB, 32 GB DDR5 |
| **Lagring** | Permanent lagring av filer og OS | SSD (rask), HDD (stor kapasitet) |
| **Hovedkort** | Kobler alle komponenter sammen | ATX, Micro-ATX |
| **Grafikkort** | Prosesserer bilde og video | NVIDIA GeForce, AMD Radeon |
| **Strømforsyning** | Gir strøm til alle komponenter | 300 W — 1000 W |
| **Kabinett** | Fysisk beskyttelse og kjøling | Tower, SFF, Mini-PC |

**Sammenhengen mellom komponenter og ytelse:**

- **Mer RAM** → flere programmer kan kjøres samtidig uten treghet
- **SSD i stedet for HDD** → maskinen starter på sekunder i stedet for minutter
- **Raskere CPU** → tyngre oppgaver som videoredigering går raskere
- **Grafikkort** → avgjørende for 3D-modellering, videoredigering og naturligvis spill

### Administrasjonsplattformer

Når en organisasjon har mange enheter, trenger man en måte å administrere dem på fra et sentralt sted. Det kalles **MDM (Mobile Device Management)** eller **UEM (Unified Endpoint Management)**.

#### Hva kan administrasjonsplattformer gjøre?

- **Rulle ut oppdateringer:** Sørge for at alle enheter har siste sikkerhetsoppdateringer
- **Installere programvare:** Distribuere programvare til mange enheter samtidig
- **Håndheve sikkerhetspolicy:** Kreve passord, kryptering, slå av kamera
- **Sletting ved tap:** Fjernslette en enhet som er mistet eller stjålet
- **Rapportering:** Se status for alle enheter i organisasjonen

#### Kjente plattformer

| Plattform | Type | Vanlig bruksområde |
|-----------|------|--------------------|
| **Microsoft Intune** | MDM/UEM | Windows + mobil, integrert med Microsoft 365 |
| **Jamf** | MDM | Kun Apple-enheter (Mac, iPad, iPhone) |
| **VMware Workspace ONE** | UEM | Alle plattformer, hybrid miljø |
| **ManageEngine** | MDM | Kostnadseffektivt for mellomstore bedrifter |

#### Active Directory og Entra ID

**Active Directory (AD)** er Microsofts katalogtjeneste som lagrer informasjon om brukere, datamaskiner og ressurser i et nettverk. Når en PC kobles til AD, kalles det å være **domenetilkoblet**. Da kan IT-avdelingen styre pålogginger, tilganger og policyer sentralt.

**Microsoft Entra ID** (tidligere Azure AD) er skyversjonen, som fungerer på tvers av internett. Enheter kan administreres uansett hvor de befinner seg.

### Oppsett og konfigurasjon

#### Installasjon av operativsystem

Å installere et operativsystem (OS) er grunnleggende IT-kompetanse:

1. Last ned OS-installasjonsmedium (USB eller nettverk)
2. Boot fra installasjonsmediet (via BIOS/UEFI)
3. Partisjoner disken og velg filsystem
4. Gjennomfør installasjonen
5. Installer drivere for maskinvare
6. Installer programvare og oppdateringer

#### Nettverkskonfigurasjon

For at en brukerenhet skal fungere på nettverket må den ha:
- **IP-adresse** (statisk eller DHCP)
- **Subnettmaske** for å vite hvilket nettverk den er på
- **Standard gateway** for å komme til andre nettverk
- **DNS-server** for å oversette navn til IP-adresser

#### Automatisert oppsett (Imaging)

I store organisasjoner setter man ikke opp hver PC manuelt. Man bruker **imaging** — en ferdigkonfigurert mal (image) som rulles ut til mange enheter:

- **MDT (Microsoft Deployment Toolkit):** Automatisert Windows-distribusjon
- **Clonezilla:** Åpen kildekode-verktøy for diskkloning
- **Apple DEP/ABM:** Automatisk oppsett av Apple-enheter

---

## 💡 Praktiske eksempler

**Eksempel 1: Skole med 1000 iPader**
En videregående skole deler ut iPader til alle elever. Skolen bruker Jamf til å administrere dem:
- Alle iPader får forhåndsinstallerte apper
- Skolens WiFi-nøkkel er forhåndskonfigurert
- Hvis en iPad mistes, kan den fjernlåses og spores

**Eksempel 2: IT-avdeling ruller ut Windows-oppdateringer**
En bedrift med 500 ansatte bruker Intune til å rulle ut månedlige sikkerhetsoppdateringer. IT-avdelingen kan se hvilke PC-er som mangler oppdateringer og tvinge gjennom installasjon uten at ansatte må gjøre noe selv.

**Eksempel 3: Bygge en PC**
En IT-tekniker bygger en stasjonær PC for videoredigering. Hun velger:
- CPU: Intel Core i7 med innebygget grafikk
- RAM: 32 GB DDR5
- Lagring: 1 TB NVMe SSD
- Grafikkort: NVIDIA RTX 4060
- Strømforsyning: 650 W

Hvorfor disse valgene? Videoredigering krever mye RAM, rask lagring og et dedikert grafikkort.

---

## 🔗 Tverrfaglige koblinger

- **KOP-09 Dokumentasjon:** Når du setter opp enheter, må du dokumentere konfigurasjonen — hvilke innstillinger som er gjort og hvorfor
- **PHF-07 Kildekritikk:** Hvordan finne pålitelig informasjon om enhetskonfigurasjon og feilsøking
- **TF-10 Digitale trusler:** Uten administrasjon av enheter oppstår sikkerhetshull

---

## 📚 Kilder

- IM Fagboka — [docs.iktim.no/1IM/](https://docs.iktim.no/1IM/)
- Microsoft Learn — [learn.microsoft.com/nb-no/training/](https://learn.microsoft.com/nb-no/training/)
- Jamf — [jamf.com](https://www.jamf.com/)
- NDLA Teknologiforståelse
