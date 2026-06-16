---
title: "Database — Modellering, SQL og datalagring"
emne: database
fag: konseptutvikling-programmering
uke: [15, 16]
kompetansemaal: [kp-04]
kilder:
  - https://ndla.no/f/konseptutvikling-og-programmering-im-ikm-vg1/7bc23d06d79d
tags: [database, sql, modellering, databaser, normalisering]
relatert:
  - konseptutvikling-programmering/programmering
  - teknologiforstaelse/digital-kommunikasjon
---
# Database — Modellering, SQL og datalagring

## 🎯 Hva skal du lære?

Du skal utforske og anvende verktøy for datamodellering i oppbygging av databaser.

---

## 📘 Fagstoff

### Hva er en database?

En database er en strukturert samling av data som er lagret slik at den enkelt kan søkes i, oppdateres og administreres. Tenk på det som et digitalt arkivskap.

### Databasetyper

- **Relasjonsdatabaser:** Data lagres i tabeller med rader og kolonner (SQL)
- **NoSQL-databaser:** Fleksibel lagring, ingen faste tabeller (MongoDB)

### Datamodellering

Før du bygger en database må du planlegge strukturen:

**1. Identifiser entiteter:** Hva skal lagres? (Elev, Fag, Karakter)
**2. Identifiser attributter:** Egenskaper ved entitetene (navn, alder, klasse)
**3. Identifiser relasjoner:** Hvordan henger entitetene sammen?

**ER-diagram (Entity-Relationship):**
```
[Elev] ──tar──> [Fag]
  │               │
  └────har──────> [Karakter]
```

### SQL-grunnleggende

SQL (Structured Query Language) brukes til å snakke med databaser:

```sql
-- Opprett tabell
CREATE TABLE Elev (
  id INTEGER PRIMARY KEY,
  navn TEXT,
  klasse TEXT
);

-- Sett inn data
INSERT INTO Elev VALUES (1, 'Ola Nordmann', 'VG1 IM');

-- Hent data
SELECT * FROM Elev WHERE klasse = 'VG1 IM';

-- Oppdater data
UPDATE Elev SET navn = 'Kari Nordmann' WHERE id = 1;

-- Slett data
DELETE FROM Elev WHERE id = 1;
```

### Normalisering

Normalisering handler om å strukturere data for å unngå duplikater:
- **1. normalform:** Hver kolonne inneholder én verdi
- **2. normalform:** Alle kolonner er avhengig av hele primærnøkkelen
- **3. normalform:** Ingen kolonner er avhengige av andre kolonner som ikke er nøkler

---

## 💡 Praktiske eksempler

**Design en database for en skole:**
- Elev: id, navn, epost, klasse_id
- Klasse: id, navn, trinn
- Fag: id, navn, lærer_id
- Karakter: elev_id, fag_id, karakter, dato

---

## 🔗 Tverrfaglige koblinger

- **Programmering:** Koble database til applikasjon
- **Teknologiforståelse:** Hvordan data lagres på servere

---

## 📚 Kilder

- NDLA — Database
- [SQL Tutorial (W3Schools)](https://www.w3schools.com/sql/)
