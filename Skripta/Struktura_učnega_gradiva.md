STRUKTURA UČNEGA GRADIVA
================================================================================

## Struktura izvedbe predmeta in struktura učnega gradiva

Rad bi tako strukturo, da bi bila:

```
- Teoretični del s primeri in
- praktične vaje z nalogami
```

dve ločeni datoteki. Ta učni proces bo namreč izveden tako, da imajo študentje vsak teden po 2 uri predavanj in 2 uri vaj. Če bi bili datoteki ločeni, bi lahko predavatelj in asistent lahko oblikovala vsak svoj del učnega gradiva, s primernim skriptom pa bi jih lahko enostavni združili in s pandoc programom preoblikovali v končno skripto.

## Poimenovanje datotek

Poimenovanja datotek naj bodo definirana v naslednji strukturi:

```
- [zaporedna številka učnega sklopa].[zaporedna številka učne enote]_T_[Skajšan_naslov_učne_enote].md - tako ime dokumenta naj bo za predavanja oziroma za torijo s primeri
- [zaporedna številka učnega sklopa].[zaporedna številka učne enote]_V_[Skajšan_naslov_učne_enote].md - tako ime dokumenta naj bo za vaje z nalogami in izzivi.
```

Na primer:

```
1.1_T_Modeliranje_s_FreeCADom.md in
1.1_V_Modeliranje_s_FreeCADom.md
```

Za tema dvema dokumentoma lahko sledi nova učna enota ali pa celo nov učni sklop. Organizacija in struktura dokumentov pa naj ostane enaka.

## Struktura vsebine dokumentov

V primeru, da gre za dokument z opisom učnega sklopa, naj le ta vsebuje nekakšen povzetek vseh vključenih učnih enot. Na primer:

```
# Uvod v modeliranje s FreeCAD programom

Sledi opis vsebine, ki se nahaja v tem učnem sklopu. Na primer: Modeliranje je zelo pomemben del inženirskega načrtovanja. Omogoča nam ... V tem sklpu obravavamo izhodiščne pojme modeliranja in predstavljamo osnovni proces modeliranja ...
```

Temu dokumentu ne sledi nobena vaja. Dokumenti se nadaljujejo z naslednjo učno enoto. Najprej naj bo na nivo 2 postavljena teorija, ki jo bodo študentje spoznali pri predavanjih. Na primer:

```
## Naslov učne enote

V tem delu naj bodo razložene teoretične osnove. Na primer: Tehniška dokumentacija je skupek risb, zapisov in podatkov, ki opisujejo tehnično rešitev. Vsi na novo uvedeni pojmi naj bodo predstavljeni in razloženi.

**Pojmi**:
- *Tehniška risba*: grafični prikaz izdelka.
- *Kosovnica (BOM)*: seznam delov.

**Relevantni standardi**:
- SIST ISO 128 – pravila tehničnega risanja
- ISO 7200 – podatkovna polja

### Teoretične osnove naj bodo podkrepljeni s primeri

- Pojasnilo na primeru iz prakse, opisan postopek in tehnika dela,
- Sheme / slike
- Primerjava pravilno / nepravilno
```

Na to naj sledi še dokument za izvedbo vaj. Naslov vsake vaje naj se začne na nivoju 3. Naloge naj si sledijo od preprostejših k bolj zahtevnim. Na Primer takole:

```

### Naloga: Pravokotnik, centriran na izhodišče

1. Ustvari novo telo in vstavi skico na ravnino XY.
2. Nariši pravokotnik.
3. Uporabi geometrijske vezave, da ga centrirano poravnaš glede na točko (0,0).
4. Določi višino in širino z dimenzijskimi omejitvami (npr. 40 mm × 30 mm).
5. Preveri, ali je skica popolnoma definirana (zelene črte).
6. Shrani kot `pravokotnik.FCStd`.

### Naloga: Krog s koncentričnostjo

1. Nariši dva kroga, enega znotraj drugega.
2. Uporabi vezavo koncentričnosti.
3. Določi premer manjšega kroga (npr. 10 mm).
4. Določi razliko med radijema (z dodatnim krogom ali kot med osjo).
5. Shrani kot `koncentricni_kroga.FCStd`.

### Izziv: Trikotnik z določeno višino

1. Nariši trikotnik iz treh črt.
2. Določi osnovno stranico in višino.
3. Poskrbi, da je trikotnik zrcalno simetričen glede na os Y.
4. Uporabi vse potrebne vezave za popolno definicijo.

#### Preizkusi svoje znanje:

- Kako ugotoviš, da je element še vedno prost?
- Katere vezave so bile potrebne za centriranje pravokotnika?
- Kaj se zgodi, če dodaš preveč vezav?

#### Oddaja naloge

- Format: `.FCStd`
- Imena datotek: `ime_priimek_skica1.FCStd`, `ime_priimek_skica2.FCStd` …
- Oddaja: v spletno učilnico ali po e-pošti

#### Refleksija
- Kaj ti je bilo najtežje?
- Kaj si danes prvič slišal?

```
S tako strukturo naj bo pripravljeno učno gradivo za vsako učno enoto posebej.
