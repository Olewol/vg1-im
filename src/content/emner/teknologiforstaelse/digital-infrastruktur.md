---
title: "Digital infrastruktur og skytjenester"
emne: digital-infrastruktur
fag: teknologiforstaelse
uke: [45, 46]
kompetansemaal: [tf-09]
kilder:
  - https://docs.iktim.no/1IM/
  - https://azure.microsoft.com/nb-no/
  - https://aws.amazon.com/no/
  - https://ndla.no/f/teknologiforstaelse-im-ikm-vg1/
tags: [infrastruktur, servere, sky, saas, datasentre, virtualisering, it-drift]
relatert:
  - teknologiforstaelse/internett-og-skytjenester
  - teknologiforstaelse/lokale-nettverk
  - teknologiforstaelse/digital-kommunikasjon
  - teknologiforstaelse/operativsystemer-og-programvare
---

# Digital infrastruktur og skytjenester

## 🎯 Hva skal du lære?

Du skal forstå hva digital infrastruktur er, hvordan datasentre fungerer, hvilke typer servere som finnes, og hvordan skytjenester har endret måten vi lagrer og prosesserer data på. Du lærer også om fordelene og ulempene med sky vs. lokale løsninger.

---

## 📘 Fagstoff

### Hva er digital infrastruktur?

Digital infrastruktur er den fysiske og logiske underbygningen som gjør digitale tjenester mulig. Tenk på det som *veinettet for data* — uten infrastruktur ville ikke nettsider, e-post eller streaming fungert.

Digital infrastruktur består av:

| Lag | Eksempler |
|-----|-----------|
| **Fysisk maskinvare** | Servere, kabler, rutere, svitsjer |
| **Nettverk** | Internett, fiber, 5G, WiFi |
| **Programvare** | Operativsystemer, database, web-server |
| **Tjenester** | E-post, skylagring, streaming |
| **Sikkerhet** | Brannmurer, kryptering, autentisering |

---

### Typer servere

En server er en datamaskin som leverer tjenester til andre datamaskiner (klienter). Forskjellen på en vanlig PC og en server er at servere er bygget for stabilitet, oppetid og samtidige tilkoblinger.

| Servertype | Funksjon | Eksempler |
|-----------|----------|-----------|
| **Webserver** | Leverer nettsider til nettleseren | Apache, Nginx, IIS |
| **Filserver** | Lagrer og deler filer på nettverket | SAMBA, Windows File Server, NAS |
| **Databaseserver** | Lagrer og organiserer data i databaser | MySQL, PostgreSQL, Microsoft SQL |
| **E-postserver** | Håndterer sending og mottak av e-post | Exchange, Postfix |
| **DNS-server** | Oversetter domenenavn til IP-adresser | Bind, Microsoft DNS |
| **DHCP-server** | Tildeler IP-adresser automatisk til enheter | Innebygget i ruter/Windows Server |
| **Applikasjonsserver** | Kjører spesifikke forretningsprogrammer | Tomcat, IIS med .NET |

#### Tjener-klient-modellen

I tjener-klient-modellen ber klienter (PC-er, mobiler, nettbrett) om tjenester fra en eller flere servere:

```
Klient ── spør ──► Server
Klient ◄─ svar ── Server
```

Fordelen er at flere klienter kan dele samme server, og man kan administrere data sentralt i stedet for på hver enkelt klient.

---

### Datasentre — hjertet av internett

Et datasenter er en bygning eller et rom fylt med servere, lagring og nettverksutstyr. Det er her internett *bor*.

#### Hva finnes i et datasenter?

- **Tusenvis av servere** stablet i rack
- **Strømforsyning:** Flere redundante strømkilder, UPS (batteri-backup), nødaggregat
- **Kjøling:** Luftkjøling eller væskekjøling for å fjerne varme
- **Nettverk:** Fiber-tilkobling til resten av verden, interne svitsjer
- **Sikkerhet:** Adgangskontroll, kameraer, brannslukking
- **Backup:** Flere kopier av data på forskjellige fysiske steder

#### Datasentre i Norge

Norge har blitt et attraktivt land for datasentre på grunn av:
- **Billig fornybar strøm** (vannkraft)
- **Kaldt klima** (naturlig kjøling)
- **Politisk stabilitet** og god digital infrastruktur

Norske datasentre inkluderer:
| Navn | Sted | Spesialitet |
|------|------|-----------|
| Green Mountain | Rjukan, Stavanger | Vannkraft, tidligere NATO-bunker |
| Lefdal Mine | Måløy | Gruve-datasenter, 100 % fornybar |
| Bulk Infrastructure | Stavanger, Hamar | Bærekraftige hyperscale-sentre |

> Et enkelt stort datasenter kan bruke like mye strøm som en norsk by med 30 000 innbyggere. Derfor er klimavennlig drift og plassering i kaldt klima viktig.

---

### Skytjenester

Skyen (the cloud) er en fellesbetegnelse på IT-tjenester som leveres over internett. I stedet for å ha servere i kjelleren, leier du kapasitet fra en sky-leverandør.

#### IaaS, PaaS og SaaS

| Modell | Forklaring | Eksempel | Du styrer | Leverandør styrer |
|--------|-----------|----------|-----------|------------------|
| **SaaS** | Programvare som tjeneste — alt ferdig satt opp | Google Docs, Microsoft 365, Teams | Ingenting | Alt |
| **PaaS** | Plattform som tjeneste — utviklingsmiljø | Google App Engine, Heroku | Applikasjon og data | Plattform, servere |
| **IaaS** | Infrastruktur som tjeneste — leie av servere | AWS EC2, Azure VM | Alt fra OS og opp | Fysiske servere, nettverk |

#### Store sky-leverandører

| Leverandør | Markedsandel (2025) | Styrke |
|-----------|-------------------|--------|
| **Amazon Web Services (AWS)** | ~32 % | Størst, bredest tjenestekatalog |
| **Microsoft Azure** | ~23 % | Integrasjon med Microsoft 365, hybrid sky |
| **Google Cloud (GCP)** | ~11 % | Dataanalyse, AI/ML |
| **Oracle Cloud** | ~4 % | Database, enterprise |

#### Sky vs. lokalt (on-premise)

| Faktor | Sky | Lokalt (on-premise) |
|--------|-----|-------------------|
| **Kostnad** | Betal etter bruk | Høy investering, lavere over tid |
| **Skalerbarhet** | Enkelt å øke kapasitet | Må kjøpe ny maskinvare |
| **Sikkerhet** | Leverandørens ansvar (delt ansvar) | Full kontroll, men eget ansvar |
| **Tilgjengelighet** | Tilgjengelig hvor som helst | Bare på det lokale nettverket |
| **Vedlikehold** | Leverandøren håndterer | Eget IT-personell må drifte |

#### Hybrid sky

Mange bedrifter bruker en hybrid løsning: sensitiv data på egne servere (on-premise), mens mindre kritisk data og skalérbare tjenester kjøres i skyen.

---

### Lastbalansering og redundans

Når tusenvis av brukere skal nå samme tjeneste samtidig, trenger man smartere infrastruktur.

**Lastbalansering** fordeler trafikken på flere servere:
```
          ┌─ Server 1
Bruker ──► Lastbalanser ──┼─ Server 2
          ├─ Server 3
          └─ Server 4
```

Hvis én server går ned, tar de andre over (failover). Dette kalles **redundans** — å ha flere kopier av alt for å unngå nedetid.

Eksempel: Netflix har tusenvis av servere på AWS som leverer film til millioner av brukere samtidig. Hvis en server i USA går ned, sendes trafikken til servere i Europa.

---

## 💡 Praktiske eksempler

**Eksempel 1 — Netflix' infrastruktur**
Netflix bruker AWS til det meste:
- Videoene lagres på AWS S3 (skylagring)
- Når du trykker "Spill av", sendes videoen fra AWS CloudFront (CDN) — servere nær deg
- Anbefalinger (suggestions) kjøres på AWS EC2
- Netflix trenger ikke å drifte egne servere — de leier kapasitet og betaler for det de bruker

**Eksempel 2 — Skolens infrastruktur**
En videregående skole har:
- En lokal filserver på IT-rommet (on-premise) for ansattes hjemmeområder
- Microsoft 365 i skyen for elev-e-post, Teams og SharePoint
- En hybrid løsning der sensitive elevmapper lagres lokalt, mens samarbeidsdokumenter ligger i skyen

**Eksempel 3 — Starte en web-app**
En utvikler lager en nettside. Hun leier en virtuell server på Azure for 300 kr/mnd, installerer Apache og MySQL, og laster opp siden. Etter hvert som flere brukere kommer, skalerer hun opp til flere servere og legger til en lastbalanser — alt uten å kjøpe egen maskinvare.

---

## 🔗 Tverrfaglige koblinger

- **KOP-05 Webutvikling:** Webservere og deployment av nettsider
- **KOP-04 Database:** Databaser som del av infrastrukturen
- **TF-07 Bærekraft:** Datasentres strømforbruk og miljøpåvirkning
- **TF-10 Digitale trusler:** Sikkerhet i skyen, delt ansvarsmodell

---

## 📚 Kilder

- IM Fagboka — [docs.iktim.no/1IM/](https://docs.iktim.no/1IM/)
- Microsoft Azure — [azure.microsoft.com](https://azure.microsoft.com/nb-no/)
- AWS — [aws.amazon.com/no](https://aws.amazon.com/no/)
- Green Mountain — [greenmountain.no](https://www.greenmountain.no/)
- NDLA Teknologiforståelse
