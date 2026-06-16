---
title: "Digital kommunikasjon — Internett, DNS og skytjenester"
emne: digital-kommunikasjon
fag: teknologiforstaelse
uke: [38, 39]
kompetansemaal: [tf-09]
kilder:
  - https://ndla.no/f/teknologiforstaelse-im-ikm-vg1/087c23101fc5
tags: [internett, dns, sky, lagring, kommunikasjon]
relatert:
  - teknologiforstaelse/lokale-nettverk
---
# Digital kommunikasjon — Internett, DNS og skytjenester

## 🎯 Hva skal du lære?

Du skal forstå hvordan internett fungerer — fra URL til nettside — og hvordan data blir kommunisert og lagret på tvers av nettverk.

---

## 📘 Fagstoff

### Hvordan internett fungerer

Internett er et globalt nettverk av datamaskiner som snakker sammen ved hjelp av felles protokoller (TCP/IP). Når du skriver en URL i nettleseren, skjer dette:

1. **DNS-oppslag:** Nettleseren spør en DNS-server hvor nettsiden "finnes" (IP-adressen)
2. **TCP-tilkobling:** Nettleseren kobler seg til serveren via TCP
3. **HTTP-forespørsel:** Nettleseren ber om nettsiden (GET /index.html)
4. **Serverens svar:** Serveren sender HTML, CSS og JavaScript
5. **Rendering:** Nettleseren tegner opp nettsiden på skjermen

### DNS (Domain Name System)

DNS er "telefonkatalogen" på internett:
- Oversetter domenenavn (f.eks. `ndla.no`) til IP-adresser (`195.1.1.1`)
- Hierarkisk struktur: rot → toppdomene (.no, .com) → domenet → subdomene
- Uten DNS måtte vi husket IP-adresser på alle nettsider

### Skytjenester (Cloud Computing)

Skytjenester betyr at data og programmer ligger på servere på internett, ikke lokalt på din maskin:

- **IaaS (Infrastructure as a Service):** Virtuelle servere og lagring (f.eks. Google Cloud)
- **PaaS (Platform as a Service):** Plattform for utvikling (f.eks. Vercel, Netlify)
- **SaaS (Software as a Service):** Programvare via nettleser (f.eks. Google Docs, Office 365)

**Fordeler:** Tilgjengelig fra alle enheter, automatisk oppdatering, skalerbart
**Ulemper:** Avhengig av internett, personvernhensyn, kostnad over tid

### Kommunikasjonsprotokoller

- **HTTP/HTTPS:** Overfører nettsider (HTTPS = kryptert)
- **SMTP:** Sender e-post
- **FTP:** Overfører filer
- **WebSocket:** Sanntids toveiskommunikasjon

---

## 💡 Praktiske eksempler

**Finn IP-adressen til en nettside:**
```bash
nslookup ndla.no
# Svar: Server: 195.1.1.1
```

**Spor ruten til en server:**
```bash
traceroute google.com
# Viser alle rutere dataen passerer gjennom
```

---

## 🔗 Tverrfaglige koblinger

- **Konseptutvikling og programmering:** Webutvikling krever forståelse av HTTP, DNS og skytjenester
- **Produksjon og historiefortelling:** Distribusjon av medieinnhold på nettet

---

## 📚 Kilder

- NDLA — Digital kommunikasjon
- [How DNS Works (Cloudflare)](https://www.cloudflare.com/learning/dns/what-is-dns/)
- [Internett forklart (NDLA)](https://ndla.no/f/teknologiforstaelse-im-ikm-vg1/087c23101fc5)
