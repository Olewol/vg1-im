---
title: "Internett, skytjenester og webinfrastruktur"
emne: internett-og-skytjenester
fag: teknologiforstaelse
uke: [38, 39]
kompetansemaal: [tf-09]
kilder:
  - https://ndla.no/f/teknologiforstaelse-im-ikm-vg1/087c23101fc5
  - https://docs.iktim.no/1IM/
  - https://www.nsm.no/
  - https://www.uio.no/studier/emner/matnat/ifi/IN1020/h23/timeplan/in1020-internett-forelesning-uke4.pdf
tags: [internett, sky, dns, hosting, CDN, infrastruktur, skytjenester]
relatert:
  - teknologiforstaelse/digital-kommunikasjon
  - teknologiforstaelse/lokale-nettverk
  - teknologiforstaelse/datasikkerhet
---

# Internett, skytjenester og webinfrastruktur

## 🎯 Hva skal du lære?

Du skal forstå hvordan internett er bygget opp — fra fysiske kabler til tjenestene du bruker hver dag. Du lærer om DNS, skytjenester (IaaS, PaaS, SaaS), hvordan data lagres og hentes, og hvilke sikkerhetshensyn som gjelder.

---

## 📘 Fagstoff

### Hvordan internett er bygget

Internett er ikke "en sky" — det er et fysisk nettverk av kabler, rutere og servere over hele verden.

**Fysisk infrastruktur:**
- **Sjøkabler:** 99 % av internasjonalt data går gjennom fiberoptiske kabler på havbunnen
- **Datasentre:** Bygninger fulle av servere som lagrer og behandler data
- **IXP (Internet Exchange Point):** Knutepunkt hvor nettverk møtes og utveksler trafikk
- **ISP (Internet Service Provider):** Selskapet du betaler for internettilgang (Telenor, Telia, Altibox)

**Veien en datapakke tar:**
1. PC-en din → hjemmeruter → ISP → regionale nettverk → IXP → datasenter → målserver
2. Svar returnerer samme vei — ofte på under 100 millisekunder

### DNS — Internettets telefonkatalog

**DNS (Domain Name System)** oversetter domenenavn som `vg.no` til IP-adresser som `195.88.127.22`. Uten DNS måtte du husket tallrekker for hver nettside.

**Slik fungerer et DNS-oppslag:**
1. Du skriver `www.vg.no` i nettleseren
2. Nettleseren spør DNS-serveren (ofte ISP-en din eller 8.8.8.8)
3. DNS-serveren finner IP-adressen og sender den tilbake
4. Nettleseren kobler til IP-adressen og laster nettsiden

> DNS er også et sikkerhetsmål — **DNS-spoofing** kan omdirigere deg til falske nettsider uten at du merker det.

### Skytjenester

"Skyen" betyr at data og tjenester lagres på servere du kobler til via internett — ikke på din egen maskin.

**Tre hovedtyper skytjenester:**

| Type | Forklaring | Eksempel |
|------|-----------|----------|
| **IaaS** (Infrastructure as a Service) | Leie av virtuelle servere og lagring | AWS EC2, Google Cloud, Azure |
| **PaaS** (Platform as a Service) | Plattform for å utvikle og deploye apper | Vercel, Netlify, Heroku |
| **SaaS** (Software as a Service) | Programvare du bruker via nettleser | Google Docs, Office 365, Slack |

**Fordeler med skyen:**
- Tilgjengelig hvor som helst med internett
- Automatisk oppdatering og sikkerhet
- Betal for det du bruker (skalerbart)
- Ingen egen maskinvare å vedlikeholde

**Ulemper:**
- Avhengig av internettforbindelse
- Data lagres hos tredjepart (personvern)
- Løpende kostnader
- Leverandørlåsning — vanskelig å bytte

### CDN — Content Delivery Network

Et CDN er et nettverk av servere spredt over hele verden som lagrer kopier av nettsider og filer. Når du besøker en nettside, henter du data fra nærmeste server — raskere lasting.

**Kjente CDN-leverandører:** Cloudflare, Akamai, Fastly

### Sikkerhet på internett

- **HTTPS:** Kryptert kommunikasjon mellom deg og nettsiden (se hengelås-ikonet)
- **VPN:** Krypterer all trafikk og skjuler IP-adressen din
- **Brannmur:** Blokkerer uønsket trafikk
- **SSL/TLS-sertifikater:** Bekrefter at nettsiden er den den utgir seg for

---

## 💡 Praktiske eksempler

**Eksempel 1: Finn IP-adressen til en nettside**
Åpne terminal/kommandolinje og skriv: `ping vg.no` eller `nslookup vg.no`
Du vil se IP-adressen og hvor lang tid det tar å nå serveren.

**Eksempel 2: Sky eller lokalt?**
Se på tjenestene du bruker daglig. Er de skybaserte (SaaS) eller lokalt installert?
- Google Docs → SaaS (sky)
- Adobe Photoshop → kan være begge deler (Creative Cloud er SaaS, klassisk er lokalt)
- Spotify → SaaS (sky, men med lokal caching)

**Eksempel 3: Hva koster skyen?**
En enkel nettside på Vercel koster 0 kr. En virtuell server hos AWS koster fra 50 kr/måneden. Et helt datasenter koster millioner. Hvorfor tror du bedrifter velger ulike løsninger?

---

## 🔗 Tverrfaglige koblinger

- **Konseptutvikling og programmering:** Når du lager nettsider, må du forstå hvordan de publiseres og nås via internett. DNS, hosting og domener er praktisk kunnskap for webutvikling (kp-05)
- **Produksjon og historiefortelling:** Strømming av video og lyd krever god infrastruktur. Kunnskap om båndbredde og CDN er relevant for medieproduksjon (ph-01)
- **Samfunnsfag:** Internettilgang er en demokratisk rettighet. Digitalt utenforskap og nettneutralitet er samfunnsaktuelle temaer

---

## 📚 Kilder

- NDLA — [Digital kommunikasjon](https://ndla.no/f/teknologiforstaelse-im-ikm-vg1/087c23101fc5)
- IM Fagboka — [Nettverk](https://docs.iktim.no/1IM/)
- NSM — [Nasjonal sikkerhetsmyndighet: Råd om internett-sikkerhet](https://nsm.no/)
- Cloudflare — [How DNS works (animert)](https://www.cloudflare.com/learning/dns/what-is-dns/)
- uio — [Forelesning: Hvordan internett fungerer](https://www.uio.no/studier/emner/matnat/ifi/IN1020/h23/timeplan/in1020-internett-forelesning-uke4.pdf)
