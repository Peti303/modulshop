# modulshop.hu → Shopify migrációs csomag

- **Készült:** 2026-11-12. A tulajdonos engedélyével, a nyilvános oldalak sima `curl` letöltésével (bejelentkezés nélkül, legfeljebb 1 kérés/mp, saját, nem böngészőnek álcázott User-Agenttel).
- **Alapelv:** csak olyan tény került bele, ami a jelenlegi oldalon szerepel. Ahol a források ellentmondanak, ott mindkét adatot jelöltük, és a tulajdonosnak kell döntenie.

## A csomag tartalma

| Fájl | Mi ez |
|---|---|
| `products.csv` | Shopify termékimport a **36 mintatermékre**: 36 termék, 129 sor. A második képtől kezdve minden kép külön sorban van. |
| `scripts/shoprenter_to_shopify.py` | Konverter, csak standard könyvtárat használ. Bármilyen termék-URL-listából (a teljes katalógusból is) CSV-t készít, és előállítja a redirect-CSV-t. |
| `collections.md` | 12 főkollekció, 2 kiemelt és 39 alkollekció automatikus feltétellel, handle-lel, leírással és képjavaslattal. |
| `menus.md` | Főmenü (mega-menü) és a 3 lábléc-menü, pontos linkcélokkal. |
| `pages/*.html` + `pages.md` | 13 oldal tartalma és az index (handle, sablon-utótag). |
| `redirects.csv` | 1949 átirányítás. A sitemap mind az 1950 URL-jét lefedi, kivéve a főoldalt, mert annak nem kell átirányítás. |

---

## Importálási sorrend a Shopify adminban

### 0. Mielőtt bármit importálsz

- **A termékképek jelenleg a ShopRenter CDN-jén vannak** (`modulshop.cdn.shoprenter.hu/.../image/data/...`). A Shopify az importáláskor ezekről az URL-ekről tölti le a képeket. **A ShopRenter-előfizetést ezért csak a teljes termékimport után mondd fel.**
  - A 36 mintatermék mind a 129 eredeti kép-URL-jét HEAD-kéréssel ellenőriztük: mind HTTP 200-at adott.
- **Tesztelj először:** a mintacsomagot egy fejlesztői vagy próbaáruházban importáld. Csak azután futtasd a teljes katalógust.

### 1. Alapbeállítások

1. **Nyelv:** *Beállítások → Nyelvek*. Az áruház alapértelmezett (közzétett) nyelve legyen a **magyar**. A téma fordításai: *Online áruház → Témák → … → Nyelv szerkesztése*.
2. **Pénznem:** *Beállítások → Általános (Áruház adatai) → Áruház pénzneme* = **Magyar forint (HUF)**. Ezt az első rendelés előtt állítsd be.
3. **Áfa – fontos:**
   - *Beállítások → Adók és vámok*: Magyarország, **27% ÁFA**.
   - **Kapcsold be: „Az adó szerepeljen a termékárakban és a szállítási díjakban” (prices include tax).**
   - A `products.csv` minden ára (`Variant Price`) **bruttó, ÁFA-val együtt értendő HUF-ár**, ahogy a jelenlegi oldalon is („Az árak bruttóban értendők, tartalmazzák az ÁFÁ-t” – GYIK). E beállítás nélkül a Shopify még egyszer rászámolná a 27%-ot.
   - Minden termék `Variant Taxable = TRUE`.
4. **Egyéb:**
   - Időzóna: Budapest.
   - Mértékegység: metrikus, gramm.
   - Szállítási zóna: csak Magyarország. A régi „Vásárlási feltételek” szerint külföldre nem szállítanak. Ezt erősítsd meg.
5. **Szállítási díjak** (*Beállítások → Szállítás és kézbesítés*):
   - A díjak a `pages/szallitas-es-fizetes.html` szerint: Foxpost/MPL automata 1250 Ft, GLS automata 1300 vagy 1350 Ft (tisztázandó), MPL házhoz 1700 Ft, GLS házhoz 1950 Ft, posta 1400 Ft, GLS csomagpont 2000 Ft, személyes átvétel ingyen („Helyi átvétel”: 1078 Budapest, Nefelejcs u. 43.).
   - Automatás és csomagpontos szállításhoz szolgáltatói app (Foxpost/Packeta, GLS, MPL) kell.
6. **Fizetés** (*Beállítások → Fizetések*): a jelenlegi módok bankkártya (Barion), utánvét, banki átutalás és készpénz személyes átvételkor. Hogy a Barion vagy más szolgáltató legyen, azt a tulajdonos dönti el (lásd a kérdéseket).

### 2. Termékek – `products.csv`

1. *Termékek → Importálás → Fájl hozzáadása*: `products.csv`. Első importnál **ne** jelöld be a „Meglévő termékek felülírása azonos handle esetén” opciót.
2. **Ellenőrizd:** 36 termék, összesen 129 kép. A készlet az alapértelmezett helyszínre kerül (`Variant Inventory Qty`). A kézi ellenőrzés legyen szúrópróbás: ár, készlet, képek sorrendje és alt-szövegei.
3. **Mezők és szabályok:**
   - **Handle:** a régi URL-slug magyar ASCII-változata, a ShopRenter-azonosító nélkül. Például `/esp32-c3-szuper-mini-wifi-bt-50-usb-c-1789` → `esp32-c3-szuper-mini-wifi-bt-50-usb-c`.
     - Ahol a levágás után két termék handle-je egyezne, ott mindkettő megtartja a teljes régi slugot. Ilyen a kék és a fehér 0,96"-os OLED: `096-oled-kijelzokek-12864-i2c-733` és `-986`.
   - **Type** = főkollekció neve. **Tags** = alkategória-nevek (a vessző helyett „ / ” áll). A típust és a címkéket elsősorban a termékoldal morzsamenüje adja. Ha az csak „Összes termék”, akkor a kategórialistákból vett tagság (lásd 4. pont).
   - **Vendor** = „Modulshop”, kivéve ha a leírásban „Gyártó: X” sor van. A mintában: ESPRESSIF.
   - **Body (HTML):** a teljes leírás egyszerű szemantikus HTML-ként (`p`, `h2`–`h4`, `ul`/`ol`, `strong`, `table`). A ShopRenter-stílusok és -spanek ki vannak szedve, a „-” kezdetű sorokból lista lett. A rövid leírás csak akkor került a leírás elejére, ha a hosszúban nem szerepelt. A kiemelt paraméterek (pl. CPU, Antenna) listaként szerepelnek.
   - **Variant Inventory Qty** = a terméklap „N db raktáron” értéke 2026-11-12-én. Policy: `deny`, Tracker: `shopify`, Fulfillment: `manual`.
   - **Variant Barcode** = a GTIN a terméklap microdata-jából. Csak érvényes ellenőrző összegű GTIN került be. 2 terméknél a „GTIN” mezőben valójában cikkszám volt (YXS2299, 15-1-13), ezeknél üresen hagytuk.
   - **Image Src** = az eredeti feltöltött kép (`image/data/...`), nem a 900×500-as, fehér kerettel kitöltött cache-változat.
   - **SEO Title / SEO Description** = a régi `<title>` és meta description. Kivettük a „Modulshop - ” előtagot, a címben lévő árat és a „Rendelés/Készleten - Gyors kiszállítás” sablonszöveget. Ahol a meta description a ShopRenter árat tartalmazó alapsablonja volt („… most 700 Ft-os áron elérhető …”), ott üresen hagytuk, mert az ár elavulna.
   - **Szándékosan üres:**
     - `Product Category`: a Shopify szabványos taxonómiájához nem találtunk biztos megfeleltetést. Az adminban állítsd be, a Shopify javaslatot is ad.
     - `Variant Grams`: a régi oldalon nincs tömegadat.
     - `Variant Compare At Price`: a mintában nem volt akciós termék.
4. **Teljes katalógus** (később, szándékosan nem futtattuk le):
   ```bash
   cd docs/import
   python3 -I scripts/shoprenter_to_shopify.py products \
       --sitemap https://modulshop.hu/sitemap.xml --all-from-sitemap \
       --crawl-categories --verify-images \
       --cache-dir /tmp/modulshop-raw/products \
       --out products-full.csv --ids-out product_ids.json --report report.json
   python3 -I scripts/shoprenter_to_shopify.py redirects \
       --sitemap https://modulshop.hu/sitemap.xml --ids product_ids.json --out redirects.csv
   ```
   - **Időigény:** kb. 1856 termékoldal, kb. 150 kategórialista-oldal és a képellenőrzés. Másodpercenként 1 kéréssel ez nagyjából 1–2 óra.
   - **Cache:** a letöltött HTML a cache-be kerül, újrafuttatáskor nem tölti le újra. Élesítés előtt friss készlethez add hozzá a `--refresh` kapcsolót.
   - **`report.json`:** felsorolja a hibás GTIN-eket, az üres leírásokat és a típus nélküli termékeket. Típus nélküli termék akkor lesz, ha a morzsamenüben csak „Összes termék” áll, és egy kategórialistában sem szerepel.
   - **A redirect-CSV-t a teljes konvertálás után újra kell generálni a `product_ids.json`-nel:**
     - A mostani `redirects.csv` a 36 mintaterméknél a terméklap valódi azonosítóját használja.
     - A többi 1820 terméknél heurisztikát használ: a végén álló 3–4 jegyű, nem 0-val kezdődő számot tekinti azonosítónak.
     - A heurisztika néhol téved. Például a `rezgeserzekelo-modul-sw-420` slugban a 420 terméknév-rész.

### 3. Kollekciók – `collections.md`

- *Termékek → Kollekciók → Kollekció létrehozása → Automatikus*. A feltétel: „Terméktípus egyenlő …”, illetve „Termékcímke egyenlő …”.
- Összesen 53 kollekció: 12 fő-, 2 kiemelt és 39 alkollekció. A handle-t a „Keresőmotoros előnézet” részben add meg, mert a menü és az átirányítások erre épülnek.
- A leírásokat és a képeket a `collections.md` tartalmazza.

### 4. Oldalak – `pages/*.html`, `pages.md`

1. *Online áruház → Oldalak → Oldal hozzáadása*. A címet és a handle-t a `pages.md`-ből vedd.
2. A tartalmat HTML-nézetben (`<>`) illeszd be. **A fájl eleji `<!-- … -->` megjegyzést ne másold be**, az a tulajdonosnak szól: ellentmondások, kitöltendő `[[…]]` helyek, források.
3. **Sablon hozzárendelése** (*Téma sablon*):

   | Oldal | Sablon |
   |---|---|
   | rolunk | `page.about` |
   | kapcsolat | `page.contact` |
   | gyik | `page.faq` |
   | szallitas-es-fizetes, garancia-es-visszakuldes | `page.shipping` |
   | iskolaknak-es-cegeknek | `page.b2b` |
   | aszf, adatvedelem, impresszum, elallas, ai-hasznalati-szabalyzat | `page.legal` |
   | husegpont, sajat-termekeink | alapértelmezett |

   A hiányzó sablonokat előbb a témaszerkesztőben hozd létre.
4. A **TERVEZET** oldalak (rolunk, iskolaknak-es-cegeknek) és a husegpont maradjanak **rejtettek**, amíg a tulajdonos jóvá nem hagyja őket, illetve amíg a hűségpont-app nem működik.
5. Ajánlott a Shopify beépített szabályzatait is kitölteni (*Beállítások → Szabályzatok*: visszatérítés, adatvédelem, szolgáltatási feltételek, szállítás, jogi közlemény), az ÁSZF és az adatvédelmi szöveg alapján. A pénztár ezekre linkel.

### 5. Menük – `menus.md`

*Online áruház → Navigáció*:
- a `main-menu` 3 szinten: Termékek → főkollekció → alkollekció;
- 3 lábléc-menü: `vasarlas`, `informaciok`, `jogi`.

A menüket a kollekciók és az oldalak után hozd létre, hogy a linkek kiválaszthatók legyenek.

### 6. Átirányítások – `redirects.csv`

*Online áruház → Navigáció → URL-átirányítások → Importálás* (az adminban az „URL redirects” keresőszóval is megtalálod).

- **Formátum:** `Redirect from,Redirect to`, relatív útvonalakkal. **1949 sor:**
  - 1856 termék → `/products/<handle>`;
  - 56 kategória- és gyártó-URL → `/collections/<handle>`, köztük az „Összes termék” → `/collections/all` és a „Modulshop” gyártóoldal → `/collections/vendors?q=Modulshop`;
  - 2 lekérdezési paraméteres terméklista (`/index.php?route=product/list&latest=52` és `&special=1`) → `/collections/all`. Ha az import ezeket elutasítja, hagyd ki őket;
  - 13 információs oldal → `/pages/<handle>`;
  - `/kereses` → `/search`, `/regisztracio-87` → `/account/register`;
  - 6 bloglista → `/blogs/news`;
  - 14 blogcikk-URL (13 különböző cikk) → `/blogs/news/<handle>`.
- **Az átirányítások csak akkor működnek, ha a modulshop.hu domain már a Shopify-ra mutat.**
- **Blogcikkek:** a blog tartalmát ez a csomag nem viszi át. A cikkeket a Shopify „news” blogjába **ezekkel a handle-ökkel** kell létrehozni:
  - `modulshop-projekt-verseny`
  - `nodemcu-autos-kit-wifi-iot`
  - `dekoracio-led-szalaggal`
  - `erosito-modulok-elektronikai-projektekhez`
  - `esp32-mi-az-es-hogyan-mukodik`
  - `fnirsi-meromuszerek-oszcilloszkopok-teszterek`
  - `irfz44-mosfet-teszt-arduinoval`
  - `egyedi-muszerdoboz-tervezes`
  - `robot-exatlon-nyiregyhaza-altalanos-iskolas-verseny`
  - `vonalkoveto-robot-arduino-alapok`
  - `soft-starter-kicsi-egyszeru-es-hatekony`
  - `tankbot-v10`
  - `raspberry-pi-pico2`

  Két régi URL ugyanarra a NodeMCU-cikkre mutat (`-58` és `-60`). A hibás `httpswww…` és `httpsmodulshophu…` slugok helyett tiszta handle-t adtunk.

### 7. Keresés és szűrés – Search & Discovery app

Telepítsd a Shopify **Search & Discovery** alkalmazást, majd *Szűrők*:

| Szűrő | Forrás | Megjegyzés |
|---|---|---|
| Elérhetőség | Availability | A régi oldalon is volt „Csak raktáron lévő termékek”. A termékek kb. 44%-a nincs raktáron. |
| Ár | Price | Tartományszűrő. |
| Terméktípus | Product type | = főkollekció. Az „Összes termék” és a keresési találatok oldalán hasznos. |
| Címke | Tag | = alkategória. Kollekcióoldalon az alkategóriák közti szűkítésre. Ha később más célú címkék is lesznek (pl. „Saját termék”), a Search & Discovery-ben csoportosítsd vagy rejtsd el őket. |

Később, ha a valódi gyártók is bekerülnek: **Gyártó (Vendor)**. Ma szinte minden termék „Modulshop”, ezért ez a szűrő még nem hasznos. Ha a paraméterek metamezőkbe kerülnek (feszültség, interfész, csatornaszám…), azokra is lehet szűrőt tenni.

### 8. Élesítés előtt

1. Friss készlet: a konvertert `--refresh` kapcsolóval futtasd, és importálj felülírással.
2. Állítsd be a domaint, utána ellenőrizd 10–20 régi URL átirányítását.
3. Pótold a „Értesítés” (újra raktáron) funkciót. Shopify alatt ehhez app kell.
4. Ha a hűségpont-rendszer megmarad, ahhoz is app kell.

---

## Adatminőségi megfigyelések (a mintából)

- **Csak „Összes termék” a morzsamenüben:** 4 terméknél (W3230 termosztát, DT-830B multiméter, NE555–CD4017 készlet, Led panel 8 db) a morzsamenü csak „Összes termék”. A típust a kategórialistából vettük (`--category-hints`, a mintaadatok `category_url` mezőjéből). A teljes katalógusnál erre szolgál a `--crawl-categories` kapcsoló.
- **Feltehetően rossz kategóriák:** az „ESP32 - Cam” az ESP8266 alkategóriában van, az AC 220V 2000W szabályzó a „DC-DC step down” alkategóriában. Részletek: `collections.md`.
- **Több alkategória:** az XY-E30H két alkategóriában is szerepel („2*50W” és „100W fölötti + 2.1”). Mindkét címkét megkapta.
- **Nem a termékhez illő meta description:** az „INR18650-33VA Li-ion akku 3200 mAh” meta descriptionje egy másik cellát ír le („Samsung INR18650-35E … 3500 mAh”). A 18650-es töltőmodul címe „usb-C”, a meta descriptionje „micro usb”. A meta descriptiont változatlanul átvettük, javítsd.
- **Elírás a SEO-címben:** az RFID tag SEO-címe „Roxy, tag, 13,56 MHz” (helyesen: Proxy).
- **Üres leírás:** a „Fémházas ónszippantó” hosszú leírása üres, a CSV-ben csak a rövid leírás szerepel.
- **Variánsok:** a szín szerinti változatok külön termékek (pl. az OLED kék/fehér). Ha variánssá vonod össze őket, a handle-ök és az átirányítások is változnak.

---

## Nyitott kérdések a tulajdonosnak

1. **Adószám:** melyik a helyes? Az ÁSZF-ben 56696741-**2**-42, az Adatvédelmi nyilatkozatban 56696741-**1**-42 áll. A projektverseny szabályzatában egy harmadik, 26536077-2-42 szerepel, „cégjegyzékszám: 01-09-330843” mellett. Ez utóbbi melyik vállalkozásé?
2. **Nyitvatartás:** hétköznap 18:00-ig vagy 19:00-ig? A főoldali GYIK 19:00-t ír, a többi oldal 18:00-t. Melyik a helyes bejárat-leírás: „Marek József utca felől, szuterén” vagy „az épület főbejárata mellett”?
3. **GLS automata díja:** 1300 Ft vagy 1350 Ft?
4. **Ingyenes szállítás:** lesz-e ingyenes szállítási értékhatár? Ha igen, mennyi?
5. **ÁSZF 15.2:** a szöveg szerint elálláskor a visszaküldés költségét a vásárló viseli. Ez ütközik az „Ingyenes visszaküldés” és a 30 napos vállalással. Melyik érvényes? Az ÁSZF-et ehhez igazítani kell.
6. **Telefonszám:** az ÁSZF panaszkezelési pontjában „06 31 781 5157” áll. Él még ez a szám, vagy csak a 06 70 944 7641 a helyes?
7. **Vásárlási feltételek:** a régi oldal (8 munkanap, 17/1999. rendelet, „kozmetikai termékek”, DPD) megszűnhet, és az ÁSZF lehet az egyetlen forrás? Mi így készítettük elő: átirányítás az ÁSZF-re.
8. **Platformváltás a jogi szövegekben:**
   - Ki legyen a fizetési szolgáltató (Barion vagy Shopify Payments, illetve más)?
   - Az ÁSZF-ben a tárhelyszolgáltatót és a fizetési részt, az Adatvédelmi nyilatkozatban az adatfeldolgozókat (Shopify, appok) frissíteni kell. Ki nézi át jogilag?
   - Érvényes-e még az onlinePénztárca-kupon (ONLINE GROUP Kft.) és az „M.I. Solution Kft.” mint adatkezelő?
9. **Online elállási funkció:** a régi `/withdrawal` űrlap helyett milyen megoldás legyen? Az (EU) 2023/2673 irányelv szerint 2026. június 19-től elállási funkció kötelező lehet, ezt jogásszal ellenőrizd.
10. **Rólunk oldal:**
    - Jóváhagyod a tervezetet?
    - Valóban 2019 óta működik a bolt? Ezt csak a copyright-sorból tudjuk.
    - Közzétehető Bán Péter neve? A régi oldalon szerepelt.
11. **Iskoláknak és cégeknek oldal:** mekkora a mennyiségi kedvezmény, és mi a feltétele? Van-e halasztott fizetés, díjbekérő vagy árajánlatkérő űrlap?
12. **Hűségpont:** marad-e, és melyik appal? Melyik szabály érvényes: „5% normál / 1% akciós”, vagy „minden forint után 5%”?
13. **Tömegadatok:** vannak-e tömegadatok (`Variant Grams`)? A súlyalapú szállítási díjhoz kellenének.
14. **Gyártók:** van-e gyártó-/márkalista? Ma szinte minden termék „Modulshop”, a valódi márka (Espressif, Samsung…) csak a leírásban szerepel.
15. **Kategóriák:**
    - Átsoroljuk-e a hibásan kategorizált termékeket (lásd fent)?
    - Szétosszuk-e az „Egyéb” 141 és az „Egyéb Modulok” 33 közvetlen termékét?
    - Legyen-e a színváltozatokból Shopify-variáns?
16. **Közösségi média:** vannak-e hivatalos profilok (Facebook, Instagram, YouTube, TikTok)? Ha igen, a láblécbe kerülnek.
17. **„Rólunk mondták” vélemények:** honnan származnak (Google, Facebook)? Csak ellenőrizhető forrással vigyük át.
18. **Blog:** ki és mikor viszi át a 13 blogcikket? A lejárt 2024-es projektverseny cikkként maradjon, vagy törölhető?
19. **Időzítés:** mikor mondható fel a ShopRenter? Csak a teljes termékimport után, mert a képek a ShopRenter CDN-jéről töltődnek.

---

## Ami nem sikerült vagy nincs benne

- **Termékkategória:** a `Product Category` (Shopify-taxonómia) üres. Biztos megfeleltetés nélkül nem töltöttük ki.
- **Csak a minta:** a teljes katalógust szándékosan nem konvertáltuk. A blogcikkek tartalma sincs benne.
- **Kollekcióképek:** a javasolt képek URL-jeit nem töltöttük le. A bannerek cache-URL-ként szerepelnek, a többinél csak a termék nevét adtuk meg.
- **Átmeneti hiba:** a futtatás közben egyetlen képellenőrzés kapott átmeneti „connection reset” hibát. Újrapróbálva HTTP 200 lett, a végső CSV-ben nincs hibás kép.
