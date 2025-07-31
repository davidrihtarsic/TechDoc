# Uvod v modeliranje s programom FreeCAD

Modeliranje je temeljni del sodobnega inženirskega oblikovanja in načrtovanja. Omogoča natančno predstavo o končnem izdelku še pred fizično izdelavo ter omogoča hitrejše in učinkovitejše iteracije pri razvoju. V tem učnem sklopu se bomo spoznali z osnovami parametričnega 3D-modeliranja s pomočjo odprtokodnega programa **FreeCAD**, ki je posebej primeren za izobraževalno rabo.

**Vsebina sklopa**

Ta učni sklop vsebuje naslednje učne enote:

- **1.1 Namestitev, osnovna nastavitev in delovna okolja**  
  Spoznali bomo, kako se FreeCAD namesti, kako prilagodimo osnovne nastavitve in kakšna so glavna delovna okolja (Sketcher, Part Design).

- **1.2 Geometrijske omejitve in parametrično načrtovanje**  
  Poudarek bo na razumevanju dimenzijskih in geometrijskih omejitev ter osnovah parametričnega modeliranja.

- **1.3 Napredna orodja modeliranja**  
  Predstavili bomo naprednejše funkcije, kot so Loft, Mirror, Pattern, Boolean operacije in Shape Binder.

- **1.4 Modeliranje enostavnih sestavljenih modelov**  
  V tej enoti bomo vstopili v svet sestavljanja modelov iz več delov z uporabo ustreznih delovnih okolij.

- **1.5 Pomožne ravnine in delo v prostoru**  
  Naučili se bomo uporabljati datum ravnine, lokalne koordinate in usmerjene skice za kompleksnejše 3D-modeliranje.

Vsaka enota vsebuje ločen teoretični del s primeri ter praktične vaje z nalogami in izzivi.

## Namestitev, osnovna nastavitev in delovna okolja

Za uspešno delo s programom FreeCAD je ključno, da ga pravilno namestimo, razumemo osnovne nastavitve in se seznanimo z najpomembnejšimi delovnimi okolji.

### Namestitev FreeCAD

Program FreeCAD je odprtokodna programska oprema, ki jo lahko prenesemo s spletne strani: [https://www.freecad.org/](https://www.freecad.org/)

Na voljo je za različne operacijske sisteme (Windows, macOS, Linux).

#### Koraki namestitve (primer za Windows):
1. Obišči spletno stran in prenesi namestitveno datoteko.
2. Zaženi namestitveni program.
3. Sledi navodilom čarovnika in zaključi namestitev.

### Osnovna nastavitev

Po prvem zagonu lahko prilagodimo osnovne nastavitve:

- Izberemo privzeto delovno okolje (npr. *Part Design*),
- Nastavimo enote (npr. milimetre),
- Prilagodimo videz (teme, ikone, mreža).

To storimo v meniju **Edit > Preferences**.

### Delovna okolja

FreeCAD omogoča delo v več specializiranih okoljih. Najpomembnejša za začetno modeliranje sta:

- **Sketcher** – omogoča ustvarjanje 2D skic z omejitvami.
- **Part Design** – omogoča izdelavo 3D modelov iz skic z uporabo funkcij (extrude, pad, pocket itd.).

Druga uporabna okolja (kasneje):

- **Part** – delo z osnovnimi telesi (primitives),
- **Assembly (A2+, A4)** – za sestavljanje več delov,
- **TechDraw** – za izdelavo tehničnih risb.

### Primer iz prakse

Po uspešni namestitvi programa se ustvari nova prazna datoteka, v kateri se raziskujejo možnosti v meniju Preferences in prilagajajo osnovne nastavitve (npr. enote, mreža, barve).

**Pravilno:** nastavitev milimetrov, izbira privzetega okolja Part Design.

**Nepravilno:** izbira napačnih enot (palci), ignoriranje nastavitev mreže (snap to grid).

### Naloga: Prvi zagon in nastavitev programa

1. Prenesi in namesti FreeCAD (če še ni nameščen).
2. Zaženi program.
3. V meniju **Edit > Preferences** nastavi:
   - Enote: milimetri (mm),
   - Privzeto delovno okolje: Part Design,
   - Omogoči prikaz mreže.
4. Shrani novo prazno datoteko kot `ime_priimek_uvod.FCStd`.

### Naloga: Ustvari osnovni 3D-model

1. Ustvari novo telo (*Body*).
2. Vstavi novo skico (*Sketch*) na ravnino XY.
3. Nariši pravokotnik s pomočjo orodja za črte.
4. Poravnaj središče pravokotnika na točko (0,0) s pomočjo geometrijskih vezav.
5. Nastavi širino (40 mm) in višino (30 mm).
6. Uporabi funkcijo *Pad* in določi višino 20 mm.
7. Preveri, da je telo pravilno ustvarjeno.
8. Shrani kot `ime_priimek_model1.FCStd`.

### Izziv: Uporaba funkcije Pocket

1. Odpri obstoječi model `model1`.
2. Na zgornji ploskvi modela ustvari novo skico.
3. Nariši krog premera 10 mm na sredini pravokotnika.
4. Uporabi funkcijo *Pocket* za ustvarjanje luknje skozi celotno telo.
5. Shrani kot `ime_priimek_model2.FCStd`.

### Izziv: Raziskovanje uporabniškega vmesnika

1. Ugotovi funkcijo zavihkov: Model, Tasks, Combo View.
2. Preklopi med delovnimi okolji Sketcher, Part Design, TechDraw.
3. Preveri, kako se v Model pogledu prikažejo elementi kot so Body, Sketch, Pad, Pocket.
4. Nariši shemo strukture preprostega modela (Body → Sketch → Pad → Sketch → Pocket).

#### Preizkusi svoje znanje
- Kaj pomeni, da je skica popolnoma definirana?
- Kako se razlikujeta funkciji *Pad* in *Pocket*?
- Kaj se zgodi, če ne ustvariš telesa (*Body*) pred risanjem skice?

#### Oddaja naloge
- Format: `.FCStd`
- Imena datotek: `ime_priimek_uvod.FCStd`, `ime_priimek_model1.FCStd`, `ime_priimek_model2.FCStd`
- Oddaja: v spletno učilnico ali po e-pošti

#### Refleksija
- Kaj ti je bilo najlažje?
- Kaj si danes prvič spoznal?
- Katera funkcija ti je bila najbolj zanimiva?

## Geometrijske omejitve in parametrično načrtovanje

Parametrično načrtovanje omogoča, da so vsi elementi modela definirani z dimenzijami, vezavami in odvisnostmi, ki jih lahko kadarkoli spremenimo. S tem postane model prilagodljiv in enostaven za posodabljanje. Geometrijske in dimenzijske omejitve igrajo pri tem ključno vlogo.

### Geometrijske omejitve

Geometrijske omejitve določajo relacije med elementi skice:

- **Horizontalna/vertikalna** – element je poravnan glede na koordinatni sistem.
- **Paralelnost, pravokotnost** – odnos med črtami.
- **Tangenta** – krožnica se dotika črte.
- **Koncentričnost** – dve krožnici imata isto središče.
- **Simetričnost** – elementi so simetrični glede na os.

### Dimenzijske omejitve (kotiranje)

Dimenzijske omejitve določajo velikost in položaj elementov:

- Dolžina črte
- Polmer/premer kroga
- Kot med črtami
- Oddaljenost med točkami ali črtami

### Parametričnost modela

Parametričnost pomeni, da model temelji na spremenljivkah. Sprememba ene vrednosti lahko vpliva na celoten model:

- Možnost ustvarjanja "nastavljivih" modelov
- Uporaba formul in spremenljivk v kotiranju
- Primer: objemka, kjer lahko s spreminjanjem premera prilagajamo celoten model

### Primer iz prakse: parametrična ploščica

Model vsebuje odprtino, katere premer določimo s parametrom. Položaj odprtine in robov se samodejno prilagodi ob spremembi.

**Pravilno:** vse skice so popolnoma definirane (zelene črte), uporaba formul.

**Nepravilno:** prekrivajoče omejitve, nedoločeni elementi (modre črte), manjkajoče relacije med elementi.

### Vizualne značilnosti

- Zelene črte: popolnoma definirano
- Modre črte: delno definirano
- Rdeče: preveč omejitev (over-constrained)

Parametrično modeliranje omogoča ustvarjanje fleksibilnih rešitev, ki se jih lahko hitro prilagodi novim zahtevam.

### Naloga: Pravokotnik z omejitvami

1. Ustvari novo telo (*Body*) in vstavi novo skico (*Sketch*) na ravnino XY.
2. Nariši pravokotnik s pomočjo črt.
3. Dodaj naslednje geometrijske omejitve:
   - Vzporednost nasprotnih stranic,
   - Pravokotnost,
   - Simetričnost glede na os Y.
4. Dodaj dimenziji višine (30 mm) in širine (50 mm).
5. Preveri, ali so vse črte zelene (popolnoma definirano).
6. Shrani kot `ime_priimek_pravokotnik.FCStd`.

### Naloga: Krog z vezavo koncentričnosti

1. Na isti skici nariši dva kroga – enega znotraj drugega.
2. Uporabi vezavo *Concentricity*.
3. Določi premer notranjega kroga (npr. 10 mm).
4. Določi razliko med radijema z dodatno dimenzijsko vezavo.
5. Preveri definiranost skice.
6. Shrani kot `ime_priimek_kroga.FCStd`.

### Izziv: Nastavljiva objemka

1. Ustvari skico prereza objemke, sestavljeno iz loka in dveh črt.
2. Vključi spremenljivko "premer" z uporabo formule (npr. `Diameter = 25 mm`).
3. Poveži dimenzije loka in širine objemke s formulo.
4. Preveri, ali model deluje pri različnih vrednostih premera (20 mm, 30 mm).
5. Shrani kot `ime_priimek_objemka.FCStd`.

#### Preizkusi svoje znanje:
- Kaj pomeni, da je skica "over-constrained"?
- Kako vključiš spremenljivke v dimenzije?
- Zakaj je pomembno, da so vse skice popolnoma definirane?

#### Oddaja naloge
- Format: `.FCStd`
- Imena datotek: `ime_priimek_pravokotnik.FCStd`, `ime_priimek_kroga.FCStd`, `ime_priimek_objemka.FCStd`
- Oddaja: v spletno učilnico ali po e-pošti

#### Refleksija
- Kako ti je uspelo uporabiti geometrijske vezave?
- Kaj je bilo najtežje pri parametričnem modeliranju?
- Kako si rešil napako pri preveč omejitvah?

## Napredna orodja modeliranja

Ko obvladamo osnovne funkcije skiciranja in osnovnega modeliranja, lahko začnemo uporabljati naprednejša orodja za kompleksnejše 3D-oblike. Ta orodja omogočajo večjo fleksibilnost in širše možnosti oblikovanja.

### Loft (prelivanje oblik)

Funkcija *Loft* omogoča povezovanje dveh ali več skic v različnih ravninah v zvezno 3D obliko.

- Zahteva najmanj dve skici,
- Skici morata biti odprti ali zaprti profili,
- Uporabno za ustvarjanje kompleksnih prehodov med oblikami.

### Mirror (zrcaljenje)

- Uporablja se za simetrične modele,
- Zrcali izbrane elemente okoli določene ravnine,
- Uporabno za zmanjšanje števila operacij v modelu.

### Pattern (ponavljanje elementov)

- Linearni in krožni vzorec (*Linear Pattern*, *Polar Pattern*),
- Uporablja se za ustvarjanje ponovitev (npr. luknje na krogu),
- Možnost spreminjanja števila ponovitev, razmika, kota.

### Boolean operacije

- Združevanje (Union), odvzemanje (Cut), presek (Intersection),
- Uporabne pri kombiniranju več teles v *Part* okolju,
- Manj priporočljivo za *Part Design*, kjer naj bodo modeli parametrični.

### Shape Binder

- Orodje za prenos geometrije med telesi,
- Omogoča uporabo referenc iz drugega telesa v trenutnem modelu,
- Pomembno pri sestavljenih modelih.

### Primeri uporabe

- *Loft* za ustvarjanje ročaja ali držala z organsko obliko,
- *Mirror* za zrcalno simetrična ohišja,
- *Pattern* za ponavljajoče se izvrtine,
- *Shape Binder* za prenos osnov iz drugega modula.

**Pravilno:** uporaba referenc (Shape Binder), delovanje znotraj enega telesa, smiselna uporaba simetrije.

**Nepravilno:** ročno podvajanje skic, manjkajoča vezava na osnovne skice, nepregleden model.

### Naloga: Uporaba funkcije Loft

1. Ustvari dve skici: eno na ravnini XY in drugo na paralelni datum ravnini nad njo.
2. Prva skica: krog premera 20 mm.
3. Druga skica: kvadrat stranice 30 mm.
4. Uporabi funkcijo *Loft* za ustvarjanje prehoda.
5. Shrani kot `ime_priimek_loft.FCStd`.

### Naloga: Zrcaljenje (Mirror)

1. Nariši polovico simetričnega profila (npr. nosilec).
2. Uporabi funkcijo *Mirror* za zrcaljenje okoli sredinske ravnine.
3. Preveri, ali je model simetričen.
4. Shrani kot `ime_priimek_mirror.FCStd`.

### Naloga: Krožni vzorec (Polar Pattern)

1. Ustvari osnovno telo (cilinder).
2. Na zgornji ploskvi dodaj luknjo z *Pocket* funkcijo.
3. Uporabi *Polar Pattern* za ponovitev luknje 6-krat v krogu.
4. Shrani kot `ime_priimek_pattern.FCStd`.

### Izziv: Kombinacija orodij

1. Ustvari obliko z uporabo *Loft* in *Mirror*.
2. Dodaj luknje z *Pattern* funkcijo.
3. Uporabi *Shape Binder* za povezavo z drugim telesom.
4. Shrani kot `ime_priimek_izziv.FCStd`.

#### Preizkusi svoje znanje
- Kaj je razlika med Linear in Polar Pattern?
- Kako deluje Shape Binder?
- Zakaj so Loft operacije uporabne?

#### Oddaja naloge
- Format: `.FCStd`
- Imena datotek: `ime_priimek_loft.FCStd`, `ime_priimek_mirror.FCStd`, `ime_priimek_pattern.FCStd`, `ime_priimek_izziv.FCStd`
- Oddaja: v spletno učilnico ali po e-pošti

#### Refleksija
- Katero orodje ti je bilo najzanimivejše?
- Kako si združil več naprednih funkcij v enem modelu?
- Kje si imel največ težav?

## Modeliranje enostavnih sestavljenih modelov

Modeli v realnem svetu pogosto niso sestavljeni iz enega samega kosa, temveč iz več komponent, ki jih je treba združiti v logično celoto. Sestavljanje modelov v FreeCAD-u poteka s pomočjo t.i. *Assembly* okolij.

### Osnovni pojmi sestavljanja

- **Komponenta**: posamezni del (kos), ki ga sestavimo v večjo celoto.
- **Sestav (Assembly)**: združba več komponent, ki so med seboj povezane s funkcionalnimi relacijami (prileganje, poravnava).
- **Povezave (Constraints)**: določajo prostorski odnos med posameznimi komponentami (npr. poravnava osi, stik ploskev).

### Pristopi k sestavljanju

- **Znotraj enega dokumenta** (več Body elementov): preprosto modeliranje brez uporabe specializiranega okolja.
- **Z ločenimi dokumenti in Assembly Workbenches**: bolj napredno sestavljanje s komponentami, uvoženimi iz različnih datotek.

### Assembly Workbenches

V FreeCAD-u obstaja več dodatkov za sestavljanje:

- **A2+** – enostaven in zelo razširjen dodatek za sestavljanje modelov.
- **Assembly 4** – naprednejši modul s parametrično vezavo in referencami.

### Primer uporabe povezav

- Poravnava dveh osi,
- Stik med dvema ploskvama,
- Fiksacija ene komponente in usklajevanje ostalih.

### Priporočila za delo

- Komponente naj bodo modelirane posamezno in shranjene kot ločene datoteke,
- Uporabljaj skupne referenčne točke za lažje poravnavanje,
- Pred sestavljanjem preveri, da so posamezne komponente popolnoma definirane.

**Pravilno:** uporaba vezav (constraints) za sestavljanje, orientacija na referenčne točke.

**Nepravilno:** ročno premikanje komponent brez povezav, manjkajoče relacije med deli, slaba organizacija datotek.

### Naloga: Modeliranje dveh ločenih komponent

1. Ustvari prvi del (osnovna plošča) z dimenzijami 100 mm × 50 mm × 10 mm.
2. Ustvari drugi del (valj) z višino 30 mm in premerom 20 mm.
3. Shrani vsako komponento kot ločeno datoteko: `ime_priimek_plosca.FCStd` in `ime_priimek_valj.FCStd`.

### Naloga: Sestavljanje z A2+ Workbench

1. Namesti dodatek A2+ (če še ni nameščen).
2. Ustvari nov sestavni dokument.
3. Uvozi obe komponenti (ploščo in valj).
4. Postavi valj na ploščo z naslednjimi vezavami:
   - Os valja poravnana s središčem plošče,
   - Osnovni ploskvi v stiku.
5. Shrani kot `ime_priimek_sestav.FCStd`.

### Izziv: Uporaba dodatnih komponent

1. Ustvari tretjo komponento (pokrov), ki se prilega valju.
2. Dodaj jo v sestav in poveži s pravilnimi vezavami (npr. osno poravnana, v stiku).
3. Preveri, ali se sestav pravilno odziva na spremembe dimenzij.
4. Shrani kot `ime_priimek_sestav_izziv.FCStd`.

#### Preizkusi svoje znanje
- Katere vrste vezav omogoča A2+?
- Kako uvoziš komponente iz ločenih datotek?
- Zakaj je pomembna popolna definiranost komponent pred sestavljanjem?

#### Oddaja naloge
- Format: `.FCStd`
- Imena datotek: `ime_priimek_plosca.FCStd`, `ime_priimek_valj.FCStd`, `ime_priimek_sestav.FCStd`, `ime_priimek_sestav_izziv.FCStd`
- Oddaja: v spletno učilnico ali po e-pošti

#### Refleksija
- Kako si določil referenčne točke za poravnavo?
- Katere napake so se pojavile pri sestavljanju?
- Kako bi organiziral sestavne dokumente pri večjem projektu?

## Pomožne ravnine in delo v prostoru

Pri kompleksnejših modelih osnovne ravnine XY, YZ in XZ pogosto ne zadostujejo. V takih primerih uporabimo pomožne ravnine (Datum Planes), ki jih lahko postavimo poljubno glede na geometrijo modela. Delo v prostoru vključuje tudi uporabo lokalnih koordinatnih sistemov in orientacijo skic v različnih smereh.

### Datum Plane (pomožne ravnine)

- Uporabimo jih za ustvarjanje skic na natančno določenem mestu v prostoru,
- Lahko so vzporedne, pravokotne ali zamaknjene glede na obstoječe ravnine ali ploskve,
- Omogočajo organizirano in logično strukturo kompleksnih modelov.

### Orientacija v prostoru

- Pomembna za modeliranje z več smermi (npr. vrtanje pod kotom),
- Uporaba orodij za rotacijo in premik objektov,
- Določanje referenc glede na obstoječe geometrijske elemente.

### Lokalni koordinatni sistemi

- Določeni s pomočjo *Datum Coordinate System*,
- Uporabni pri sestavljenih modelih in povezovanju različnih komponent,
- Omogočajo neodvisno orientacijo posameznih delov.

### Projekcije skic na ploskve

- Možno je projicirati 2D-skico na ukrivljeno ali rotirano ploskev,
- Uporabno pri naprednih oblikah (npr. gravure, utori),
- Orodje: *Map Sketch to Face*.

### Primeri uporabe

- Skica na 45° ravnini za poševno izvrtino,
- Konstrukcija lukenj na zakrivljenih površinah,
- Ločeno modeliranje podsklopov z lastnimi koordinatnimi sistemi.

**Pravilno:** uporaba Datum Plane za logično ločevanje funkcionalnih sklopov,
orientacija glede na obstoječe elemente.

**Nepravilno:** prekrivanje geometrije, nenatančna pozicija skic, uporaba napačnih referenc.

### Naloga: Skica na pomožni ravnini

1. Ustvari osnovno telo (kocka 40 × 40 × 10 mm).
2. Ustvari novo Datum Plane ravnino 10 mm nad zgornjo ploskvijo.
3. Na njej nariši skico s krogom premera 10 mm.
4. Uporabi *Pocket* za izvrtino navzdol skozi osnovno telo.
5. Shrani kot `ime_priimek_ravnina.FCStd`.

### Naloga: Skica pod kotom

1. Ustvari Datum Plane z nagibom 45° glede na XY ravnino.
2. Uporabi to ravnino za skico – nariši pravokotnik.
3. Uporabi *Pad* za ustvarjanje poševnega izrastka.
4. Shrani kot `ime_priimek_kotni_element.FCStd`.

### Izziv: Lokalni koordinatni sistem

1. Ustvari dva ločena telesa (Body).
2. V vsakem ustvari Datum Coordinate System z različno orientacijo.
3. Uporabi ta sistema za pozicioniranje novih skic.
4. Modeliraj funkcionalni par z ločenima orientacijama.
5. Shrani kot `ime_priimek_izziv_prostor.FCStd`.

#### Preizkusi svoje znanje
- Kako se ustvarja in pozicionira Datum Plane?
- Kdaj uporabiš lokalni koordinatni sistem?
- Kaj pomeni "map sketch to face" in kdaj ga uporabiš?

#### Oddaja naloge
- Format: `.FCStd`
- Imena datotek: `ime_priimek_ravnina.FCStd`, `ime_priimek_kotni_element.FCStd`, `ime_priimek_izziv_prostor.FCStd`
- Oddaja: v spletno učilnico ali po e-pošti

#### Refleksija
- Kako ti je šlo delo v prostoru?
- Ali so ti bila orodja za orientacijo razumljiva?
- Kaj bi uporabil za boljši nadzor nad pozicijami elementov?

# Projekcije

Projekcija je način prikaza tridimenzionalnega objekta na dvodimenzionalni površini, kot je papir ali zaslon. V inženirski praksi je to ključno za natančno komunikacijo oblike, dimenzij in odnosa med deli. V tem učnem sklopu se bomo spoznali z osnovnimi vrstami projekcij, ki se uporabljajo v tehničnem risanju.

**Vsebina sklopa**

Ta učni sklop vsebuje naslednje učne enote:

- **2.1 Principi prve in tretje kotne projekcije**  
  Pregled osnovnih pristopov k projekciji predmetov in razlik med evropskim in ameriškim sistemom.

- **2.2 Pravokotne projekcije (večpogledne risbe)**  
  Prikaz osnovnih pravil pri ustvarjanju večpoglednih risb (zgornji, čelni, stranski pogled).

- **2.3 Aksonometrične projekcije (izometrična projekcija)**  
  Teoretična podlaga in uporaba izometrične projekcije za prikaz kompleksnih oblik.

Vsaka enota vsebuje ločen teoretični del s primeri ter praktične vaje z nalogami in izzivi.

## Principi prve in tretje kotne projekcije

V tehničnem risanju uporabljamo različne načine za prikazovanje 3D predmetov na 2D ravnino. Dva glavna sistema projekcije sta:

### Prva kotna projekcija (evropski sistem)

- Objekt se nahaja med opazovalcem in ravnino projekcije,
- Pogledi so razporejeni: desni pogled na levo, zgornji pogled spodaj,
- Označena s simbolom ISO: kvadratni stožec obrnjen proti opazovalcu.

### Tretja kotna projekcija (ameriški sistem)

- Ravnina projekcije je med opazovalcem in objektom,
- Pogledi so razporejeni: desni pogled desno, zgornji pogled zgoraj,
- Označena s simbolom ANSI: kvadratni stožec obrnjen stran od opazovalca.

### Primerjava sistemov

| Pogled        | Prva kotna projekcija | Tretja kotna projekcija |
|---------------|------------------------|--------------------------|
| Desni         | levo                   | desno                   |
| Zgornji       | spodaj                 | zgoraj                  |

### Uporaba

- V Evropi je standardizirana **prva kotna projekcija** (ISO 5456-2),
- V ZDA in Kanadi se uporablja **tretja kotna projekcija** (ASME Y14.3).

### Pomembno

- Vedno označimo uporabljeni sistem s simbolom v kotu risbe,
- Napačna interpretacija lahko vodi do napak pri izdelavi.

**Pravilno:** uporaba simbola, dosledna razporeditev pogledov.

**Nepravilno:** mešanje sistemov, pomanjkanje simbola, napačno umeščeni pogledi.

### Naloga: Primerjava projektnih sistemov

1. Na papir nariši predmet (npr. preprost blok z odprtino).
2. Uporabi **prvo kotno projekcijo** za razporeditev pogledov.
3. Na ločenem listu nariši isti predmet z **tretjo kotno projekcijo**.
4. Označi simbole za obe projekciji.
5. Primerjaj razporeditve pogledov in razmisli, katera je bolj intuitivna.

### Naloga: Prepoznavanje sistema

1. Poišči tehniško risbo na spletu ali v učbeniku.
2. Ugotovi, kateri projektni sistem je uporabljen glede na razporeditev pogledov.
3. Poišči ali manjkajo simboli za sistem.

### Izziv: Preoblikovanje risbe

1. Prevedi risbo iz ene projekcije v drugo.
2. Poskrbi za pravilno razporeditev in orientacijo pogledov.
3. Uporabi predlogo risalnega lista z ustreznimi simboli.

#### Preizkusi svoje znanje
- Kako lahko takoj prepoznaš, kateri sistem je uporabljen?
- Kaj pomeni napačna interpretacija projekcije v proizvodnji?
- Kje najdeš standarde, ki določajo te razporeditve?

#### Oddaja naloge
- Format: skenirana risba ali PDF
- Imena datotek: `ime_priimek_projekcija1.pdf`, `ime_priimek_projekcija2.pdf`
- Oddaja: v spletno učilnico ali po e-pošti

#### Refleksija
- Kateri sistem se ti zdi bolj pregleden?
- Kaj ti je povzročilo največ težav pri risanju?
- Kako bi razložil razliko med sistemoma sošolcu?

## Pravokotne projekcije (večpogledne risbe)

Večpogledna risba je standardni način prikaza 3D objekta v 2D prostoru. Uporabljamo več pogledov (čelni, zgornji, stranski), ki omogočajo natančno interpretacijo oblike in dimenzij objekta.

### Pogledi

- **Čelni pogled** (frontal view): osnovni pogled, iz katerega se izhaja,
- **Zgornji pogled** (top view): nad čelnim,
- **Desni stranski pogled** (right side view): desno od čelnega,
- Po potrebi dodamo **levi**, **zadnji** ali **spodnji** pogled.

### Pravila usklajenosti pogledov

- Pogledi morajo biti poravnani,
- Velikosti objektov morajo biti enake v vseh pogledih,
- Debele črte za vidne robove, tanke črtkane za skrite linije.

### Pomožne oznake

- Sredinske črte (centerlines), osi,
- Označene točke, kote,
- Simbol projekcije in naslovna plošča.

### Namen

- Enolična interpretacija oblike,
- Osnova za izdelavo in nadzor,
- Združevanje s kotiranjem in prerezom.

**Pravilno:** poravnani pogledi, dosledna uporaba črt.

**Nepravilno:** pogledi napačno postavljeni, manjkajoče linije ali oznake.

### Naloga: Ročna večpogledna risba

1. Izberi enostaven 3D predmet (npr. črka L v prostoru).
2. Na risalni papir nariši čelni, zgornji in desni stranski pogled.
3. Uporabi ustrezne črte (polne, črtkane, sredinske).
4. Dodaj simbol projekcije in naslovno ploščo.

### Naloga: Digitalna večpogledna risba v FreeCAD

1. Ustvari 3D model izbranega predmeta.
2. Preklopi v okolje **TechDraw**.
3. Ustvari čelni, zgornji in desni pogled na risalni list.
4. Prilagodi razmerje, črte in orientacijo.
5. Shrani risbo kot PDF.

### Izziv: Dodaten pogled in simetrija

1. Dodaj še levi ali zadnji pogled na risbo.
2. Označi vse simetrijske osi.
3. Preveri skladnost med pogledi.

#### Preizkusi svoje znanje
- Zakaj je poravnava pogledov pomembna?
- Kako se pravilno označi sredinske osi?
- Kako v FreeCAD prilagodiš razmerje med pogledi?

#### Oddaja naloge
- Format: PDF ali skenirana risba
- Imena datotek: `ime_priimek_vecpogledi.pdf`
- Oddaja: v spletno učilnico ali po e-pošti

#### Refleksija
- Kaj ti je bilo lažje – ročna ali digitalna risba?
- Kako si preverjal poravnanost pogledov?
- Kaj bi izboljšal pri svoji rešitvi?

## Aksonometrične projekcije (izometrična projekcija)

Izometrična projekcija je posebna oblika aksonometrične projekcije, kjer so tri glavne osi objekta prikazane pod enakimi koti (120° med seboj) in brez perspektive. Uporablja se za bolj intuitiven prikaz 3D oblik.

### Značilnosti izometrične projekcije

- Vse tri osi (X, Y, Z) so enako nagnjene (30° od vodoravnice),
- Razmerja dolžin ostanejo nespremenjena (ni perspektivnega skrajševanja),
- Krogi postanejo elipse, kvadri ostanejo pravokotni.

### Risanje izometričnih projekcij

- Osnovni sistem osi: X (30° desno), Y (30° levo), Z (navpično),
- Izometrična mreža olajša ročno risanje,
- V CAD programih se uporablja izometrični pogled kamere.

### Uporaba

- Hiter vizualni prikaz kompleksne oblike,
- Primeren za predstavitev funkcionalnih sklopov,
- Ni primeren za natančne meritve.

### Primeri

- Tehnični priročniki,
- Priročni prikazi naprav,
- Uvodne predstavitve modelov pred izdelavo.

**Pravilno:** pravilni koti osi, ohranjena razmerja.

**Nepravilno:** mešanje perspektive, nepravilna orientacija osi.

### Naloga: Ročno risanje izometrične projekcije

1. Izberi preprost objekt (npr. kocka z izvrtino).
2. Nariši izometrično mrežo na papir (ali uporabi predlogo).
3. Z njo nariši izometrično projekcijo objekta.
4. Uporabi pravilne kote in razmerja.

### Naloga: Digitalna izometrična projekcija

1. Ustvari model v FreeCAD.
2. Nastavi izometrični pogled v 3D oknu.
3. Posnemi sliko zaslona ali uporabi orodje za izvoz slike.
4. V TechDraw poskusi vključiti izometrični pogled.

### Izziv: Risanje kompleksne oblike

1. Uporabi izometrično mrežo za risanje sestavljenega objekta (npr. stopničasta oblika).
2. Vključi detajle kot so luknje, rezi ali utori.
3. Pripravi legendo z merami.

#### Preizkusi svoje znanje
- Zakaj so krogi v izometrični projekciji elipse?
- Kako nastaviš izometrični pogled v FreeCAD?
- Kakšna je razlika med izometrično in perspektivno projekcijo?

#### Oddaja naloge
- Format: PDF ali slika (PNG, JPG)
- Imena datotek: `ime_priimek_izometrija.pdf`
- Oddaja: v spletno učilnico ali po e-pošti

#### Refleksija
- Kako ti je šlo risanje pod kotom?
- Kaj ti je predstavljalo največji izziv?
- Bi raje uporabljal digitalna orodja za tak prikaz?

# Standardi tehniške dokumentacije

Tehniška dokumentacija je osnova za razumevanje, izdelavo in nadzor tehničnih izdelkov. Natančna in standardizirana dokumentacija zagotavlja jasno komunikacijo med vsemi udeleženci v procesu načrtovanja in proizvodnje. V tem učnem sklopu bomo spoznali temeljne elemente, ki jih predpisujejo mednarodni in nacionalni standardi.

**Vsebina sklopa**

Ta učni sklop vsebuje naslednje učne enote:

- **3.1 Vrste črt, pisava in oznake**  
  Pomen črt različnih debelin, vrstic in simbolov ter uporaba tehniške pisave.

- **3.2 Kote in kotiranje v tehnični dokumentaciji**  
  Pravilno označevanje dimenzij in postavljanje kot.

- **3.3 Prerezi in prikazi prerezov**  
  Prikaz notranjih značilnosti predmetov s pomočjo prerezov.

- **3.4 Toleriranje mer in oblik**  
  Označevanje dovoljenih odstopanj pri dimenzijah in oblikah.

- **3.5 Označevanje hrapavosti površin in materialov**  
  Simboli za površinsko obdelavo in standardni postopki.

- **3.6 Kosovnice in sestavni načrti**  
  Priprava seznama delov in povezava med modeli in dokumentacijo.

- **3.7 Standardi tehniške dokumentacije**  
  Pregled najpomembnejših standardov (ISO, SIST, DIN) in njihova uporaba.

Vsaka enota vsebuje ločen teoretični del s primeri ter praktične vaje z nalogami in izzivi.

## Vrste črt, pisava in oznake

Za razumevanje tehničnih risb je ključno poznavanje različnih vrst črt, ki se uporabljajo za prikazovanje robov, skritih elementov, osi in drugih značilnosti. Poleg črt je pomembna tudi enotna tehniška pisava ter ustrezno označevanje elementov.

### Vrste črt (po SIST ISO 128)

* **Debela polna črta** – vidni robovi in obrisi,
* **Tanka polna črta** – pomožne črte, kotirne črte, oznake,
* **Črtkana črta** – skriti robovi in robovi v notranjosti,
* **Črtno-pikčasta črta** – središčnice, osi simetrije,
* **Dvojno črtno-pikčasta črta** – ravnine prereza.

### Tehniška pisava

* Pisava mora biti enostavna, čitljiva, standardizirana (običajno brez ležečih in pisanih črk),
* Višina znakov: 2.5 mm, 3.5 mm, 5 mm (glede na velikost risbe),
* Debelina črt pisave mora biti usklajena z vrsto črte,
* Pisava se uporablja pri oznakah, kotiranju, nazivnih blokih.

### Simboli in oznake

* **Oznaka prereza**: črka s črto prereza,
* **Oznaka površine**: simbol hrapavosti,
* **Materiali**: oznake materialov v prerezu (npr. jeklo, plastika).

### Vizualni primeri (dodani v PDF/učilnici)

* Risba z vsemi vrstami črt na istem predmetu,
* Primer primerne in neprimerne pisave,
* Legenda z oznakami in simboli.

**Pravilno:** dosledna uporaba črt glede na namen, čista in enotna pisava.

**Nepravilno:** uporaba napačne debeline črt, mešanje črtkane in središčne črte, neberljiva pisava.

### Naloga: Prepoznavanje črt

1. Nariši predmet (npr. valj z luknjo) in uporabi naslednje vrste črt:

   * Debelo polno (vidni robovi),
   * Tanka polna (kotirne črte),
   * Črtkana (skriti robovi),
   * Črtno-pikčasta (os).
2. Legenda: ob vsaki črti napiši njen namen.
3. Shrani risbo kot PDF ali sliko.

### Naloga: Vadba pisave

1. Nariši tabelo s tremi vrsticami:

   * Višina pisave 2.5 mm,
   * Višina pisave 3.5 mm,
   * Višina pisave 5 mm.
2. V vsako vrstico napiši naslednje:

   * “TEHNIŠKA PISAVA”
   * “RISBA 1:1”
   * “IME PRIIMEK”

### Izziv: Kombinirana risba s simboli

1. Na risbo iz prve naloge dodaj oznako prereza (črto prereza A–A).
2. V prerezu uporabi šrafuro (ročno ali digitalno).
3. Dodaj simbol hrapavosti na izbrani rob.
4. Označi material (npr. "jeklo").

#### Preizkusi svoje znanje

* Katera črta predstavlja skrite elemente?
* Katera je standardna višina pisave za nazivni blok?
* Kako je označena središčna črta?

#### Oddaja naloge

* Format: PDF ali sken
* Ime datoteke: `ime_priimek_crte_pisava.pdf`
* Oddaja: v spletno učilnico

#### Refleksija

* Katera črta ti je povzročila največ težav?
* Kako si določil debelino črt?
* Kaj bi izboljšal pri svoji pisavi?

## Kote in kotiranje v tehnični dokumentaciji

Kotiranje je način, kako se na tehnični risbi prikažejo mere, ki določajo velikost in položaj značilnosti objekta. Natančno kotiranje je ključno za razumevanje izdelave.

### Vrste kot

* **Linearno kotiranje** – dolžine med dvema točkama (vodoravno, navpično, diagonalno),
* **Kotno kotiranje** – meri kot med dvema črtama,
* **Radialno kotiranje** – označevanje radijev (R),
* **Premerno kotiranje** – označevanje premerov ($\phi$),
* **Koordinatno kotiranje** – za določanje položajev iz izhodišč.

### Pravila kotiranja

* Vse mere v mm, brez enote (razen če ni drugače določeno),
* Mere ne smejo biti podvojene,
* Ne kotiramo dimenzij, ki jih je mogoče izračunati,
* Dimenzije se postavljajo izven objekta,
* Kotirne črte so tanke, z oznakami puščic.

### Značilni elementi

* Kotirna črta (s puščicama),
* Pomožne črte (od objekta do kotirne črte),
* Številčna vrednost dimenzije nad kotirno črto.

**Pravilno:** uporaba pravih vrst kotiranja, doslednost postavitve.

**Nepravilno:** dvojno kotiranje, kotiranje na samem predmetu, manjkajoče pomožne črte.

### Naloga: Linearno in kotno kotiranje

1. Nariši pravokotnik z dimenzijami 80 mm × 40 mm.
2. Dodaj linearne mere za dolžino in širino.
3. Dodaj diagonalo in označi kot med daljšo stranico in diagonalo.
4. Uporabi pravilne kotirne črte in puščice.

### Naloga: Radialno in premerno kotiranje

1. Nariši krog premera 60 mm in dodaj:

   * Premer ( $\phi$ 60 mm),
   * Radij (R30 mm), če uporabiš lok.
2. Dodaj še en manjši krog z radijem 10 mm.
3. Kotiraj z radialno in premerno oznako.

### Izziv: Kotiranje sestavljenega predmeta

1. Nariši predmet z luknjo, izvrtino in poševnim robom.
2. Uporabi:

   * Linearno kotiranje,
   * Kotno kotiranje,
   * Radialno kotiranje.
3. Preveri, da mere niso podvojene in da so postavljene zunaj objekta.

#### Preizkusi svoje znanje

* Kako se razlikujeta radij in premer?
* Kje naj bo postavljena številčna vrednost?
* Kaj pomeni, da mere ne smejo biti podvojene?

#### Oddaja naloge

* Format: PDF ali sken
* Ime datoteke: `ime_priimek_kotiranje.pdf`
* Oddaja: v spletno učilnico

#### Refleksija

* Katera vrsta kotiranja ti je bila najlažja?
* Kako si preveril pravilnost postavitve mer?
* Kaj bi izboljšal v svojem prikazu?

## Prerezi in prikazi prerezov

Prerezi omogočajo prikaz notranjih značilnosti objekta, ki jih z zunanjimi pogledi ni mogoče jasno predstaviti. Uporabljajo se tam, kjer je potrebno pokazati votline, luknje, reže in drugo notranjo strukturo.

### Vrste prerezov

* **Polni prerez** – objekt prerežemo povsem,
* **Delni prerez** – prikažemo le del prereza (z lomljeno črto),
* **Stopničasti prerez** – prerez poteka v več ravninah,
* **Osni prerez** – simetrični objekti (npr. gredi) z osjo prereza.

### Označevanje prerezov

* **Črta prereza**: črtno-pikčasta z debelimi zaključki in puščicami,
* **Oznaka prereza**: črka (A–A, B–B), označena ob puščicah,
* **Šrafura**: prikaz prerezanega materiala z enakomernimi poševnimi črtami.

### Pravila

* Šrafura pod kotom 45° (če ni drugače določeno),
* Razmik med črtami je enoten,
* Različni materiali = različne šrafure ali oznake,
* Ne šrafiramo vijakov, osi, standardnih elementov.

**Pravilno:** pravilno označen rez, enotna šrafura, čista postavitev.

**Nepravilno:** manjkajoče oznake, prekomerna šrafura, nejasna smer prereza.

### Naloga: Polni prerez

1. Nariši valjasto telo z izvrtino.
2. Uporabi črto prereza A–A skozi središče.
3. Nariši pogled A–A kot polni prerez.
4. Uporabi enotno šrafuro (45°),
5. Ne šrafiraj osi in vijakov.

### Naloga: Delni prerez

1. Nariši L-profil (kotni del) s simetrijo.
2. Nariši delni prerez z lomljeno črto.
3. Uporabi šrafuro samo v prikazanem delu.

### Izziv: Stopničasti prerez

1. Nariši objekt s tremi nivoji (npr. osnovna plošča, vmesna plast, zgornji pokrov).
2. Definiraj pot prereza z več zavoji.
3. Nariši ustrezen prerez z vsemi elementi.
4. Označi vsak nivo s svojo oznako.

#### Preizkusi svoje znanje

* Kdaj uporabiš delni in kdaj polni prerez?
* Kako se označi črta prereza?
* Zakaj ne šrafiramo vseh delov?

#### Oddaja naloge

* Format: PDF ali sken
* Ime datoteke: `ime_priimek_prerezi.pdf`
* Oddaja: v spletno učilnico

#### Refleksija

* Kaj ti je bilo najtežje pri risanju prereza?
* Kako si določil smer prereza?
* Kaj bi izboljšal v šrafuri?

## Toleriranje mer in oblik

Toleriranje omogoča, da določimo dopustna odstopanja od nominalnih mer, kar je bistveno za pravilno delovanje in sestavljanje delov.

### Vrste toleranc

* **Dimenzijske tolerance** – dovoljeno odstopanje pri dolžini, višini, premeru:

  * Simetrične (±0.1 mm),
  * Enostranske (+0.2 / -0.0 mm).

* **Geometrijske tolerance** – odstopanja oblike in lege:

  * Ravnost, vzporednost, pravokotnost,
  * Koncentričnost, valjavitost, kotnost.

### Zapisi toleranc

* Dimenzija z oznako tolerance: 50 ±0.1 mm
* Geometrijske tolerance s simbolom v kvadratnem okvirju:

  * simbol in vrednost (npr. 0.05)

### Uporaba

* Pri sestavljanju gibljivih delov (ležaji, osi, puše),
* Kjer je pomembna natančnost prileganja,
* Pri zahtevah za stabilnost in kakovost.

**Pravilno:** uporaba ustrezne tolerance glede na funkcijo dela.

**Nepravilno:** manjkajoče tolerance, neskladje med zahtevo in izvedbo, napačna oznaka.

### Naloga: Dimenzijske tolerance

1. Nariši valj premera 20 mm.
2. Označi dimenzijo z dopustnim odstopanjem ±0.1 mm.
3. Nariši odprtino premera 20.2 mm z odstopanjem -0.0 / +0.2 mm.
4. Označi prileganje z razlago (ohlapno).

### Naloga: Geometrijske tolerance

1. Nariši kvader z zgornjo ploskvijo kot funkcionalno površino.
2. Dodaj toleranco:

   * Ravnost 0.05 mm,
   * Pravokotnost 0.1 mm na referenco.
3. Uporabi simbole v kvadratnih okvirčkih.

### Izziv: Kombinacija toleranc

1. Nariši sestavljeni del z dvema gibljevima komponentama.
2. Določi:

   * Dimenzijske tolerance za gred in ležaj,
   * Geometrijske tolerance za osi.
3. Opiši vpliv toleranc na delovanje.

#### Preizkusi svoje znanje

* Kdaj uporabiš simetrično in kdaj enostransko toleranco?
* Kaj pomeni v geometrijski toleranci?
* Zakaj so tolerance pomembne pri sestavih?

#### Oddaja naloge

* Format: PDF ali sken
* Ime datoteke: `ime_priimek_tolerance.pdf`
* Oddaja: v spletno učilnico

#### Refleksija

* Kako si določil, katere tolerance uporabiti?
* Katere oznake so ti bile najmanj jasne?
* Kako bi razložil toleranco sošolcu?

## Označevanje hrapavosti površin in materialov

Površinska hrapavost pomembno vpliva na delovanje mehanskih komponent, zlasti tam, kjer prihaja do stika med deli. Pravilno označevanje hrapavosti je bistven del tehniške dokumentacije.

### Simboli za hrapavost (po ISO 1302)

* Osnovni simbol: $\nabla$ (brez dodatnih oznak),
* S specifikacijo: $\nabla$ Ra 3.2 (površinska hrapavost v $\mu m$),
* Prepoved obdelave: $\frown$ (simbol s črtico),
* Dovoljena katerakoli obdelava: $\nabla$ (brez dodatnih oznak).

### Kjer se uporablja

* Površine za tesnjenje,
* Ležajne površine,
* Estetske površine ali tiste, ki zahtevajo določeno drsnost.

### Označevanje materialov

* V prerezih: tekstualno (npr. "jeklo", "aluminij"),
* S šrafurami ali simboli za materiale,
* V legendi risbe ali neposredno ob elementu.

### Pravila

* Simbol hrapavosti je vedno obdan s pomožno črto,
* Zapis Ra vrednosti je v mikrometrih ( $\mu m$),
* Material je jasno označen ob prerezih.

**Pravilno:** simboli z ustrezno Ra vrednostjo, ustrezna postavitev.

**Nepravilno:** manjkajoči simboli, napačna interpretacija vrednosti, nejasne oznake.

### Naloga: Označevanje hrapavosti

1. Nariši ploščico z zgornjo površino za drsenje.
2. Dodaj simbol hrapavosti Ra 1.6 µm na zgornjo površino.
3. Na spodnjo površino dodaj simbol "ne obdeluj" ( $\frown$ ).
4. Označi preostale površine kot dovoljene za poljubno obdelavo.

### Naloga: Označevanje materiala

1. V prerezu označi material kot “jeklo”.
2. Dodaj šrafuro v skladu s standardom ( $45^\circ$ ).
3. Dodaj simbol hrapavosti Ra 3.2 $\mu m$ na izpostavljeni rob.

### Izziv: Kombinacija materialov in površin

1. Nariši sestavljen kos iz dveh različnih materialov (npr. jeklo in plastika).
2. Označi vsak material s tekstom in drugačno šrafuro.
3. Dodaj različne zahteve za hrapavost (Ra 0.8 $\mu m$ za eno, Ra 6.3 $\mu m$ za drugo).

#### Preizkusi svoje znanje

* Kaj pomeni Ra 1.6 $\mu m$?
* Kako označiš, da površina ne sme biti obdelana?
* Kako vizualno ločiš materiale v prerezu?

#### Oddaja naloge

* Format: PDF ali slika
* Ime datoteke: `ime_priimek_hrapavost_materiali.pdf`
* Oddaja: v spletno učilnico

#### Refleksija

* Kako si določil vrednosti hrapavosti?
* Kaj si uporabil za razpoznavanje materialov?
* Kaj bi še želel pojasniti o tem področju?

## Kosovnice in sestavni načrti

Kosovnica (ang. Bill of Materials – BOM) je seznam vseh komponent, ki sestavljajo končni izdelek. Sestavni načrt pa prikazuje, kako so ti deli medsebojno povezani.

### Kosovnica

* Seznam vseh delov:

  * Ime dela,
  * Količina,
  * Material,
  * Številka pozicije.
* Lahko vključuje tudi:

  * Standard (če gre za standardni element),
  * Dimenzije,
  * Dobavitelja.

### Sestavni načrt

* Tehniška risba celotnega izdelka,
* Označbe posameznih komponent s številkami (pozicije),
* Povezava z vrstico v kosovnici.

### Pravila

* Pozicijske številke morajo biti enolične,
* Vse komponente v risbi morajo biti vključene v kosovnico,
* Sestavni načrt mora biti pregleden in enostavno berljiv.

**Pravilno:** ujemanje pozicij med risbo in tabelo, jasne oznake.

**Nepravilno:** manjkajoči deli v kosovnici, podvojene številke, slaba berljivost.

### Naloga: Sestavni načrt in kosovnica

1. Nariši izdelek iz vsaj 3 delov (npr. osnovna plošča, valj, pokrov).
2. Dodeli pozicijske številke (1, 2, 3).
3. Naredi tabelo (kosovnico) z naslednjimi stolpci:

   * Pozicija,
   * Naziv dela,
   * Količina,
   * Material.
4. Poveži številke v risbi s tabelo.

### Naloga: Digitalna kosovnica v FreeCAD

1. Ustvari sestav v okolju A2+ ali Assembly4.
2. Označi posamezne dele z atributi (npr. naziv, material).
3. Izvozi kosovnico v CSV ali vstavi v TechDraw.

### Izziv: Večnivojska kosovnica

1. Pripravi podsklop (npr. ohišje iz več delov).
2. Prikaži povezavo med podsklopi in glavnim sklopom.
3. Uporabi označevanje pozicij v obliki 1.1, 1.2, 2.1 …

#### Preizkusi svoje znanje

* Kaj mora vsebovati kosovnica?
* Kako veš, da je sestavni načrt pravilen?
* Kako v FreeCAD povežeš risbo s tabelo?

#### Oddaja naloge

* Format: PDF + kosovnica (CSV ali ročno)
* Ime datoteke: `ime_priimek_kosovnica.pdf`
* Oddaja: v spletno učilnico

#### Refleksija

* Kako si organiziral povezavo med delom in tabelo?
* Kaj je največji izziv pri izdelavi sestavnega načrta?
* Kako bi razložil pomen kosovnice nekomu, ki še ni modeliral?

## Standardi tehniške dokumentacije

Uporaba standardov zagotavlja enotno razumevanje tehničnih risb, ne glede na to, kdo jih bere ali izdela. Standardi določajo vse – od vrst črt, simbolov, meril do načina postavitve risbe.

### Ključni standardi

* **ISO (Mednarodna organizacija za standardizacijo)**

  * ISO 128: pravila tehničnega risanja,
  * ISO 7200: podatkovna polja risb,
  * ISO 1302: hrapavost.

* **SIST (Slovenski inštitut za standardizacijo)**

  * Slovenski prevodi ISO standardov,
  * Lokalno veljavne oznake in posebnosti.

* **DIN (Nemški standardi)**

  * Včasih bolj podrobni, specifični za orodjarstvo.

### Kako uporabljamo standarde

* Pri risanju ročno in digitalno (FreeCAD, AutoCAD ...),
* Pri branju dokumentacije drugih izdelovalcev,
* Pri izdelavi projektov, kjer sodelujejo različni partnerji.

### Kje jih najdemo

* Spletna stran SIST,
* ISO portal,
* Učbeniki in priročniki za tehnično risanje.

**Pravilno:** sklicevanje na veljavne standarde, uporaba najnovejših različic.

**Nepravilno:** ignoriranje standardov, uporaba zastarelih praks, mešanje sistemov.

### Naloga: Iskanje standardov

1. Obišči spletno stran SIST ali ISO.
2. Poišči vsaj dva standarda, povezana s tehničnim risanjem.
3. Zapiši:

   * Oznako (npr. ISO 128),
   * Naslov,
   * Področje uporabe.

### Naloga: Analiza risbe po standardih

1. Poišči primer tehniške risbe (npr. iz učbenika).
2. Ugotovi, kateri standardi so upoštevani:

   * Vrste črt,
   * Oznake,
   * Podatkovno polje.
3. Označi elemente in komentiraj pravilnost.

### Izziv: Primerjava med standardi

1. Izberi en element (npr. kotiranje).
2. Primerjaj zapis v ISO, DIN in SIST različici (če je dostopno).
3. Pripravi tabelo s primerjavo.

#### Preizkusi svoje znanje

* Kje najdeš standarde?
* Zakaj so potrebni prevodi (SIST)?
* Kako preveriš, ali je risba standardna?

#### Oddaja naloge

* Format: PDF ali tekstovni dokument
* Ime datoteke: `ime_priimek_standardi.pdf`
* Oddaja: v spletno učilnico

#### Refleksija

* Kaj te je presenetilo pri iskanju standardov?
* Kako pogosto bi moral risar uporabljati standarde?
* Kaj bi svetoval začetniku pri razumevanju standardov?

# Ročno tehniško risanje

Čeprav danes večinoma uporabljamo računalniško podprto konstruiranje (CAD), ima ročno tehniško risanje še vedno pomembno vlogo pri učenju osnov tehničnega komuniciranja, geometrije in prostorske predstave.

Ročno risanje razvija občutek za razmerja, natančnost in razumevanje projekcij. Pomembno je tudi za hitro skiciranje idej in za dokumentacijo v pogojih, kjer računalnik ni na voljo.

**Vsebina sklopa**

Ta učni sklop vsebuje naslednje učne enote:

* **4.1 Vloga ročnega risanja**
  Zgodovinski pregled in pomen risanja za razvoj prostorske predstave.

* **4.2 Trdota svinčnika, pripomočki in priprava**
  Pravilna izbira orodij za tehnično risanje in priprava risalne mape.

* **4.3 Risanje osnovnih geometrijskih elementov**
  Vadba risanja pravokotnic, krogov in vzporednic z uporabo pripomočkov.

* **4.4 Osnove opisne geometrije**
  Risanje preslikav in razumevanje projekcij točk in likov v prostoru.

Vsaka enota vsebuje ločen teoretični del s primeri ter praktične vaje z nalogami in izzivi.

## Vloga ročnega risanja

Ročno tehniško risanje ima dolgo zgodovino in je bilo pred uvedbo CAD orodij edini način za tehnično komuniciranje med inženirji, tehnologi in izdelovalci. Danes ostaja pomembno kot temeljno orodje za razvijanje prostorske predstave, natančnosti in razumevanja projekcij.

### Zgodovinski kontekst

* Prve tehniške risbe so nastale že v antičnem Rimu (Vitruvijeve risbe),
* V času renesanse so umetniki kot Leonardo da Vinci uporabljali natančne skice za tehnične zamisli,
* Do 20. stoletja je bilo ročno risanje osrednje orodje v tehničnih poklicih.

### Današnja vloga

* Uporablja se pri hitrem konceptnem načrtovanju,
* Ključno v izobraževanju za razvoj razumevanja geometrije,
* Omogoča komunikacijo brez računalniških orodij.

### Prednosti

* Razvija fino motoriko in občutek za razmerja,
* Omogoča bolj intuitivno risanje,
* Krepi temeljno razumevanje projektivnega prikaza.

**Pravilno:** uporaba osnovnih geometrijskih oblik, ohranjanje čistosti linij, jasno ločevanje med vrstami črt.

**Nepravilno:** neporavnane projekcije, prekrivanje črt, risanje brez uporabe pripomočkov.

### Naloga: Primerjaj dva tipa risbe

1. Nariši enostaven predmet (npr. kvader z izvrtino) ročno s svinčnikom,
2. Nato ga nariši v poljubnem CAD programu,
3. Primerjaj:

   * Čas izvedbe,
   * Jasnost projekcij,
   * Napake pri ročni risbi.

### Naloga: Risanje brez pripomočkov

1. Poskusi narisati osnovno pravokotno projekcijo (čelni, zgornji, stranski pogled) brez ravnila,
2. Nato enako ponovi z ravnilom in kotomerom,
3. Ugotovi razlike v natančnosti in berljivosti.

### Izziv: Skiciranje tehniške ideje

1. Predstavljaj si tehničen predmet (npr. držalo za telefon),
2. Ročno skiciraj tri poglavitne poglede,
3. Dodaj osnovne mere in legendo.

#### Preizkusi svoje znanje

* Zakaj je ročno risanje še vedno pomembno?
* Katere spretnosti razvijaš z njim?
* Kdaj je ročna skica lahko boljša kot CAD?

#### Oddaja naloge

* Format: sken ali PDF
* Ime datoteke: `ime_priimek_rocna_skica.pdf`
* Oddaja: v spletno učilnico

#### Refleksija

* Kaj ti je bilo najtežje brez pripomočkov?
* Kaj si opazil pri primerjavi CAD in ročne risbe?
* Kdaj bi uporabil ročno risbo v praksi?

## Trdota svinčnika, pripomočki in priprava

Uspešna ročna tehniška risba je odvisna od ustreznih orodij, natančnosti in doslednosti. Pravilna izbira svinčnika in pripomočkov vpliva na berljivost in kakovost risbe.

### Trdota svinčnikov

* Oznake:

  * H – trdi svinčniki (tanke, svetle linije),
  * B – mehki svinčniki (temne, debelejše linije),
  * HB – srednji, univerzalni svinčnik,
* Uporaba:

  * 2H ali H za pomožne črte,
  * HB ali B za konture, vidne robove.

### Risalni pripomočki

* Ravnila (30 cm, 50 cm),
* Kotomeri (30°–60°, 45°),
* Krogla, šablone,
* Tehniški svinčniki (0.5 mm, 0.7 mm),
* Risalne mape in papir (A4, A3),
* Brisalci, radirke s šablono.

### Priprava risalne mape

* Oznaka imena, datuma, šole,
* Naslovna plošča na desnem spodnjem delu,
* Označene meje risalnega lista,
* Čistost in preglednost.

**Pravilno:** ustrezna izbira svinčnika glede na funkcijo črte, čiste linije, brez odvečnih oznak.

**Nepravilno:** enaka črta za vse elemente, nepravilno označen list, manjkajoča orodja.

### Naloga: Preskusi svinčnike različnih trdot

1. Na papir nariši 3 horizontalne črte:

   * Prvo s svinčnikom 2H,
   * Drugo s HB,
   * Tretjo s B.
2. Primerjaj linije:

   * Debelina,
   * Očitnost,
   * Možnost brisanja.

### Naloga: Pripravi risalni list

1. Pripravi A4 ali A3 papir,
2. Označi robove (10 mm od roba),
3. Nariši naslovno polje:

   * Ime, priimek,
   * Datum,
   * Predmet,
   * Naziv risbe,
4. Uporabi šablono, če je na voljo.

### Izziv: Nariši risalno postajo

1. Skiciraj od zgoraj pogled na risalno mizo s pripomočki,
2. Označi vsak pripomoček z imenom,
3. Opiši, čemu služi vsak.

#### Preizkusi svoje znanje

* Kdaj uporabiš 2H in kdaj B svinčnik?
* Zakaj je pomembna priprava lista?
* Katere pripomočke si pogrešal?

#### Oddaja naloge

* Format: PDF ali fotografija
* Ime datoteke: `ime_priimek_priprava_risanja.pdf`
* Oddaja: v spletno učilnico

#### Refleksija

* Kaj si se naučil o uporabi svinčnikov?
* Kako si pripravil naslovno polje?
* Kaj bi spremenil v svojem delovnem procesu?

## Risanje osnovnih geometrijskih elementov

Temelj vsake tehniške risbe so osnovne geometrijske oblike. Njihovo pravilno risanje omogoča natančne konstrukcije in razumevanje tehničnih predmetov.

### Ključni elementi

* **Ravnina** – podlaga za vse ostalo,
* **Točka** – začetek črte, središče kroga,
* **Črta** – ravna povezava dveh točk,
* **Pravokotnica** – črta pod pravim kotom,
* **Vzporednica** – črta, ki je enako oddaljena,
* **Krog** – točke enako oddaljene od središča.

### Tehniške risarske tehnike

* Uporaba kotomera za pravokotnice in vzporednice,
* Risanje krogov s šestilom,
* Natančno merjenje z ravnilom,
* Označevanje presečišč in sredin.

### Uporaba v tehnični risbi

* Konstrukcija osnovnih teles (kvadri, valji),
* Priprava osnov za prostorske prikaze,
* Pomožne črte za pozicioniranje.

**Pravilno:** čiste in tanke pomožne črte, natančne mere, jasna presečišča.

**Nepravilno:** debela skica, neporavnane črte, ročno risani krogi brez šestila.

### Naloga: Pravokotnice in vzporednice

1. Nariši točko A,
2. Iz točke A nariši črto,
3. Konstruiraj pravokotnico na črto v točki A,
4. Nariši dve vzporednici z razmikom 15 mm.

### Naloga: Krogi in loki

1. Nariši krog premera 50 mm,
2. Nariši drugi krog z istim središčem, premera 30 mm,
3. Nariši lok 90° s polmerom 20 mm.

### Izziv: Kombinacija osnovnih elementov

1. Nariši kvadrat s stranico 60 mm,
2. V vsako stranico vriši sredinsko točko,
3. Poveži središča z diagonalo,
4. Na sredini kvadrata nariši krog premera 40 mm.

#### Preizkusi svoje znanje

* Kaj je razlika med krogom in lokom?
* Kako preveriš, da sta črti vzporedni?
* Kako se konstruira pravokotnica brez kotomera?

#### Oddaja naloge

* Format: sken risbe ali PDF
* Ime datoteke: `ime_priimek_geometrija.pdf`
* Oddaja: v spletno učilnico

#### Refleksija

* Kaj ti je bilo najlažje?
* Kaj je bilo najzahtevnejše pri merjenju?
* Kako si preveril natančnost?

## Osnove opisne geometrije

Opisna geometrija omogoča natančen prikaz prostorskih objektov na ravnini z uporabo projekcij. Gre za temeljno disciplino pri tehničnem risanju in inženirskem načrtovanju.

### Ključni pojmi

* **Točka** – osnovni element, ki ga projiciramo na ravnine,
* **Ravnina** – vodilna površina, na katero projiciramo (čelna, vodoravna, stranska),
* **Projekcija** – preslikava objekta na izbrano ravnino,
* **Sled ravnine** – linija presečišča ravnine s projekcijsko ravnino.

### Vrste projekcij

* Pravokotna projekcija (ortogonalna),
* Aksonometrična (izometrična, dimetrična),
* Kotna projekcija.

### Postopki risanja

* Najprej določimo ravnine (XY, YZ, XZ),
* Nato določimo točke v prostoru in njihove preslikave,
* Uporabimo čiste pomožne črte in oznake.

### Uporaba

* Razumevanje 3D oblike prek 2D prikazov,
* Osnova za razumevanje večpoglednih risb,
* Uporabno pri konstruiranju kompleksnih teles.

**Pravilno:** pravilna zaporednost projekcij, poravnane točke med pogledi.

**Nepravilno:** mešanje ravnin, neoznačene preslikave, nepravilne sledi.

### Naloga: Projekcija točke

1. Določi točko A v prostoru,
2. Nariši njeno projekcijo na vodoravno (XY), čelno (XZ) in stransko (YZ) ravnino,
3. Označi $A_N$ (čelni pogled), $A_T$ (vodoravni), $A_S$ (stranski).

### Naloga: Projekcija daljice

1. Določi točki A in B,
2. Poveži ju z daljico v prostoru,
3. Izriši vse tri ortogonalne projekcije daljice.

### Izziv: Projekcija trikotnika

1. Nariši trikotnik v prostoru (točke A, B, C),
2. Prikaži vse projekcije (čelno, vodoravno, stransko),
3. Poveži točke z ustreznimi linijami.

#### Preizkusi svoje znanje

* Kaj pomeni $A_N, $A_T in $A_S$?
* Kako se določi središče projekcije?
* Kako preveriš pravilnost projekcije?

#### Oddaja naloge

* Format: PDF ali sken
* Ime datoteke: `ime_priimek_opisna_geometrija.pdf`
* Oddaja: v spletno učilnico

#### Refleksija

* Kaj ti je bilo najtežje pri risanju več projekcij?
* Kako si preveril poravnanost točk?
* Kaj si se naučil o pomenu ravnin?

