# Kollekciók (Shopify automatikus kollekciók)

- **Forrás:** a modulshop.hu kategóriaoldalai (H1, kategórialeírás, termékszám), letöltve 2026-11-12-én. Az alkategóriák termékszámát a kategóriaoldal „1 - 18 / N termék” számlálójából vettük.
- **Felvétel módja:** Shopify admin → *Termékek → Kollekciók → Kollekció létrehozása* → Kollekció típusa: **Automatikus** → „A termékeknek **bármelyik** feltételnek meg kell felelniük”.
- **Feltételek:**
  - Főkollekció: **Terméktípus = X**. A `products.csv` `Type` oszlopa pontosan ezt az értéket kapja.
  - Alkollekció: **Termékcímke = Y**. A `Tags` oszlop ezt kapja.
- Ugyanezek az értékek vannak a `scripts/shoprenter_to_shopify.py` `MAIN` / `SUB` / `FEATURED` táblájában. Ha valamelyiket átírod, a kettőt együtt módosítsd.
- **Kollekció-handle:** a régi URL-slug magyar ASCII-változata, ShopRenter-azonosító nélkül. Ahol a régi slug félrevezető volt (pl. `egyeb-176`, `csatlakozok-vezetekek-202`), ott a név alapján képeztük.
- **Leírások:** a jelenlegi kategórialeírásokból készültek. Javítottuk a nyilvánvaló elírásokat. Kivettük a navigációs sort („Az alábbi alkategóriákra kattintva…”), a kulcsszóhalmozó sorokat (pl. „Modulshop.hu - elektronika - …”) és a beágyazott bannerképet. **Új állítást nem írtunk bele.** Ahol a régi oldalon nincs leírás, ott ezt jelezzük. Azokat a tulajdonos írja meg.
- **Javasolt kép:**
  - Főkollekciónál a régi kategóriabanner, ha van. A banner 970×300-as kép, szöveg lehet rajta, ezért előbb nézd meg.
  - Ahol nincs banner, ott a főoldali „Népszerű kategóriák” csempe képét javasoljuk.
  - Alkollekciónál annak a terméknek a főképét javasoljuk, amely a „Legtöbbet vásárolt” rendezésben (raktáron lévő termékek között) az első. Ahol ilyen rendezést nem töltöttünk le, ott az alapértelmezett lista első termékét.
- **Címkék írásmódja:** a Shopify-címkében nem lehet vessző, ezért a vesszőt „ / ” jelre cseréltük. A régi neveken a következő elírásokat javítottuk:
  - „gyursulás” → „gyorsulás”
  - „Komunikációs” → „Kommunikációs”
  - „nyáklapoK” → „nyáklapok”
  - „MosFet” → „MOSFET”
  - „fesz.” → „feszültség”

  A régi „Egyéb” alkategória a BMS alatt a saját H1-e szerint „BMS kiegészítők” címkét kapott, hogy ne keveredjen az „Egyéb” főkollekcióval.

> **Figyelem:** Egy termék a ShopRenterben több kategóriában is szerepelhet. A konverter a termékoldal morzsamenüjéből (elsődleges kategória) képzi a típust és a címkét. Ha a termék több alkategóriában is szerepel, azt csak a kategórialisták bejárása mutatja meg (`--featured-category <útvonal>`, ez a kapcsoló tetszőleges kategóriára ismételhető). A teljes katalógus átvitelénél ezért érdemes az összes alkategóriát is megadni (kb. 150 kérés).

---

## 1. Főkollekciók (12)

| # | Kollekció neve | Handle | Feltétel | Régi URL | Termék (becsült) |
|---|---|---|---|---|---|
| 1 | Mikrovezérlők, alaplapok | `mikrovezerlok-alaplapok` | Terméktípus = `Mikrovezérlők, alaplapok` | /mikrovezerlok-alaplapok-157 | ~117 |
| 2 | Szenzor Modulok | `szenzor-modulok` | Terméktípus = `Szenzor Modulok` | /szenzor-modulok-158 | ~121 |
| 3 | Egyéb Modulok | `egyeb-modulok` | Terméktípus = `Egyéb Modulok` | /egyeb-modulok-159 | ~316 |
| 4 | Erősítők, Végfokok | `erositok-vegfokok` | Terméktípus = `Erősítők, Végfokok` | /erositok-vegfokok-160 | ~156 |
| 5 | LCD-k, Kijelzők | `lcd-k-kijelzok` | Terméktípus = `LCD-k, Kijelzők` | /lcd-k-kijelzok-161 | 50 |
| 6 | BMS-ek, 18650 Akkuk | `bms-ek-18650-akkuk` | Terméktípus = `BMS-ek, 18650 Akkuk` | /bms-ek-18650-akkuk-162 | ~196 |
| 7 | DC, AC konverterek | `dc-ac-konverterek` | Terméktípus = `DC, AC konverterek` | /dc-ac-konverterek-163 | ~134 |
| 8 | Műszerek | `muszerek` | Terméktípus = `Műszerek` | /muszerek-164 | ~109 |
| 9 | Egyéb | `egyeb` | Terméktípus = `Egyéb` | /egyeb-165 | ~196 |
| 10 | Elektronika | `elektronika` | Terméktípus = `Elektronika` | /elektronika-177 | ~652 |
| 11 | D.I.Y. Készletek | `diy-keszletek` | Terméktípus = `D.I.Y. Készletek` | /diy-keszletek-225 | ~82 |
| 12 | Led világítás | `led-vilagitas` | Terméktípus = `Led világítás` | /led-vilagitas-197 | 54 |

A kollekció **címe** (amit a vásárló lát) később átírható, például „Szenzormodulok” vagy „DIY készletek”. A feltétel nem a címhez, hanem a terméktípushoz kötődik, ezért az átírás nem rontja el a kollekciót.

### Leírások és javasolt képek (főkollekciók)

**1. Mikrovezérlők, alaplapok**
> A Modulshop mikrovezérlői ár-érték arányban a legjobbak Magyarországon. Arduino, ESP, STM és sok más kínálatunk mellett rengeteg kiegészítőt is találsz. Folyamatosan bővülő termékpalettánkon megtalálsz mindent, amire csak szükséged van.

Kép: régi banner – https://modulshop.hu/custom/modulshop/image/cache/w970h300q100np1/bannerek/Mikrovezerlok_alaplapok_kategoria_kep.png (csempekép: Beetle Leonardo).
*Megjegyzés: az „ár-érték arányban a legjobbak Magyarországon” a régi oldal állítása. Hirdetésben csak akkor használd, ha alá tudod támasztani.*

**2. Szenzor Modulok**
> Webáruházunk egyik legszélesebb választékával a szenzormodulok rendelkeznek. Hőmérséklet-, pára- és nyomás-, feszültség-, áram- és távolság-, valamint fény-, mozgás-, giroszkóp-, gyorsulás- és RFID-érzékelő modulok közül válogathattok.

Kép: régi banner – …/bannerek/szenzor_modulok_kateg_kep.png

**3. Egyéb Modulok**
> Folyamatosan bővülő kategóriánkban jelenleg beviteli eszközökkel, kommunikációs modulokkal és motorvezérlőkkel találkozhattok.

Kép: régi banner – …/bannerek/egyeb_modulok_kateg_kep.png

**4. Erősítők, Végfokok**
> Nagy teljesítményű erősítők és végfokok audió kiegészítőkkel megspékelve, mindenkinek, aki érdeklődik a hangtechnika iránt.

Kép: régi banner – …/bannerek/erositok_vegfokok_kategoria_kep.png

**5. LCD-k, Kijelzők**
> *Nincs szöveges leírás a régi oldalon (csak banner).* Megírandó.

Kép: régi banner – …/bannerek/jo_Lcd_kateg_kep.png

**6. BMS-ek, 18650 Akkuk**
> Kategóriánkban akkutöltőket, 1S–13S BMS-eket és a hozzájuk tartozó kiegészítőket találod.

Kép: régi banner – …/bannerek/BMS_kateg_kep.png

**7. DC, AC konverterek**
> Webáruházunk DC és AC konverterei. Alkategóriák: AC-DC tápegységek, DC-DC step down (feszültségcsökkentő) és DC-DC step up (feszültségnövelő) konverterek.

Kép: régi banner – …/bannerek/dc_ac_kateg_kep.png
*Megjegyzés: a régi szöveg csak a két DC-DC alkategóriát sorolta fel. Az AC-DC tápegységek alkategória is létezik, ezért az felkerült a felsorolásba.*

**8. Műszerek** – *Nincs leírás a régi oldalon.* Kép: a legkelendőbb termék, a W3230 Termosztát 230 voltos főképe.

**9. Egyéb** – *Nincs leírás a régi oldalon.* Kép: a Kék hőálló szilikon szerelőalátét főképe.
*Javaslat: a 141 közvetlenül ide sorolt terméket érdemes áttekinteni és szétosztani (lásd site-analysis.md).*

**10. Elektronika** – *Nincs szöveges leírás (csak banner).* Kép: régi banner – …/bannerek/joElektronika_kateg_kep.png

**11. D.I.Y. Készletek** – *Nincs leírás a régi oldalon.* Kép: a főoldali csempekép (`tank1.jpg`) vagy a legkelendőbb termék, a NE555–CD4017 piros-kék LED villogó forrasztókészlet főképe.

**12. Led világítás** – *Nincs leírás a régi oldalon.* Kép: a kategória első termékének képe.
*Megjegyzés: a régi oldal ebben a kategóriában az „AC 220V 2000W Teljesítmény-, fény-, motor sebesség szabályzó” terméket mutatja elsőnek.*

(A „…/bannerek/” rövidítés teljes alakja: `https://modulshop.hu/custom/modulshop/image/cache/w970h300q100np1/bannerek/`.)

---

## 2. Kiemelt kollekciók (címke alapján)

| Kollekció neve | Handle | Feltétel | Régi URL | Termék |
|---|---|---|---|---|
| Általunk készített termékek | `sajat-termekeink` | Termékcímke = `Saját termék` | /sajat-termekeink-244 | 6 |
| Csomagok | `csomagok` | Termékcímke = `Csomag` | /csomagok-190 (és /csomag-ajanlataink-242 → ide irányít) | 15 |

- **Általunk készített termékek:**
  > Általunk készített, tervezett vagy gyártott termékeket találhatsz itt. Fő terméktervezőnk és készítőnk: Bán Péter.

  Kép: a főoldali csempe képe (`sziv_nyak/promo_kep.png`). Részletes bemutatás: a `pages/sajat-termekeink.html` oldal.
- **Csomagok:**
  > *A régi leírás csak kulcsszavakból állt („Modulshop - aurdino - mikrovezérlő - ESP -BMS - erősítő - Audió - hangtechnika - Csomagban”).* Megírandó.

  Kép: a „LM317 Állítható tápegység D.I.Y készlet” főképe.

Ezek a címkék a konverterben csak akkor kerülnek fel, ha futtatáskor megadod a kategóriát (`--featured-category /sajat-termekeink-244 --featured-category /csomagok-190`). A mintafuttatásnál ezt megadtuk, de a 36 mintatermék közül egyik sincs ezekben a kategóriákban.

Az „Összes termék” (/osszes-termek-191) helyett a Shopify beépített `/collections/all` oldala szolgál. A „Modulshop” gyártóoldal (/modulshop-m-32) helyett a `/collections/vendors?q=Modulshop` oldal.

---

## 3. Alkollekciók

| Főkollekció | Alkollekció neve (= címke) | Handle | Feltétel | Régi URL | Termék | Leírás (tisztítva) | Javasolt kép |
|---|---|---|---|---|---|---|---|
| Mikrovezérlők, alaplapok | Arduino | `arduino` | Termékcímke = `Arduino` | /mikrovezerlok-alaplapok-157/avr-duino | 37 | A Modulshop AVR mikrovezérlői 100%-osan kompatibilisek az Arduino alaplapjaival. Az Uno, Nano, Pro Micro és Leonardo mellett sok más fejlesztőpanelt is megtalálsz a shopban. Termékeinkre maximális csere garanciát vállalunk! | Nano V3.0, USB-C (beforrasztott pin) |
| Mikrovezérlők, alaplapok | ESP8266 | `esp8266` | Termékcímke = `ESP8266` | /mikrovezerlok-alaplapok-157/esp-167 | 23 | Az ESP talán a legtöbb projekt alapja, ezért igyekszünk biztosítani, hogy megtaláld, amit keresel, bármire is van szükséged. | ESP32 - Cam 8 MB ram… ⚠ |
| Mikrovezérlők, alaplapok | ESP32 | `esp32` | Termékcímke = `ESP32` | /mikrovezerlok-alaplapok-157/esp32-205 | 43 | ESP32 alaplapok. | ESP32-C3 Szuper mini |
| Mikrovezérlők, alaplapok | STM | `stm` | Termékcímke = `STM` | /mikrovezerlok-alaplapok-157/stm-168 | 4 | *nincs (csak kulcsszósor)* | STM32F401CCU6 V3.0, usb-c |
| Mikrovezérlők, alaplapok | Raspberry | `raspberry` | Termékcímke = `Raspberry` | /mikrovezerlok-alaplapok-157/raspberry-208 | 9 | Raspberry alaplapok. | Raspberry Pi PICO usb-c |
| Szenzor Modulok | Hőmérséklet / pára / nyomás | `homerseklet-para-nyomas` | Termékcímke = `Hőmérséklet / pára / nyomás` | /szenzor-modulok-158/homerseklet-para-nyomas-184 | 31 | Hőmérséklet-, pára- és nyomásérzékelő szenzormodulokon felül nagyon sok kiegészítővel találkozhattok, többek között eső- és hóérzékelő panellel. | DHT11 Hőmérséklet és páratartalom érzékelő modul |
| Szenzor Modulok | Feszültség / áram / távolság | `feszultseg-aram-tavolsag` | Termékcímke = `Feszültség / áram / távolság` | /szenzor-modulok-158/feszultseg-aram-tavolsag-185 | 37 | Feszültség-, áram- és távolságérzékelő szenzormodulokon felül nagyon sok kiegészítővel találkozhattok, többek között Hall-szenzorral. | RCWL-0516 Mikrohullámú radaros mozgásérzékelő modul |
| Szenzor Modulok | Fény / mozgás / giro / gyorsulás / RFID érzékelés | `feny-mozgas-giro-gyorsulas-rfid` | Termékcímke = `Fény / mozgás / giro / gyorsulás / RFID érzékelés` | /szenzor-modulok-158/feny-mozgas-erzekeles-186 | 49 | Közkedvelt szenzormoduljainkon belül itt fény-, mozgás-, giroszkóp-, gyorsulás- és RFID-érzékelő modulokkal találkozhattok. | MFRC-522 RC522 RFID Író/olvasó szett |
| Egyéb Modulok | Beviteli eszközök | `beviteli-eszkozok` | Termékcímke = `Beviteli eszközök` | /egyeb-modulok-159/beviteli-eszkozok-189 | 44 | Egyéb moduljainkon belül a beviteli eszközök. Ebben a kategóriában többek között kártyaolvasók, shieldek és nyomógombok találhatók. | Micro SD kártya író-olvasó modul |
| Egyéb Modulok | Kommunikációs modulok | `kommunikacios-modulok` | Termékcímke = `Kommunikációs modulok` | /egyeb-modulok-159/komunikacios-modulok-187 | 64 | Ebben a kategóriában találhatók a kommunikációs modulok, többek között adóvevő modul, GPS-modul és sok más. | Antenna 2.4 Ghz WiFi Bluetooth, ZigBee SMA to IPEX |
| Egyéb Modulok | Motor / DC / léptető / szervó | `motor-dc-lepteto-szervo` | Termékcímke = `Motor / DC / léptető / szervó` | /egyeb-modulok-159/motork-dc-lepteto-szervo-192 | 47 | Kategóriánk folyamatosan bővül az újonnan érkező termékekkel. Léptetőmotor-vezérlőkkel és szervókkal találkozhattok itt. | MG90S Szervo motor 180° |
| Egyéb Modulok | Motorvezérlők | `motorvezerlok` | Termékcímke = `Motorvezérlők` | /egyeb-modulok-159/motor-vezerlok-188 | 27 | Webáruházunk motorvezérlői: shieldek, motorvezérlők és léptetőmotorok várják az érdeklődőket! | DC Motor vezérlő fordulatszámszabályzó, 150W |
| Egyéb Modulok | Próbapanelek / shieldek / egyéb | `probapanelek-shieldek` | Termékcímke = `Próbapanelek / shieldek / egyéb` | /egyeb-modulok-159/probapanelekshieldekegyeb-196 | 52 | *nincs* | Tüskesor 40 pin egyenes 2,54 mm |
| Egyéb Modulok | Relék / optocsatolók | `relek-optocsatolok` | Termékcímke = `Relék / optocsatolók` | /egyeb-modulok-159/relek-211 | 49 | Relémodulok: hagyományos, behúzótekercses és szilárdtest relék. | Relé modul 1 portos 5V/220V |
| Erősítők, Végfokok | 100W fölötti + 2.1 | `100w-folotti-erositok` | Termékcímke = `100W fölötti + 2.1` | /erositok-vegfokok-160/100w-folotti-21-171 | 39 | 100 W fölötti erősítők és végfokok bőséges választéka. Közkedvelt, nagy teljesítményű erősítőink között megtalálod például a HX-M544, az XH-M572 és a ZK-1002C HiFi sztereó erősítőt. | XY-E30H 2.1 erősítő |
| Erősítők, Végfokok | 2*50W erősítő / végfok | `2x50w-erositok-vegfokok` | Termékcímke = `2*50W erősítő / végfok` | /erositok-vegfokok-160/250w-erositovegfok-170 | 51 | 2×50 W fölötti erősítők és végfokok bőséges választéka. Közkedvelt, nagy teljesítményű erősítőink között megtalálod például a ZK-502L HiFi sztereó erősítőt és az APL50L 2×50 W-os erősítőt. | XH-M577 sztereó erősítőmodul |
| Erősítők, Végfokok | Audió kiegészítők | `audio-kiegeszitok` | Termékcímke = `Audió kiegészítők` | /erositok-vegfokok-160/audio-kiegeszitok-173 | 57 | Audió kiegészítők elsősorban, de nem kizárólag erősítőkhöz. Folyamatosan bővülő kategóriánkban többek között DFPlayer Minivel, zavarszűrőkkel, valamint hangfelvevő és -lejátszó modulokkal találkozhattok. | 4 pólusú rugós hangszóró csatlakozó |
| Erősítők, Végfokok | Hangszóró | `hangszorok` | Termékcímke = `Hangszóró` | /erositok-vegfokok-160/hangszoro-222 | 8 | *nincs* | 3525 hangszóró 4Ω 3W |
| BMS-ek, 18650 Akkuk | 1S - 5S BMS | `1s-5s-bms` | Termékcímke = `1S - 5S BMS` | /bms-ek-18650-akkuk-162/1s-5s-bms-169 | 33 | 1S–5S BMS modulok. Hatalmas választékunkban megtalálod például az egycellás 18650 Li-ion power bank vezérlőmodult, a 2S 10A-es balanszos BMS modult és még sok más balanszos BMS modult. | 3S40A 18650 BMS modul |
| BMS-ek, 18650 Akkuk | Akku cellák / elemek | `akku-cellak-elemek` | Termékcímke = `Akku cellák / elemek` | /bms-ek-18650-akkuk-162/akku-cellak-elemek-236 | 24 | *nincs* | INR18650-33VA Li-ion akku 3200 mAh |
| BMS-ek, 18650 Akkuk | 6S - 13S BMS | `6s-13s-bms` | Termékcímke = `6S - 13S BMS` | /bms-ek-18650-akkuk-162/6s-13s-bms-172 | 14 | 6S–13S BMS modulok. Kínálatunkban megtalálod például a 25,2 V-os, balanszos 6S 40A BMS modult, a 10S 15A-es 18650 akkufelügyeleti BMS-t, a 37–42 V-os Li-ion védőmodult és még rengeteg balanszos BMS modult. | 6S 14A 18650 BMS |
| BMS-ek, 18650 Akkuk | Akku töltők | `akku-toltok` | Termékcímke = `Akku töltők` | /bms-ek-18650-akkuk-162/akku-toltok-175 | 45 | 18650-es akkumulátortöltők, Li-ion töltők és még sok más. | 18650 Li-ion akku töltő modul + step up |
| BMS-ek, 18650 Akkuk | BMS kiegészítők | `bms-kiegeszitok` | Termékcímke = `BMS kiegészítők` | /bms-ek-18650-akkuk-162/egyeb-176 | 79 | Ebben a kategóriában BMS-kiegészítőket találhattok, többek között szigetelőgyűrűt. | 18650 Akku cella tartó 2 db-os |
| DC, AC konverterek | AC-DC tápegységek / labortáp | `ac-dc-tapegysegek-labortap` | Termékcímke = `AC-DC tápegységek / labortáp` | /dc-ac-konverterek-163/dc-tapegysegek-194 | 48 | *nincs* | 12 voltos 5A tápegység, AC-DC |
| DC, AC konverterek | DC-DC step down / feszültségcsökkentő | `dc-dc-step-down` | Termékcímke = `DC-DC step down / feszültségcsökkentő` | /dc-ac-konverterek-163/dc-dc-step-down-feszcsokkento-181 | 59 | DC-DC step down feszültségcsökkentőink. Megtalálod köztük például a Mini 360 DC-DC step down modult, az XL4015 5A-es modult, a 75 W-os, LED-kijelzős kapcsolóüzemű tápegységet és még rengeteg mást. | AC 220V 2000W szabályzó ⚠ |
| DC, AC konverterek | DC-DC step up / feszültségnövelő | `dc-dc-step-up` | Termékcímke = `DC-DC step up / feszültségnövelő` | /dc-ac-konverterek-163/dc-dc-step-up-fesznovelo-182 | 26 | DC-DC step up feszültségnövelőink. Kategóriánkban megtalálod például a DC 400W 15A step-up boost konvertert, az MT3608 step up modult és még rengeteg mást. | DC 400W 15A Step-up Boost konverter |
| Műszerek | Műszerdobozok | `muszerdobozok` | Termékcímke = `Műszerdobozok` | /muszerek-164/muszerdobozok-227 | 16 | *nincs* | Műszerdoboz 95*55*22 fekete |
| Egyéb | Szerszámok | `szerszamok` | Termékcímke = `Szerszámok` | /egyeb-165/szerszamok-220 | 55 | *nincs* | Kék hőálló szilikon szerelőalátét |
| Elektronika | Ellenállások / potméterek | `ellenallasok-potmeterek` | Termékcímke = `Ellenállások / potméterek` | /elektronika-177/ellenallasok-potmeterek-180 | 146 | *nincs* | Ellenállás 1k ohm 1/4W / 10 db |
| Elektronika | Fizika óra / áramköri elemek | `fizika-ora-aramkori-elemek` | Termékcímke = `Fizika óra / áramköri elemek` | /elektronika-177/fizika-ora-aramkori-elemek-203 | 17 | *nincs* | (alapértelmezett első: IC kiemelő ⚠) |
| Elektronika | Hűtőbordák / ventilátorok | `hutobordak-ventilatorok` | Termékcímke = `Hűtőbordák / ventilátorok` | /elektronika-177/csatlakozok-vezetekek-202 | 18 | *nincs* | Szilikon izolációs lap TO-3P |
| Elektronika | IC | `ic` | Termékcímke = `IC` | /elektronika-177/ic-178 | 40 | *nincs* | (IC kiemelő ⚠) |
| Elektronika | Kapcsolók / csatlakozók / vezetékek | `kapcsolok-csatlakozok-vezetekek` | Termékcímke = `Kapcsolók / csatlakozók / vezetékek` | /elektronika-177/kapcsolok-csatlakozok-vezetekek-200 | 219 | *nincs* | Próbapanel/breadboard jumper vezetékek /65 db |
| Elektronika | Kondenzátorok / diódák | `kondenzatorok-diodak` | Termékcímke = `Kondenzátorok / diódák` | /elektronika-177/kondenzatorok-195 | 57 | *nincs* | (IC kiemelő ⚠) |
| Elektronika | Ledek | `ledek` | Termékcímke = `Ledek` | /elektronika-177/ledek-183 | 47 | *nincs* | LED 5mm kék /10 db |
| Elektronika | PCB nyáklapok / forrasztási anyagok | `pcb-nyaklapok-forrasztasi-anyagok` | Termékcímke = `PCB nyáklapok / forrasztási anyagok` | /elektronika-177/pcb-nyaklapok-forrasztasi-anyagok-193 | 32 | *nincs* | Próba NYÁK, forrszemekkel 7*9 cm |
| Elektronika | Tranzisztor / MOSFET | `tranzisztor-mosfet` | Termékcímke = `Tranzisztor / MOSFET` | /elektronika-177/tranzisztor-mosfet-179 | 52 | *nincs* | L7805cv 5V-os feszültségszabályzó IC |
| D.I.Y. Készletek | Csavarok / betétek | `csavarok-betetek` | Termékcímke = `Csavarok / betétek` | /diy-keszletek-225/csavarok-betetek-239 | 7 | *nincs* | M3 réz menetes betét |
| D.I.Y. Készletek | Távtartók | `tavtartok` | Termékcímke = `Távtartók` | /diy-keszletek-225/tavtartok-237 | 18 | *nincs* | M3 réz távtartó készlet (120 db) |

### Eltérések, amelyeket a tulajdonosnak érdemes megnéznie (⚠)

- **ESP8266 alkollekció:**
  - Az „ESP32 - Cam” termék (cikkszám 1-2-1) a morzsamenü szerint az ESP8266 alkategóriában van, pedig ESP32-es termék. Valószínűleg át kellene sorolni ESP32-be.
  - A menü „22” terméket ír, a kategóriaoldal 23-at.
- **Arduino:** a menü „34” terméket ír, a kategóriaoldal 37-et. A régi slug `avr-duino`, a kategória H1-je „Modulshop - Avr-diuno” (elírással).
- **DC-DC step down:** a „Legtöbbet vásárolt” rendezés első terméke egy 230 V-os AC teljesítményszabályzó, ami nem DC-DC konverter. Ugyanez a termék a „Led világítás” kategória első helyén is ott van. Érdemes átsorolni.
- **IC kiemelő:** ugyanez a szerszám áll az alapértelmezett lista élén a „Fizika óra”, az „IC” és a „Kondenzátorok, Diódák” alkategóriában is. Valószínűleg a „Szerszámok” közé való. Ezekhez az alkollekciókhoz egy jellemző alkatrész képét válaszd.
- **Hűtőbordák / ventilátorok:** a régi slug (`csatlakozok-vezetekek-202`) nem egyezik a névvel. Az új handle a név alapján készült.
- **Erősítők alkategóriák:** mindkét erősítő-alkategória H1-je egyszerűen „Erősítők”. A menüben szereplő név alapján neveztük el őket.
- **2*50W erősítő / végfok:** a régi slug (`250w-erositovegfok`) 250 W-ot sugall, a név 2×50 W-ot. A handle a név alapján készült: `2x50w-erositok-vegfokok`.
