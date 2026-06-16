---
title: "Lokale nettverk — Grunnleggende nettverksforståelse"
emne: lokale-nettverk
fag: teknologiforstaelse
uke: [36, 37]
kompetansemaal: [tf-04]
kilder:
  - https://ndla.no/f/teknologiforstaelse-im-ikm-vg1/087c23101fc5
tags: [nettverk, ip, subnetting, osi-modellen, tcp-ip]
relatert:
  - teknologiforstaelse/digital-kommunikasjon
---
# Lokale nettverk — Grunnleggende nettverksforståelse

## 🎯 Hva skal du lære?

Du skal forstå hvordan lokale nettverk er bygget opp, hvordan data sendes mellom enheter, og hvordan du kan konfigurere et nettverk med egne subnett.

---

## 📘 Fagstoff

### Hva er et nettverk?

Et nettverk er to eller flere enheter (PC-er, servere, printere, mobiler) som er koblet sammen slik at de kan kommunisere og dele ressurser.

### Nettverkskomponenter

- **Ruter:** Kobler sammen ulike nettverk og sender data mellom dem
- **Svitsj (switch):** Kobler sammen enheter innenfor samme nettverk
- **Aksesspunkt (AP):** Gir trådløs tilkobling (WiFi)
- **Nettverkskabel (Ethernet):** Fysisk forbindelse mellom enheter
- **Nettverkskort (NIC):** Hardware i enheten som kobler til nettverket

### OSI-modellen (7 lag)

OSI-modellen beskriver hvordan data sendes over et nettverk i 7 lag:

| Lag | Navn | Funksjon | Eksempel |
|-----|------|----------|----------|
| 7 | Applikasjon | Brukerens grensesnitt | HTTP, SMTP |
| 6 | Presentasjon | Datakoding, kryptering | SSL/TLS |
| 5 | Sesjon | Holder orden på samtaler | NetBIOS |
| 4 | Transport | Sikker levering | TCP, UDP |
| 3 | Nettverk | Ruting av pakker | IP |
| 2 | Datalink | Overføring på mediet | Ethernet, WiFi |
| 1 | Fysisk | Kabler, signaler | Kategori 5e/6 |

**Huskeregel:** Alle (7) Produsenter (6) Skal (5) Til (4) Nye (3) Datamaskiner (2) Først (1)

### TCP/IP-modellen (4 lag)

Den forenklede modellen som internett faktisk bruker:
1. **Nettverkstilgang** (fysisk + datalink)
2. **Internett** (nettverk) — IP-adressering og ruting
3. **Transport** — TCP (sikker) eller UDP (rask)
4. **Applikasjon** — HTTP, DNS, SMTP

### IP-adressering

- **IPv4:** 192.168.1.1 — 32 bits, 4 oktetter (ca. 4,3 milliarder adresser)
- **IPv6:** 2001:db8::1 — 128 bits, løser adressemangel
- **Subnettmaske:** Angir hvor mange enheter som kan være i nettverket (255.255.255.0 = 254 enheter)
- **DHCP:** Tildeler automatisk IP-adresser til enheter

### Subnetting — dele opp nettverk

Subnetting handler om å dele et større nettverk inn i mindre subnett for bedre organisering og sikkerhet.

**Eksempel:** Et nettverk med adresser 192.168.1.0/24 kan deles i:
- 192.168.1.0/25 — 126 enheter (administrasjon)
- 192.168.1.128/25 — 126 enheter (elever)

---

## 💡 Praktiske eksempler

**Konfigurere et lokalt nettverk:**
1. Koble en svitsj til ruteren
2. Koble PC-er til svitsjen med Ethernet-kabler
3. Aktiver DHCP på ruteren
4. PC-ene får automatisk IP-adresse fra ruteren
5. Test med `ping` mellom PC-ene

---

## 🔗 Tverrfaglige koblinger

- **Programmering:** Nettverk er nødvendig for webapplikasjoner og API-kall
- **Produksjon:** Streaming og videoproduksjon krever god nettverksforståelse
- **Matematikk:** Binærtall og subnettkalkulering bygger på matematisk forståelse

---

## 📚 Kilder

- NDLA — Teknologiforståelse: Lokale nettverk
- [Nettverk forklart (NDLA)](https://ndla.no/f/teknologiforstaelse-im-ikm-vg1/087c23101fc5)
