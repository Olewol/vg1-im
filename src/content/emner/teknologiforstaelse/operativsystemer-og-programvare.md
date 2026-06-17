---
title: "Operativsystemer og programvare"
emne: operativsystemer-og-programvare
fag: teknologiforstaelse
uke: [42, 43]
kompetansemaal: [tf-05, tf-03]
kilder:
  - https://docs.iktim.no/1IM/
  - https://learn.microsoft.com/nb-no/
  - https://ubuntu.com/
  - https://ndla.no/f/teknologiforstaelse-im-ikm-vg1/
tags: [operativsystem, windows, macos, linux, lisenser, virtualisering, programvare]
relatert:
  - teknologiforstaelse/praktisk-it
  - teknologiforstaelse/brukerenheter-og-administrasjon
  - teknologiforstaelse/digital-infrastruktur
---

# Operativsystemer og programvare

## 🎯 Hva skal du lære?

Du skal forstå hva et operativsystem er, hvilke typer operativsystemer som finnes, og hvordan du installerer og konfigurerer dem. Du lærer også om programvarelisenser og virtualisering — sentrale temaer i IT-bransjen.

---

## 📘 Fagstoff

### Hva er et operativsystem?

Et operativsystem (OS) er programvaren som fungerer som et mellomledd mellom maskinvaren og programmene du bruker. Det håndterer:

- **Prosesser:** Hvilke programmer som kjører og når
- **Minne:** Hvilken del av RAM som er i bruk
- **Lagring:** Hvordan filer organiseres på disk
- **Enheter:** Kommunikasjon med tastatur, skjerm, mus, skriver
- **Sikkerhet:** Tilgangskontroll, brukerkontoer

**Kjernen** (kernel) er hjertet i operativsystemet — den delen som alltid kjører og har full kontroll over maskinvaren.

### Ulike operativsystemer

| OS | Utvikler | Kjennetegn | Bruksområde |
|----|----------|-----------|-------------|
| **Windows 11** | Microsoft | Mest utbredt på kontor, støtter mest programvare | Allmenn bruk, gaming, kontor, enterprise |
| **Windows Server** | Microsoft | Versjon for servere, støtter Active Directory | Serverdrift, bedriftsnettverk |
| **macOS** | Apple | Unix-basert, intuitivt, godt for kreativt arbeid | Medieproduksjon, utvikling, design |
| **Linux (Ubuntu, Debian, Fedora)** | Åpen kildekode | Gratis, stabilt, ekstremt konfigurerbart | Server, programmering, embeddet |
| **iOS** | Apple | Lukket økosystem, sterk sikkerhet | Mobil, nettbrett |
| **Android** | Google | Åpent, tilpassbart, bred enhetsstøtte | Mobil, nettbrett, TV |

#### Windows

Windows er det mest brukte operativsystemet i norske bedrifter. Det kjennetegnes av:
- Grafisk grensesnitt med Start-meny og oppgavelinje
- .exe- og .msi-installasjoner
- Active Directory-integrasjon (domene)
- Stort utvalg av programvare og spill

#### macOS

MacOS er populært i design- og mediebransjen:
- Bygger på Unix — har terminal og POSIX-kompatibilitet
- Tett integrasjon med iPhone/iPad (AirDrop, Universal Clipboard)
- Programvare som Final Cut Pro, Logic Pro og Adobe-pakken kjører optimalt

#### Linux

Linux er en åpen kildekode-kjerne som brukes i alt fra smartklokker til superdatamaskiner:
- **Ubuntu:** Nybegynnervennlig, godt fellesskap
- **Debian:** Stabilt, grunnlaget for Ubuntu
- **Fedora:** Ny teknologi, Red Hat-tilknytning
- **Ubuntu Server:** Verdens mest brukte server-OS

> **Over 90 % av verdens servere kjører Linux** (inkludert de fleste webservere, Google, Amazon, Facebook). Likevel bruker de fleste ansatte Windows på jobb-PCen.

---

### Installasjon og oppsett

#### Clean install vs oppgradering

| Metode | Beskrivelse | Fordeler | Ulemper |
|--------|------------|----------|---------|
| **Clean install** | Sletter alt og installerer på nytt | Raskt, rent, fjerne problemer | Mister data og innstillinger |
| **Oppgradering** | Installerer over eksisterende OS | Beholder filer og innstillinger | Kan arve problemer |

#### Partisjonering og filsystemer

Før du installerer et OS må du partisjonere disken. Det betyr å dele den opp i områder med ulike formater:

| Filsystem | OS | Maks filstørrelse | Funksjoner |
|-----------|-----|-------------------|-----------|
| **NTFS** | Windows | 16 TB | Kryptering, komprimering, tilgangskontroll |
| **APFS** | macOS | Ubegrenset | Snapshots, kryptering, effektiv plassbruk |
| **ext4** | Linux | 16 TB | Journalføring, stabil, åpen |

#### Boot-prosess (UEFI/BIOS)

Når du slår på en datamaskin skjer dette:

1. **POST** (Power-On Self Test) — maskinvaren sjekker seg selv
2. **UEFI/BIOS** — finner hvilken enhet som skal bootes fra
3. **Bootloader** — laster inn operativsystemets kjerne
4. **Kernel** — starter opp systemet
5. **Tjenester og GUI** — logger på og jobber

**UEFI** er den moderne erstatningen for BIOS. Den støtter større disker, raskere oppstart, og grafisk grensesnitt.

---

### Programvare og lisenser

Programvare kan deles inn i to hovedkategorier basert på lisens:

#### Åpen kildekode (FOSS — Free and Open Source Software)

- Kildekoden er tilgjengelig for alle
- Du kan laste ned, endre og distribuere fritt
- **Eksempler:** Linux, Firefox, GIMP, LibreOffice, VLC
- **Lisenser:** GPL (må dele endringer), MIT (kan lukkes), Apache 2.0

#### Proprietær programvare

- Kildekoden er hemmelig
- Du kjøper en lisens til å **bruke** programvaren, ikke eie den
- **Eksempler:** Adobe Creative Cloud, Microsoft Office, Photoshop
- **Lisensmodeller:** Per-sete, abonnement, enterprise-avtale

#### Eksempler fra IM-bransjen

| Oppgave | Proprietær | Åpen kildekode |
|---------|-----------|---------------|
| Fotoredigering | Adobe Photoshop | GIMP |
| Videoredigering | Adobe Premiere, Final Cut | DaVinci Resolve, Shotcut |
| Kontor | Microsoft 365 | LibreOffice, OnlyOffice |
| 3D-modellering | Autodesk Maya | Blender |

---

### Virtualisering

Virtualisering lar deg kjøre flere operativsystemer samtidig på én fysisk maskin. Hvert OS kjører i sin egen **virtuelle maskin (VM)**.

#### Hvorfor virtualisere?

- **Teste** et OS uten å installere det på hovedmaskinen
- **Serverkonsolidering:** En fysisk server kan kjøre 10 virtuelle servere
- **Sandkasse:** Test usikker programvare uten å sette hovedsystemet i fare
- **Ulike plattformer:** Kjør Linux på en Mac, eller Windows på en Linux-maskin

#### Virtuelle maskin-verktøy

| Verktøy | Plattformer | Type |
|---------|-----------|------|
| **VirtualBox** | Windows, Mac, Linux | Gratis, åpen kildekode |
| **VMware Workstation** | Windows, Linux | Kommersiell, mye brukt i bedrifter |
| **Hyper-V** | Windows | Innebygd i Windows Pro/Enterprise |
| **UTM** | Mac (Apple Silicon) | Gratis, bruker QEMU |

#### Container-virtualisering (Docker)

I stedet for å virtualisere hele maskinen, kan man virtualisere bare programmet. Containere deler verts-OSets kjerne men isolerer programmet og avhengighetene.

- **Docker** er den mest brukte container-plattformen
- Brukes mye i moderne IT-drift og utvikling
- Lettere og raskere enn fulle VM-er

---

## 💡 Praktiske eksempler

**Eksempel 1 — Installere Linux i VirtualBox**
Du har Windows på skole-PCen, men vil lære Linux. Du laster ned Ubuntu og VirtualBox, oppretter en ny virtuell maskin med 4 GB RAM og 25 GB disk, og installerer Ubuntu som et program inni Windows. Nå har du begge OS-ene samtidig.

**Eksempel 2 — Velge programvare for et mediebyrå**
Et mediebyrå må velge mellom Adobe Creative Cloud (1490 kr/mnd) og åpen kildekode-alternativer (gratis). Argumenter for Adobe: bransjestandard, integrasjon, support. Argumenter for FOSS: ingen lisenskostnader, kan tilpasses, frihet.

**Eksempel 3 — Vurdere OS til ulike roller**
- **Grafisk designer:** macOS eller Windows med Adobe-pakken
- **Systemutvikler:** Linux for servere, macOS for utviklings-PC
- **IT-driftstekniker:** Windows for klientadministrasjon, Linux for servere
- **Spillutvikler:** Windows (bredest støtte) eller Linux (nyere spillmotorer)

---

## 🔗 Tverrfaglige koblinger

- **KOP-03 Programmering:** Linux-terminal, skripting, utviklingsmiljø
- **YFF:** Lisenskostnader i bedrift, valg av programvare i arbeidslivet
- **TF-07 Bærekraft:** Virtualisering reduserer antall fysiske servere og strømforbruk

---

## 📚 Kilder

- IM Fagboka — [docs.iktim.no/1IM/](https://docs.iktim.no/1IM/)
- Microsoft Learn — [learn.microsoft.com](https://learn.microsoft.com/)
- Ubuntu-dokumentasjon — [ubuntu.com](https://ubuntu.com/)
- NDLA Teknologiforståelse
