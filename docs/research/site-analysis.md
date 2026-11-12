# A jelenlegi modulshop.hu elemzése

- **Gyűjtés dátuma:** 2026-11-12
- **Módszer:** sima `curl` kérések (bejelentkezés nélkül, kb. 1 kérés/mp), a HTML-t a scratchpadban dolgoztuk fel. Letöltöttük a sitemapet, a menüben szereplő összes kategória első oldalát, a tájékoztató oldalakat és 39 termékoldalt. A teljes katalógust nem töltöttük le.
- **Platform:** ShopRenter, `hamburg_global` téma (a CSS-útvonalakban: `modulshop.cdn.shoprenter.hu/catalog/view/theme/hamburg_global/...`). A footerben ShopRenter-logó és -link látható.
- **Ehhez tartozik még:** `docs/research/products-sample.json` (36 mintatermék).
- Csak olyat írtunk le, amit láttunk. Minden állítás mellett ott a forrás URL-je. Ahol két oldal ellentmond egymásnak, mindkét adatot leírtuk (lásd a 8. fejezetet).

---

## 1. Kategóriafa és termékszámok

**Forrás:** a főoldal kategóriamenüje (https://modulshop.hu/) és a kategóriaoldalakon kiírt „1 - 18 / N termék” számláló. A számokat 2026-11-12-én olvastuk le.

**Összesítés**
- Az „Összes termék” kategória 1811 terméket mutat (https://modulshop.hu/osszes-termek-191).
- A „Csak raktáron lévő termékek” szűrővel 1019 marad (https://modulshop.hu/osszes-termek-191?stockfilter=1). Vagyis a termékek **kb. 44%-a nincs raktáron**.
- A sitemapben (https://modulshop.hu/sitemap.xml) 1950 URL van:
  - 1856 db 0.6-os prioritású (termékek),
  - 56 db 0.8-as (kategóriák és a „Modulshop” gyártóoldal),
  - 37 db 0.3-as (tájékoztató oldalak és blog).
- A „Modulshop” gyártóoldalon 561 termék szerepel (https://modulshop.hu/modulshop-m-32).

> **Fontos:** egy főkategória oldala csak a közvetlenül hozzá rendelt termékeket listázza, az alkategóriák termékeit nem. Például a „Mikrovezérlők, alaplapok” oldalon 1 termék látszik, miközben az alkategóriákban összesen 116 van. Ezért a főkategóriák becsült termékszáma = a közvetlen termékek + az alkategóriák összege. Egy termék több kategóriában is lehet, ezért az összeg (≈2200) nagyobb az 1811-nél.

| # | Főkategória (URL) | Alkategóriák (URL, termékszám) | Becsült termékszám |
|---|---|---|---|
| 1 | Általunk készített termékek – https://modulshop.hu/sajat-termekeink-244 | – | 6 |
| 2 | Csomag ajánlataink – https://modulshop.hu/csomag-ajanlataink-242 | – (301-es átirányítás a https://modulshop.hu/csomag-ajanlataink-101 oldalra, amely **üres tájékoztató oldal**) | 0 |
| 3 | Mikrovezérlők, alaplapok – https://modulshop.hu/mikrovezerlok-alaplapok-157 (közvetlenül 1) | Arduino `/mikrovezerlok-alaplapok-157/avr-duino` (37; a menü „34”-et ír) · ESP8266 `/esp-167` (23; a menü „22”-t ír) · ESP32 `/esp32-205` (43) · STM `/stm-168` (4) · Raspberry `/raspberry-208` (9) | ~117 |
| 4 | Szenzor Modulok – https://modulshop.hu/szenzor-modulok-158 (közvetlenül 4) | Hőmérséklet, pára, nyomás `/homerseklet-para-nyomas-184` (31) · Feszültség, áram, távolság `/feszultseg-aram-tavolsag-185` (37) · Fény, mozgás, giro, gyursulás, RFID érzékelés `/feny-mozgas-erzekeles-186` (49) | ~121 |
| 5 | Egyéb Modulok – https://modulshop.hu/egyeb-modulok-159 (közvetlenül 33) | Beviteli eszközök `/beviteli-eszkozok-189` (44) · Komunikációs modulok `/komunikacios-modulok-187` (64) · Motor, DC, Léptető, Szervó `/motork-dc-lepteto-szervo-192` (47) · Motorvezérlők `/motor-vezerlok-188` (27) · Próbapanelek, shieldek, egyéb `/probapanelekshieldekegyeb-196` (52) · Relék, Optocsatolók `/relek-211` (49) | ~316 |
| 6 | Erősítők, Végfokok – https://modulshop.hu/erositok-vegfokok-160 (közvetlenül 1) | 100W fölötti + 2.1 `/100w-folotti-21-171` (39) · 2*50W erősítő, végfok `/250w-erositovegfok-170` (51) · Audió kiegészítők `/audio-kiegeszitok-173` (57) · Hangszóró `/hangszoro-222` (8) | ~156 |
| 7 | LCD-k, Kijelzők – https://modulshop.hu/lcd-k-kijelzok-161 | – | 50 |
| 8 | BMS-ek, 18650 Akkuk – https://modulshop.hu/bms-ek-18650-akkuk-162 (közvetlenül 1) | 1S - 5S BMS `/1s-5s-bms-169` (33) · Akku cellák, elemek `/akku-cellak-elemek-236` (24) · 6S - 13S BMS `/6s-13s-bms-172` (14) · Akku töltők `/akku-toltok-175` (45) · Egyéb `/egyeb-176` (79; a H1 szerint „BMS kiegészítők”) | ~196 |
| 9 | DC, AC konverterek – https://modulshop.hu/dc-ac-konverterek-163 (közvetlenül 1) | AC->DC tápegységek, labortáp `/dc-tapegysegek-194` (48) · DC-DC Step down, fesz.csökkentő `/dc-dc-step-down-feszcsokkento-181` (59) · DC-DC Step up, fesz.növelő `/dc-dc-step-up-fesznovelo-182` (26) | ~134 |
| 10 | Műszerek – https://modulshop.hu/muszerek-164 (közvetlenül 93) | Műszerdobozok `/muszerdobozok-227` (16) | ~109 |
| 11 | Egyéb – https://modulshop.hu/egyeb-165 (közvetlenül 141) | Szerszámok `/szerszamok-220` (55) | ~196 |
| 12 | Elektronika – https://modulshop.hu/elektronika-177 (közvetlenül 24) | Ellenállások, potméterek `/ellenallasok-potmeterek-180` (146) · Fizika óra, áramköri elemek `/fizika-ora-aramkori-elemek-203` (17) · Hűtőbordák, Ventilátorok `/csatlakozok-vezetekek-202` (18; **a slug nem egyezik a névvel**) · IC `/ic-178` (40) · Kapcsolók, csatlakozók, vezetékek `/kapcsolok-csatlakozok-vezetekek-200` (219) · Kondenzátorok, Diódák `/kondenzatorok-195` (57) · Ledek `/ledek-183` (47) · PCB nyáklapoK, forrasztási anyagok `/pcb-nyaklapok-forrasztasi-anyagok-193` (32) · Tranzisztor MosFet `/tranzisztor-mosfet-179` (52) | ~652 |
| 13 | D.I.Y. Készletek – https://modulshop.hu/diy-keszletek-225 (közvetlenül 57) | Csavarok, betétek `/csavarok-betetek-239` (7) · Távtartók `/tavtartok-237` (18) | ~82 |
| 14 | Csomagok – https://modulshop.hu/csomagok-190 | – | 15 |
| 15 | Led világítás – https://modulshop.hu/led-vilagitas-197 | – | 54 |
| 16 | Összes termék – https://modulshop.hu/osszes-termek-191 | – | 1811 (ebből 1019 raktáron) |

A táblázatban az alkategóriák URL-je a főkategória slugja után következik. Például az Arduino teljes címe: `https://modulshop.hu/mikrovezerlok-alaplapok-157/avr-duino`.

**Javaslat a Shopify-kollekciókhoz:** a 12 tényleges termékcsoport (3–15. sor) legyen főkollekció. Az „Általunk készített termékek” és a „Csomagok” jó kiemelt kollekció lehet. Az „Egyéb” (141 közvetlen termék) és az „Egyéb Modulok” (33 közvetlen termék) tartalmát érdemes átnézni és szétosztani.

---

## 2. Fejléc, lábléc, navigáció, keresés, szűrés, rendezés

**Forrás:** https://modulshop.hu/ és a kategóriaoldalak.

### Felső sávok (fentről lefelé)
1. **Cookie-sáv** két kategóriával („Szükséges cookie-k”, „Marketing cookie-k”), „Beállítások módosítása” és „Elfogadom” gombbal.
2. **Rotáló hirdetősáv** három üzenettel:
   - „Személyes átvétellel kapcsolatos kérdésed van? Katt ide!” → GYIK
   - „Szállítási áraink ....” → https://modulshop.hu/szallitasi-informaciok-65
   - „Görgess lejjebb a további tartalmakért!” → `#`
3. **Kapcsolati sor:** `+36/70 944 76 41`, `info@modulshop.hu`, Belépés, Regisztráció.
4. **Fejléc:** logó (350×80), kereső (placeholder: „keresés...”, élő javaslatokkal: `index.php?route=product/list/suggest`), kívánságlista, kosár (oldalsó kosárfiókkal), ragadós fejléc.
5. **Kategóriamenü:** „Kategóriák / Termékek” lenyíló, kétszintű menü (a fenti fa). Mellette a következő linkek:
   - Hűségpont rendszer, Regisztráció, Online elállás
   - Gyakran ismételt kérdések (**kétszer** szerepel)
   - Szállítási Információk, 30 napos termék-visszaküldés, Szállítási módok, Kapcsolat
6. **Mobilon** mmenu-alapú hamburger menü. A nyelvválasztó (hu) és a pénznemválasztó (HUF) itt is megjelenik.

### A főoldal blokkjai (sorrendben)
1. **Bannerslider:** jelenleg egyetlen, 1350×500-as kép, rajta csak szöveg („Köszönjük! … ezen a héten MINDEN csomagot át fogunk adni a futároknak!”). Nincs alt szövege és linkje sem (`bannerek/bf26/bfthx.png`).
2. **„Népszerű kategóriák”:** 12 csempe. Az „Elektronika” kétszer szerepel benne.
3. **Képes blogkártyák (kicker):**
   - Vonalkövető – Az első projekted!
   - Fnirsi – Blog
   - Erősítők – Blog
   - V. Robot Exatlon – Blog
   - ESP – Blog
   - Arduino vagy ESP32?
   - Műszerdoboz tervezés
4. **„Videók”:** a kártyák címe „Hamarosan”, „OTTO robot” és „teszt 1”. **Ez helykitöltő, félkész tartalom.**
5. **„Blogok”:** 9 bejegyzés kivonata (lásd a 3. fejezetet).
6. **„Népszerű termékeink”:** 12 termék, villámnézettel, kívánságlista- és kosár gombbal.
7. **SEO-szöveg H1-ként:** „Arduino és ESP mikrovezérlők, ezekhez mindefnéle modulok és kijelzők…” (elírással). A lábléc fölött van egy **második H1** is.
8. **„Rólunk mondták”:** 5 vélemény keresztnévvel (Zoltán, Zsombor, Zoli, Zsolt, Ádám). Forrás nincs feltüntetve, és nem widgetből jönnek.
9. **GYIK-blokk** 4 kérdéssel.
10. **„Modulshop Átvevőhely”** címmel. Térkép nincs (nincs beágyazott Google Maps).
11. **Kapcsolat- és átvételipont-doboz.**

### Lábléc
- **„Keress minket bizalommal!”:** e-mail, telefon, átvételi pont címe és nyitvatartása.
- **Hírlevél-feliratkozás:** keresztnév, e-mail és GDPR-jelölőnégyzet.
- **„Információk” linklista:**
  - Ingyenes visszaküldés, Hűségpont rendszer, Regisztráció, Online elállás
  - MESTERSÉGES INTELLIGENCIA (AI) HASZNÁLATI SZABÁLYZAT, Gyakran ismételt kérdések
  - Adatvédelmi nyilatkozat, Vásárlási feltételek
  - ÁSZF (**ez a https://modulshop.hu/adatvedelem-45 oldalra mutat**)
  - Szállítási módok
- **Copyright:** „© 2019 - 2026-2023 modulshop - Elektronikai webáruház” (hibás évszámmal), mellette ShopRenter-logó.
- **Hiányzik a láblécből:** Kapcsolat, Rólunk és Blog link, közösségimédia-ikonok, fizetési és szállítási logók.

### Kategóriaoldal (példa: https://modulshop.hu/mikrovezerlok-alaplapok-157/esp32-205)
- Morzsamenü, H1, rövid kategórialeírás, alkategória-linkek („Az alábbi alkategóriákra kattintva…”), „Ugrás a terméklistára” link, a lista alatt hosszabb SEO-szöveg.
- **Szűrők** (az oldal minden változtatás után újratöltődik):
  - **Gyártó:** az ESP32-nél csak a „Modulshop (17)” érték jelenik meg a 43 termékből, ezért a szűrő gyakorlatilag használhatatlan.
  - **Ár:** minimum–maximum mező.
  - **„Raktárkészlet szűrő – Csak raktáron lévő termékek listázása”** (`?stockfilter=1`).
- **Rendezés** (`?sort=…&order=…`):
  - Név, A–Z / Z–A
  - Ár szerint növekvő / csökkenő
  - Értékelés, legjobb
  - Elérhetőség, legújabb
  - Legtöbbet vásárolt (`sort=bestseller`)
- **Lapozás:** 18 termék oldalanként, számozott oldalakkal (`?page=N`).
- **Termékkártya:** 210×210-es kép, név, bruttó ár, rövid leírás (specifikációs sorok), kívánságlista, mennyiség, „Kosárba” vagy „Értesítés” gomb, „Részletek”. Néhány listában a készlet is látszik („30 db raktáron”).
- **Oldalsávban „Legújabb termékek”** blokk.

### Keresés
- A találati oldal címe `https://modulshop.hu/index.php?route=product/list&keyword=esp32`, az „esp32” keresés 51 találatot adott.
- A találati oldalon van kategóriaválasztó („Minden kategória”), Gyártó- és Ár-szűrő, valamint ugyanaz a rendezés, mint a kategóriaoldalakon.
- A `https://modulshop.hu/kereses?search=…` cím üres „Keresés” oldalt ad.

### Analitika és mérés (a forráskódban látható)
- Google Tag Manager `GTM-PT3V3VB`, GA4 `G-SN91WR1F3L`
- Facebook Pixel `485146113799847`
- Hotjar

---

## 3. Tájékoztató és jogi oldalak

| Oldal | URL | A legfontosabb tények |
|---|---|---|
| Szállítási Információk | https://modulshop.hu/szallitasi-informaciok-65 | **Automatába:** Foxpost 1250 Ft, MPL 1250 Ft, GLS 1300 Ft. **Házhozszállítás:** MPL 1700 Ft, GLS 1950 Ft. **Csomagpontba / postára:** Posta 1400 Ft, GLS 2000 Ft. |
| Szállítási módok | https://modulshop.hu/szallitasi-modok-71 | **Személyes átvétel:** 1078 Budapest, Nefelejcs utca 43. (bejárat a Marek József utca felől; fehér műanyag ajtó, szuterén), csak online leadott rendelésre. Nyitvatartás: H–P 08:00–18:00, Sz–V 10:00–16:00. „Minden nagyobb futárcéggel szerződésben állunk: MPL, GLS, Foxpost (Packeta)”. Az automata „jelenleg … a legnépszerűbb és legolcsóbb”. Az árak itt is szerepelnek, de **a GLS automata ára itt 1350 Ft** (a másik oldalon 1300 Ft). |
| Gyakran ismételt kérdések | https://modulshop.hu/gyakran-ismetelt-kerdesek-36 | Az árak bruttók (ÁFA-val). Készleten lévő terméknél a kiszállítás 1–4 munkanap; az „értesítés” státuszú termékek átlagosan 14–45 nap alatt érkeznek be. Személyes átvétel a rendelés után azonnal (H–P 08–18, Sz–V 10–16). **1 év garancia minden termékre.** Előrendelés e-mailben; iskoláknak és cégeknek egyedi mennyiségi kedvezmény. |
| GYIK-blokk a főoldalon | https://modulshop.hu/ | A készlet a terméklapon valós raktárszámot mutat. Átvétel „azonnal … H-P: 08:00-19:00, Sz-V: 10:00-16:00” (**ellentmond a 08–18-nak**). „Nem” lehet helyben vásárolni, csak webáruházként üzemelnek. Több mint 50 vásárlói javaslatra felvett termék. |
| 30 napos termék-visszaküldés | https://modulshop.hu/30-napos-termek-visszakuldes-38 | Elégedetlenség esetén írásban az info@modulshop.hu címen jelezhető. A vásárlástól számított 30 napon belül „kérdés nélkül” visszatérítik a vételárat vagy cserélik a terméket. A visszaküldés és a csere költségét a bolt állja. |
| Ingyenes visszaküldés | https://modulshop.hu/ingyenes-visszakuldes-77 | Bármely okból ingyenesen visszaküldhető GLS automatán át. Linkkel generált kód (ecsomag.hu/hu/visszaru). |
| Hűségpont rendszer | https://modulshop.hu/husegpont-rendszer-85 | 2026. január 1-jétől, regisztrációhoz kötve. **Normál áras terméknél 5%** (20 Ft után 1 pont), **akciós terméknél 1%** (100 Ft után 1 pont). 1 pont = 1 Ft, a pénztárban váltható be. |
| Regisztráció | https://modulshop.hu/regisztracio-87 | „Miért érdemes regisztrálni?”: 5% hűségpont, amely beszámítható a szállítási költségbe is. Link: /customer/register. |
| Online elállás | https://modulshop.hu/withdrawal | Elállási űrlap: név, rendelésszám, e-mail, és hogy a teljes rendelésre vagy egyes tételekre vonatkozik. |
| ÁSZF | https://modulshop.hu/adatvedelem-45 (a slug félrevezető) | **Kereskedő:** Nováki József egyéni vállalkozó. **Székhely:** 1081 Budapest, Szilágyi utca 1/b fsz. 1. **Nyilvántartási szám:** 55371672. **Adószám:** 56696741-**2**-42. **Telefon:** 06 70 944 7641. **OKNYIR:** 306071/B/1. **Tárhely:** Shoprenter.hu Kft. A szállítási határidő legfeljebb 10 munkanap (ha raktáron van). 14 napos elállás (45/2014. Korm. rendelet). **Fizetés:** készpénz személyes átvételkor, utánvét, bankkártya (Barion), átutalás. |
| Adatvédelmi nyilatkozat | https://modulshop.hu/adatvedelmi-nyilatkozat-44 | Adatkezelő: Nováki József e.v. **Adószám itt: 56696741-1-42** (eltér az ÁSZF-től). Ugyanaz a nyilvántartási szám és OKNYIR, info@modulshop.hu, +36 70 944 7641. Adatfeldolgozók között szerepel a GLS Hungary Kft., a Barion Payment Zrt. és a Netsoft informatikai Kft. |
| Vásárlási feltételek | https://modulshop.hu/vasarlasi-feltetelek-5 | **Elavult sablonszöveg, amely ütközik az ÁSZF-fel:** 8 munkanapos elállást, a 17/1999. Korm. rendeletet, „kozmetikai termékeket”, DPD-s utánvétet, illetve „kizárólag Foxpost” szállítást említ. Szállítási módok és idők: GLS automata, csomagpont, házhoz (2 munkanap); MPL automata (2–3), postán maradó, házhoz (2); elsőbbségi ajánlott levél (2–3); Foxpost automata (3–4). Fizetés: átutalás, utánvét, Barion, készpénz. Külföldre nem szállítanak. |
| AI használati szabályzat | https://modulshop.hu/mesterseges-intelligencia-ai-hasznalati-szabalyzat-115 | Hatályos 2026. augusztus 1-jétől, 1.0-s verzió, az EU AI Act (2024/1689) alapján. Az AI-t belső, munkát támogató eszközként használják. |
| Kapcsolat | https://modulshop.hu/kapcsolat-32 | Átvételi pont: 1078 Budapest, Nefelejcs utca 43., bejárat a Marek József utca felől. H–P 8:00–18:00, Sz–V 10:00–16:00. info@modulshop.hu, „Tel: 0670- 944-7641”. **Nincs kapcsolati űrlap és térkép.** |
| Rólunk | https://modulshop.hu/rolunk-51 | Csak annyi áll rajta: „Hamarosan....” |
| Csomag ajánlataink | https://modulshop.hu/csomag-ajanlataink-101 | Üres oldal. |
| Projekt verseny | https://modulshop.hu/modulshop-projekt-verseny-79 | Lejárt verseny (jelentkezés 2024.06.26-tól, a záró dátum elgépelve: „20247.09.08”). Első díj: 50 000 Ft-os utalvány. Még benne van a sitemapben. |
| Blog: „Álmodd meg ötleted és valósítsd meg” | https://modulshop.hu/almodd-meg-otleted-es-valositsd-meg-2 | 9 bejegyzés: Műszerdoboz-tervezés, Vonalkövetés, ESP – Blog, FNIRSI, Erősítő modulok…, Robot Exatlon – Nyíregyháza, Dekoráció led szalaggal, Nodemcu autós kit, IRFZ44 Mosfet teszt Arduinóval. Címkék: ac-dc, dc-dc, D_I_Y_, konverter(ek). Egy bejegyzés slugja elrontott (`httpswwwmodulshophublogerosito-modulok-…`). A sitemapben további listák is vannak: `hirek-3`, `hasznos-dolgok-4`, `uj-termekeink-7`, `egyedi-muszerdobozok-10`, `arduino-vagy-esp32-99`. |

### Összefoglaló adatlap (a migrációhoz)

**Cég és elérhetőség**
- **Cégnév:** Nováki József egyéni vállalkozó (forrás: ÁSZF és adatvédelmi nyilatkozat).
- **Adószám:** 56696741-2-42 (ÁSZF) vagy 56696741-1-42 (adatvédelmi nyilatkozat). **A tulajdonossal tisztázni kell, melyik a helyes.**
- **Nyilvántartási szám:** 55371672. **OKNYIR:** 306071/B/1.
- **Székhely:** 1081 Budapest, Szilágyi utca 1/b fsz. 1.
- **Átvételi pont / raktár:** 1078 Budapest, Nefelejcs utca 43. (bejárat a Marek József utca felől, fehér műanyag ajtó, szuterén).
  - H–P 08:00–18:00, Sz–V 10:00–16:00. A főoldali GYIK 19:00-s zárást ír.
- **Telefon:** +36 70 944 7641. **E-mail:** info@modulshop.hu.

**Szállítás**
- **Módok:** személyes átvétel (ingyenes), Foxpost/Packeta automata, MPL automata/posta/házhoz, GLS automata/csomagpont/házhoz.
- **Díjak:** 1250–2000 Ft (lásd fent).
- **Ingyenes szállítási értékhatárt egyik oldalon sem találtunk.** A forrásban ugyan van egy „FreeShippingNanobar” modul, de nincs beállított értékhatár.
- A hűségpontokkal „lehet ingyen szállítás” (forrás: Regisztráció oldal).

**Fizetés:** bankkártya (Barion), utánvét, banki átutalás, készpénz személyes átvételkor.

**Garancia és elállás**
- 1 év garancia (forrás: GYIK).
- 14 napos elállás (forrás: ÁSZF).
- Önként vállalt 30 napos visszaküldés vagy csere, a bolt költségén (forrás: 30 napos oldal), és ingyenes GLS-automatás visszaküldés.

---

## 4. Bizalmi elemek és USP-k (az oldalon szereplő állítások)

| Állítás | Hol |
|---|---|
| „Magyarországi raktárkészlet. Nincs további vám és egyéb adóteher.” | Főoldal, lábléc feletti szöveg (https://modulshop.hu/) |
| „a délelőtt 10 óráig leadott megrendeléseket még aznap átadjuk a futárcégek számára” | Ugyanott |
| „A személyes átvétellel kért rendelések azonnal átvehetők a budapesti raktárunkban.” | Ugyanott és a GYIK-ben |
| Terméklapi ikonsor: „Villámgyors szállítás – 1 napon belül átadjuk a futárcégnek”, „Óriási raktárkészlet”, „Iskolákat, Intézményeket cégeket is kiszolgálunk”, „Segítünk ha elakadtál – Hívj vagy írj emailt” | Minden termékoldalon, pl. https://modulshop.hu/esp32-c3-szuper-mini-wifi-bt-50-usb-c-1789 |
| Kiszállítás 1–4 munkanapon belül, ha a termék raktáron van | GYIK |
| 1 év garancia minden termékre | GYIK |
| 30 napos, kérdés nélküli visszaküldés vagy csere, a bolt költségén, és ingyenes GLS-automatás visszaküldés | /30-napos-termek-visszakuldes-38, /ingyenes-visszakuldes-77 |
| 5%-os hűségpont regisztrált vásárlóknak | /husegpont-rendszer-85 |
| Iskoláknak és cégeknek mennyiségi kedvezmény, előrendelés | GYIK |
| „már több mint 50 olyan termék került fel amit vásárlóink ajánlottak” | Főoldali GYIK |
| A valós készlet darabra pontosan látszik („37 db raktáron”, „Utolsó 1 db raktáron”) | Termékoldalak |
| Saját fejlesztésű termékek („Fő terméktervezőnk és készítőnk: Bán Péter”), egyedi 3D-nyomtatott műszerdoboz e-mailes terv alapján | https://modulshop.hu/sajat-termekeink-244, a főoldali „Műszerdoboz – tervezés” blogkártya |
| „ár-érték arányban a legjobbak Magyarországon” / „a legjobb árakkal és gyors kiszállítással” | A kategórialeírás (/mikrovezerlok-alaplapok-157) és a meta description |
| Működés 2019 óta (csak a „© 2019 - …” copyrightból következtethető) | Lábléc |
| Oktatási jelenlét: Robot Exatlon (Nyíregyháza, általános iskolás verseny), projektverseny | Blog, /modulshop-projekt-verseny-79 |
| 5 vásárlói vélemény keresztnévvel („Rólunk mondták”) | Főoldal; forrás nincs feltüntetve |

**Ami nincs az oldalon:** cégalapítási történet, a készletméret konkrét száma (a katalógus mérete: 1811 termék, ebből 1019 raktáron), értékelési átlag, külső értékelési widget.

---

## 5. Arculat

### Logók
A fájlok a scratchpadban vannak: `/tmp/claude-0/-home-user-modulshop/bcb3e1a5-f441-5cd9-871a-229eb86095fe/scratchpad/site/brand/`.

| Fájl | Forrás URL | Méret | Megjegyzés |
|---|---|---|---|
| `logo-original.png` | https://modulshop.cdn.shoprenter.hu/custom/modulshop/image/data/Logo/logo350x80-3keret.png | 350×80, RGBA | A fejlécben használt logó. Egyszínű kék (#01598B) szöveg, áramkörös ikonnal, keretes. |
| `logo-header.webp` | …/image/cache/w350h80q100/Logo/logo350x80-3keret.png.webp | 350×80 | Ugyanez a logó WebP-ben, ahogy a fejléc betölti. |
| `Modulshop_logo-original.png` | https://modulshop.cdn.shoprenter.hu/custom/modulshop/image/data/Weboldal_frissites/Logo/Modulshop_logo.png | 540×300, RGBA, átlátszó | **Kétszínű, újabb változat:** a „Modul” türkiz (#0594AE), a „shop” sötétkék (#01598B), mellette áramkörös ikon. Ez az og:image. **A redesignhoz ezt javasoljuk.** |
| `logo-og.png` | https://modulshop.hu/custom/modulshop/image/cache/w220h100m00/Weboldal_frissites/Logo/Modulshop_logo.png | 220×100 | Az előző kicsinyített változata. |
| `favicon-loggo.png` | https://modulshop.cdn.shoprenter.hu/custom/modulshop/image/data/loggo.png | 1801×1801, RGBA | Csak az áramkörös ikon (fehér vonalak, #01598B lekerekített négyzet). Favicon és apple-touch-icon. |

### Színek
A téma CSS-változói a https://modulshop.hu/ inline stílusában vannak, a logó színei pixelanalízisből származnak.

| Szerep | Hex | Forrás |
|---|---|---|
| Elsődleges (fejléc/menü háttér, gombok, linkek) | `#273C99` | `--global-color`, `--button-color`, `--link-color`, `--footer-global-color` |
| Másodlagos / kiemelő sárga | `#FFCF0F` | `--secondary-color`, `--footer-secondary-color` |
| Szöveg sárga alapon / ár | `#121212` | `--text-on-secondary`, `--price-color` |
| Szöveg az elsődleges színen / gombon | `#FFFFFF` | `--text-on-global`, `--text-on-button` |
| Akciós ár | `#C00E28` | `--price-special-color` |
| Eredeti (áthúzott) ár | `#676767` | `--price-original-color` |
| Logó sötétkék | `#01598B` | logo PNG |
| Logó türkiz | `#0594AE` | Modulshop_logo.png |

> A téma kékje (#273C99) és a logó kékje (#01598B) eltér egymástól. A `docs/decisions.md` szerint új vizuális irány készül, és legfeljebb a logó marad meg. Ezért a palettát érdemes a logó két színére (#01598B, #0594AE) építeni.

### Betűtípus
- **Roboto** alap- és másodlagos betűként (`--hamburg-base-font-family`, `--hamburg-secondary-font-family`).
- A ShopRenter saját CDN-jéről töltődik woff2-ben (latin-ext, cirill, görög), nem a Google Fonts-ról.

---

## 6. A termékoldal felépítése

**Három példatermék:**
- **A)** https://modulshop.hu/esp32-c3-szuper-mini-wifi-bt-50-usb-c-1789
- **B)** https://modulshop.hu/zk-mt21-21-es-bluetooth-erosito-2x50w-100w
- **C)** https://modulshop.hu/inr18650-35e-li-ion-akku-3400-mah-samsung

| Adat | A) ESP32-C3 Szuper mini | B) ZK-MT21 2.1 erősítő | C) INR18650-35E akku |
|---|---|---|---|
| Morzsamenü / kategória | Mikrovezérlők, alaplapok › ESP32 | Erősítők › 100W fölötti + 2.1 | BMS-ek › Akku cellák, elemek |
| Cikkszám (SKU) | 1-2-29 | 5-2-13 | 6-5-10 |
| GTIN (microdata) | 5999572386689 | 5999572381134 | – |
| Ár (bruttó) | 1 900 Ft | 6 300 Ft | 1 950 Ft |
| Elérhetőség | „37 db raktáron” | „Szállítás alatt” (OutOfStock), gomb: **Értesítés** | „Szállítás alatt”, gomb: **Értesítés** |
| Rövid leírás | 4 spec-sor (IC, frekvencia, csatlakozó, memória) | Bekezdés (BT 5.0, AUX, 12–24 V, 2×50+100 W) | 9 spec-sor; a márka itt szöveges sorként: „Gyártó : Samsung” |
| Szerezhető hűségpont | 96 | 315 | 98 |
| Képek (galéria, 900×500) | 6 | 6 | 3 |
| Hosszú leírás | ~170 szó | ~560 szó, GYIK-szerű alcímekkel („Mi ez a termék pontosan?”) | ~800 szó |
| Vélemények | 0 | 2 | 1 |

**Minden termékoldalon megvan:**
- H1
- cikkszám
- elérhetőség darabszámmal
- rövid leírás
- hűségpont
- mennyiségválasztó és „Kosárba” gomb (ugyanez megismétlődik)
- USP-ikonsor
- fülek: „Leírás és Paraméterek” és „Vélemények”, véleményírás űrlappal (név, szöveg, 1–5 csillag)
- megosztás (Facebook, Twitter, Pinterest)
- schema.org microdata: Product, Offer, sku, gtin, availability, price, BreadcrumbList, Review

**Nincs a termékoldalakon** (39 letöltött termékoldal alapján):
- **Gyártó/márka mező.** A „Gyártó” szűrőben szinte csak a „Modulshop” érték szerepel, a valódi márka (Espressif, Samsung…) legfeljebb a leírás szövegében.
- **Strukturált spec-táblázat.** A paraméterek szabad szöveges sorok; 36-ból csak 1 oldalon volt `<table>`.
- **Adatlap-PDF.** Egyetlen `.pdf` link sem volt.
- **Kapcsolódó, ajánlott vagy kiegészítő termékek** blokk.
- **Variánsok.** A szín- vagy kiszerelésbeli változatok külön termékek, pl. „0,96" Oled kijelző/kék” (4-1-11) és „/Fehér” (4-1-21).
- **Akciós ár.** A mintában egyetlen akciós termék sem volt.
- **Várható szállítási dátum** és ingyenes szállítás sáv.

**Az SKU-séma:** `főkategória-alkategória-sorszám`, például 1-2-29 = Mikrovezérlők › ESP › 29. Egyes termékeknél ettől eltérő kód szerepel (pl. `YXS2299`). A képfájlok neve is az SKU-val kezdődik.

**Mintaadatkészlet:** `docs/research/products-sample.json`
- **36 termék**, mind raktáron, mind a 12 tényleges főkategóriából.
- **Kiválasztás:** alkategóriánként a „Legtöbbet vásárolt” rendezés és a „Csak raktáron” szűrő első 1–3 találata.
- **Mezők:** title, url, price_huf, compare_at_price_huf, sku, brand, category, image_url, short_description, in_stock, valamint stock_text, gtin és category_url.
- **brand:** csak ott van kitöltve, ahol az oldalon „Gyártó:” sor szerepel (a mintában 1 terméknél: ESPRESSIF); máshol `null`.
- **image_url:** az og:image (ShopRenter cache, 955×500 WebP). A képeket még nem töltöttük le.

---

## 7. Közösségi média és értékelések

- **Közösségimédia-profil linket egyik letöltött oldalon sem találtunk** (főoldal, 16 tájékoztató oldal, 56 kategóriaoldal, 39 termékoldal). Facebook-, Instagram-, YouTube- és TikTok-ikon sincs a fejlécben vagy a láblécben.
- **Ami megvan:**
  - Facebook Pixel (`485146113799847`).
  - Megosztó gombok (facebook.com/sharer, twitter.com/home, pinterest.com/pin/create).
  - A főoldal „Videók” blokkjában YouTube-beágyazás helye, de valódi videó nélkül („Hamarosan”, „teszt 1”).
- **Értékelési widget nincs:** nem találtunk Árukereső, Trustindex, Trustpilot vagy Google értékelés modult, sem Google Maps beágyazást.
- **Saját értékelések:**
  - A ShopRenter beépített termékértékelései (kevés: a példatermékeknél 0–2 db).
  - A főoldali „Rólunk mondták” 5 véleménye, forrásmegjelölés nélkül.
  - A vélemények valódiságát és forrását a `docs/research/reviews.md` fejezetben kell igazolni.
- A közösségi jelenlétet a webshopon kívül kell felderíteni (`docs/research/brand-and-presence.md`).

---

## 8. A jelenlegi oldal UX-problémái (prioritás szerint)

### P0 – bizalom, jog, konverzió
1. **Egymásnak ellentmondó jogi és üzleti adatok:**
   - két különböző adószám (…-2-42 és …-1-42);
   - az elállási idő a Vásárlási feltételekben 8 munkanap, az ÁSZF-ben 14 nap;
   - a Vásárlási feltételek kozmetikumokra hivatkozik, DPD-s utánvétet és „kizárólag Foxpost” szállítást ír;
   - a GLS automata ára 1300 vagy 1350 Ft;
   - a zárás 18:00 vagy 19:00.
   
   **Az új oldalon egyetlen, egységes ÁSZF, szállítási és kapcsolati forrás kell. Az adatokat a tulajdonossal jóvá kell hagyatni.**
2. **Félrevezető linkek és slugok:**
   - a lábléc „ÁSZF” linkje a `/adatvedelem-45` oldalra mutat;
   - a „Hűtőbordák, Ventilátorok” alkategória slugja `csatlakozok-vezetekek-202`;
   - a „Csomag ajánlataink” menüpont üres oldalra visz;
   - a GYIK kétszer szerepel a menüben.
3. **Félkész, helykitöltő tartalom élesben:**
   - „teszt 1”, „Hamarosan”, „OTTO robot” a Videók blokkban;
   - a Rólunk oldalon csak „Hamarosan....”;
   - lejárt 2024-es verseny;
   - hibás copyright („2019 - 2026-2023”).
4. **A főkategória-oldalak szinte üresek:** csak a közvetlenül hozzárendelt termékek látszanak (pl. a Mikrovezérlők oldalon 1 termék). Aki a főkategóriára kattint, azt hiheti, hogy nincs áru. **Shopifyon a főkollekció tartalmazza az alkollekciók termékeit is** (automatikus kollekció tag vagy típus alapján).
5. **A raktárhiány nincs kezelve:**
   - a katalógus kb. 44%-a nincs raktáron;
   - a főoldali „Népszerű termékeink” között is van nem rendelhető termék (ZK-MT21, INR18650-35E: „Szállítás alatt”; az ESP32-S3 N16R8 a listában „Értesítés” gombbal);
   - a listák alapértelmezésben nem a raktáron lévő termékeket mutatják előre.
   
   **Kell:** a raktáron lévők előre sorolása, látható készletjelvény, „értesítést kérek” funkció, és a kiemelt blokkok szűrése készletre.
6. **Nincs ingyenes szállítási értékhatár, vagy legalábbis sehol nincs kommunikálva,** és nincs kosárérték-sáv. Ha a bolt bevezet ilyet, a kosárban és a fejlécben jelezni kell.

### P1 – termékkeresés és termékadatok
7. **A gyártószűrő használhatatlan** (szinte minden termék „Modulshop”). Paraméter alapú szűrő sincs (feszültség, interfész, csatlakozó, teljesítmény). **Shopifyon metafield-alapú szűrők kellenek** (pl. platform: ESP32/Arduino/RP2040; tápfeszültség; interfész: I2C/SPI/UART; teljesítmény W). A valódi márkát vendor mezőbe kell tenni.
8. **A specifikációk szabad szövegként szerepelnek** a rövid leírásban, nem összehasonlítható táblázatban. Adatlap-PDF sincs. **Kell:** strukturált spec-táblázat (metafieldekből) és letölthető adatlap/pinout.
9. **Hiányzik a cross-sell,** pedig ennél a profilnál kulcsfontosságú (pl. ESP32 mellé breadboard, jumper kábel, tápegység; erősítő mellé tápegység, hangszóró). **Kell:** kapcsolódó és kiegészítő termékek blokk, valamint „gyakran együtt vásárolt” ajánlás.
10. **A variánsok külön termékek** (pl. Oled kék és fehér). **Shopifyon** egy termék legyen szín/kiszerelés variánssal, ahol ez értelmes.
11. **Elnevezési és nyelvi hibák a navigációban és a SEO-szövegben:**
    - „gyursulás”, „Komunikációs”, „nyáklapoK”, „mindefnéle”;
    - elavult menüszámlálók (Arduino 34 → 37, ESP8266 22 → 23);
    - inkonzisztens H1-ek, pl. a „Modulshop - Avr-diuno” vagy két különböző alkategória egyaránt „Erősítők” címmel;
    - a „2*50W” alkategória slugja `250w-…`.
12. **A szűrők minden változtatásnál újratöltik az oldalt,** és az oldalankénti 18 termék sok lapozást jelent egy 1800 termékes katalógusban.

### P2 – vizuális és tartalmi minőség, akadálymentesség
13. **A hero banner szöveges kép** alt szöveg és link nélkül. Az üzenet (feldolgozási késés) operatív közlemény, nem értékajánlat.
14. **Két H1 a főoldalon,** és a SEO-szöveg H1-ként jelenik meg.
15. **A termékképek 900×500-as fekvő formátumúak,** a kártyák 210×210-esek. A képarányok vegyesek, és a fájlnevek is (`.png`, `.jpg`, „_q50”).
16. **A „Kapcsolat” oldalon nincs űrlap, térkép és útvonalterv,** pedig a személyes átvétel fontos (szuterén, hátsó bejárat). Kell egy átvételi pont kártya térképpel és fotóval.
17. **Nincs Rólunk-történet, csapat és jól látható bizalmi sáv** (fizetési logók: Barion/kártya; futárlogók; garancia; 30 nap). Értékelési widget sincs.
18. **A lábléc hiányos:** nincs benne Kapcsolat, Rólunk, Blog link és közösségi ikon. A jogi és információs linkek ömlesztve vannak.
19. **A blog szét van szórva:** több listában van (`/almodd-meg-…`, `hirek-3`, `hasznos-dolgok-4`, `uj-termekeink-7`, …), elrontott sluggal, a kicker-kártyák egy része közvetlen URL-re, egy része a blogútvonalra mutat. **Shopifyon** egy blog legyen címkékkel (Projektek, Útmutatók, Hírek).
20. **Teljesítmény:** a főoldal HTML-je ~440 KB, 29 CSS-fájllal, 28 külső szkripttel, és GTM, GA4, FB Pixel és Hotjar fut rajta egyszerre. A Horizon-alapú újratervezésnél jóval könnyebb oldalt kell célozni.

### Megtartandó erősségek
- darabra pontos készletkijelzés;
- élő keresési javaslatok;
- „Legtöbbet vásárolt” rendezés;
- hűségpont rendszer;
- 30 napos és ingyenes visszaküldés;
- azonnali személyes átvétel;
- GYIK-stílusú, részletes termékleírások az újabb termékeknél (pl. ZK-MT21);
- SKU-alapú, következetes képfájlnevek;
- schema.org microdata (GTIN-nel).

---

## Nyitott kérdések a tulajdonosnak
1. Melyik a helyes adószám: 56696741-2-42 vagy 56696741-1-42?
2. Mi a helyes nyitvatartás (18:00 vagy 19:00) és a GLS automata ára (1300 vagy 1350 Ft)?
3. Lesz-e ingyenes szállítási értékhatár? Ha igen, mennyi?
4. Vannak-e hivatalos közösségimédia-profilok (Facebook, Instagram, YouTube, TikTok)? A webshopon egyik sem szerepel.
5. A „Vásárlási feltételek” oldal megszűnhet, és az ÁSZF lehet az egyetlen forrás?
6. Honnan származnak a „Rólunk mondták” vélemények (Google, Facebook)?
