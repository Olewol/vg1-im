---
title: "Programmering — Introduksjon til koding"
emne: programmering
fag: konseptutvikling-programmering
uke: [2, 3]
kompetansemaal: [kp-03, kp-08, kp-07]
kilder:
  - https://ndla.no/f/konseptutvikling-og-programmering-im-ikm-vg1/7bc23d06d79d
tags: [programmering, python, javascript, koding, algoritmer]
relatert:
  - konseptutvikling-programmering/webutvikling
  - konseptutvikling-programmering/database
---
# Programmering — Introduksjon til koding

## 🎯 Hva skal du lære?

Du skal bruke programmering til å løse praktiske utfordringer og fortelle interaktive historier, samt beskrive hvordan teknologi behandler data, algoritmer og statistikk.

---

## 📘 Fagstoff

### Hva er programmering?

Programmering handler om å gi instruksjoner til en datamaskin. Du skriver kode i et programmeringsspråk, og datamaskinen utfører instruksjonene.

### Algoritmer

En **algoritme** er en oppskrift for å løse et problem — steg for steg.

**Eksempel — Algoritme for å steke pannekaker:**
1. Bland mel, egg, melk og salt
2. Varm opp stekepannen
3. Hell i røre
4. Stek i 2 minutter på hver side
5. Server

### Programmeringsspråk på VG1 IM

**Python:**
- Lettlest og nybegynnervennlig
- Mye brukt i IT-bransjen
- Eksempel: `print("Hello, world!")`

**JavaScript:**
- Brukes i webapplikasjoner
- Kjører i nettleseren
- Eksempel: `console.log("Hello, world!")`

### Grunnleggende konsepter

**Variabler:** Lagrer data
```python
navn = "Ola"
alder = 17
```

**Datatyper:** Tall, tekst (string), sann/usann (boolean), lister (array)

**Betingelser (if/else):**
```python
if alder >= 18:
    print("Du er myndig")
else:
    print("Du er ikke myndig")
```

**Løkker:** Gjenta kode
```python
for i in range(5):
    print("Hei verden!")
```

**Funksjoner:** Gjenbrukbar kode
```python
def hilsen(navn):
    return f"Hei {navn}!"

print(hilsen("Ola"))
```

### Hvordan datamaskinen behandler kode

1. **Kildekode:** Teksten du skriver
2. **Kompilering/tolkning:** Omgjøres til maskinkode
3. **CPU:** Utfører instruksjonene
4. **Minne (RAM):** Lagrer data under kjøring

---

## 💡 Praktiske eksempler

**Lag en enkel kalkulator i Python:**
```python
tall1 = float(input("Skriv inn første tall: "))
tall2 = float(input("Skriv inn andre tall: "))
print(f"Sum: {tall1 + tall2}")
print(f"Differanse: {tall1 - tall2}")
```

**Betinget historie i Twine:** Lag en interaktiv fortelling der leseren velger hva som skal skje.

---

## 🔗 Tverrfaglige koblinger

- **Produksjon:** Interaktive historier, spillutvikling
- **Teknologiforståelse:** Hvordan hardware kjører koden

---

## 📚 Kilder

- NDLA — Konseptutvikling og programmering: Programmering
- [Python for beginners](https://www.python.org/about/gettingstarted/)
