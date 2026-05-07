
Spodaj je celovit, tehnično korekten povzetek — strukturiran kot “inženirski zapis postopka”, ne kot intuitivna razlaga.

---

# 📘 Problem

Želiš uporabiti pisavo **ISOCPEUR** tako, da bo:

* **dejanska višina črk (npr. M)** = 3.5 mm (ali 5 mm, 2.5 mm …)
* skladno z **ISO 3098** (tehnične risbe)

---

# ⚠️ Ključna začetna zmota

Velikost pisave (pt ali mm v UI) **NE pomeni dejanske višine črk**, ker:

> font size = višina **em-square**, ne višina črk

---

# 🔍 Korak 1: Analiza fonta (TTF datoteka)

Iz datoteke `isocpeur.ttf`:

* unitsPerEm = **2048**
* višina črke M = **1320 units**
* baseline = **y = 0**
* M: od **0 do 1320**

---

# 📐 Korak 2: Izračun ključnega razmerja

[
\text{cap/em} = \frac{1320}{2048} = 0.64453125
]

👉 to je **najpomembnejši rezultat**

Pomen:

> črke zasedejo ~64.45 % em prostora

---

# 🧠 Interpretacija

TTF ISOCPEUR:

* ima tipografski model (em, ascender, descender)
* **ni “čista ISO geometrija”**
* vsebuje dodatni prostor (predvsem descender)

---

# 🔁 Korak 3: Inverzni problem

Želiš:
[
h = \text{dejanska višina črk}
]

ampak nastavljaš:
[
\text{font size} = ?
]

---

# 🧮 Rešitev

[
\text{font size} = \frac{h}{0.64453125}
]

---

# ✅ Primer (3.5 mm)

[
\frac{3.5}{0.64453125} = 5.430651872 \text{ mm}
]

👉 zato si dobil:

> **5.430652 mm (točno pravilno)**

---

# 🔍 Korak 4: Validacija

Eksperimentalno:

* povečal si font
* izmeril višino M
* dobil isti rezultat

👉 to potrdi:

> matematični model = realni rendering

---

# 📏 Korak 5: Razmik vrstic

Iz font metrike:

[
\text{line height} = 1320 - (-396) = 1716
]

[
\frac{1716}{2048} = 0.8379
]

[
\text{line spacing} = \text{font size} \times 0.8379
]

Primer:

* za 3.5 mm → **4.55 mm**

---

# ⚠️ Razlika do ISO standarda

ISO priporoča:

[
\text{line spacing} \approx 1.4h
]

Font daje:

[
\approx 1.3h
]

👉 torej:

* rahlo bolj “zbit” zapis

---

# 📊 Končni model (generaliziran)

Za ISOCPEUR (ta konkretna TTF verzija):

## konstante:

```text
unitsPerEm = 2048
capHeight = 1320
k = 0.64453125
lineFactor = 0.8379
```

---

## formule:

### višina pisave:

[
\text{font size} = \frac{h}{k}
]

### razmik vrstic:

[
\text{line spacing} = \text{font size} \times 0.8379
]

---

# 🎯 Ključne ugotovitve

### 1. pt enote niso uporabne

* temeljijo na em-square
* ignorirajo dejansko geometrijo črk

---

### 2. ISOCPEUR (TTF) ≠ ISO font

* ima tipografski overhead
* zato:

  * cap height < em
  * potrebuje korekcijo

---

### 3. edini pravilen pristop

> vedno kalibriraš glede na **dejansko višino črk**

---

### 4. tvoj rezultat

> **5.430652 mm ni približek — je eksaktna rešitev**

---

# 🧩 Intuitivni povzetek

* font ima “okvir” (em)
* črke zasedejo samo ~64 %
* zato moraš okvir povečati, da črke dosežejo pravo višino

---

# 🏁 Bottom line

Če uporabljaš **ISOCPEUR TTF**:

> velikost pisave ≠ višina črk
> → vedno uporabi faktor **0.64453125**

---

Če želiš nadaljevati, lahko:

* primerjava s **SHX (ISOCP)** kjer je logika čisto drugačna
* ali naredim **orodje / kalkulator**, da ti to avtomatsko računa
