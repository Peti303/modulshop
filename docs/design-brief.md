# Design brief – modulshop.hu új Shopify webshop

> Átadási dokumentum egy tervező/fejlesztő modellnek (Fable 5.2).
> Összefoglalja a megrendelő kéréseit, az eddigi munkát, a valódi adatokat és a szabályokat.
> **A feladat most: részletes dizájnterv készítése.** A sablon átépítése csak a terv jóváhagyása után kezdődik.

---

## 1. A feladat egy mondatban
A **modulshop.hu** (magyar elektronikai alkatrész-webáruház) a ShopRenterről Shopifyra költözik. Új, egyedi, **jól konvertáló, átlátható és könnyen kezelhető** dizájnt kell tervezni a **Shopify Horizon v4.5.0** sablonra építve. A dizájn működjön telefonon, tableten és számítógépen, legyen **világos és sötét módja**, és **kerülje a sablonos, AI-generált oldalakra jellemző mintázatokat**.

## 2. A megrendelő kérései
1. **Egyedi dizájn** a Horizon keretrendszerben, a modulshop.hu-nak, a cég engedélyével. A jelenlegi webshop működik, de nagyon rosszul néz ki.
2. **Jól konvertáló webshop**, szép dizájnnal, ami telefonon, tableten és számítógépen is átlátható.
3. **Világos és sötét mód**: egy kapcsolóval lehessen váltani, szép animációval. A kapcsoló gombja pontosan középen legyen a nap és a hold ikonon. A megrendelő ezt külön kifogásolta: az első változatnál a kör nem volt középen.
4. **Csak valódi tartalom**: valódi vélemények forrással, valódi adatok. Semmit nem szabad kitalálni.
5. **Képek**: a Facebookon nincs használható minőségű kép, onnan ne vegyünk át semmit. A képek a modulshop.hu saját termékfotói (fehér háttér).
6. **Költözés**: meg kell tervezni minden oldalt, ami a webshop teljes működéséhez kell. Prioritás: **felhasználóbarát, kezelhető, átlátható**.
7. **Autonóm munka**: önálló kutatás és döntések, de az ellentmondó tényeket a tulajdonosnak kell tisztáznia.
8. **A design újragondolása**: a színeket és az elrendezést újra kell gondolni. Készüljenek **tervek és ötletek**, a meglévő sablon egyelőre ne változzon.
9. **Ne legyen sablonos AI-oldal hatása.** Lásd a 6. pontot.
10. Gyorsabb és jobb eredményért szabad párhuzamos segédeket (subagenteket) használni.

## 3. A cég – valódi tények (forrás: docs/research/*)
- **Profil:** elektronikai alkatrészek, modulok és kiegészítők webáruháza. Arduino, ESP32, Raspberry Pi, szenzorok, kijelzők, erősítők, BMS és 18650 akkuk, tápegységek, műszerek, szerszámok, DIY készletek, LED.
- **Üzemeltető:** Nováki József egyéni vállalkozó. Copyright-sor alapján 2019 óta működik (nincs megerősítve).
- **Kínálat:** 1811 termék, ebből 1019 raktáron (2026-11-12). A készletet darabra pontosan mutatják.
- **Elérhetőség:** +36 70 944 7641 · info@modulshop.hu
- **Személyes átvétel:** 1078 Budapest, Nefelejcs utca 43. (bejárat a Marek József utca felől, fehér ajtó, szuterén). Csak online leadott rendelésre. H–P 8:00–18:00, Sz–V 10:00–16:00. ⚠ A Facebook-grafika más címet ír: 1081 Budapest, II. János Pál pápa tér 12.
- **Állítások, amelyek kommunikálhatók:**
  - a 10:00-ig leadott rendelést még aznap átadják a futárnak;
  - magyarországi raktárkészlet, nincs további vám vagy adóteher;
  - 30 napos, kérdés nélküli visszaküldés, ingyenes GLS-automatás visszaküldéssel;
  - 1 év garancia minden termékre;
  - iskolákat, intézményeket és cégeket is kiszolgálnak (mennyiségi kedvezmény, előrendelés);
  - saját fejlesztésű termékek, fő terméktervező Bán Péter;
  - 5% hűségpont;
  - Facebook szerint: hírlevél-feliratkozásért 5% kedvezmény, és 15 000 Ft felett ingyenes szállítás (megerősítendő).
- **Szállítás:**
  - automata: Foxpost 1250 Ft, MPL 1250 Ft, GLS 1300 Ft (egy másik oldalon 1350 Ft);
  - házhoz: MPL 1700 Ft, GLS 1950 Ft;
  - posta 1400 Ft, GLS csomagpont 2000 Ft.
- **Fizetés:** Barion bankkártya, utánvét, átutalás, készpénz átvételkor.
- **Értékelések:**
  - modulshop.hu termékvélemények: **4,62/5 (311 db)**;
  - Onlinepénztárca: **9,6/10 (447 db)**, https://onlinepenztarca.hu/webaruhaz/modulshophu
  - Google: kb. 4,3/5 (kb. 57–61 db), csak közvetett adat;
  - az Árukereső nem volt ellenőrizhető.
- **Közösségi média:**
  - Facebook „Modulshop”: https://www.facebook.com/NovakiJozsef/ (1,3 E követő);
  - YouTube: https://www.youtube.com/@Modulshop
  - Az Instagram nincs megerősítve. A TikTok @modulshop NEM a cégé.
- **Arculat:**
  - kétszínű logó, a „Modul” türkiz #0594AE, a „shop” sötétkék #01598B, áramköri ikonnal;
  - a régi téma színei: #273C99 kék és #FFCF0F sárga, Roboto betűtípussal;
  - a logó fájljai: `assets/ms-logo.png` és sötét módhoz `assets/ms-logo-dark.png`.

### Kategóriák és termékszámok
| Kategória | db |
|---|---|
| Mikrovezérlők, alaplapok | 117 |
| Szenzor modulok | 121 |
| Egyéb modulok | 316 |
| Erősítők, végfokok | 156 |
| LCD-k, kijelzők | 50 |
| BMS-ek, 18650 akkuk | 196 |
| DC, AC konverterek | 134 |
| Műszerek | 109 |
| Elektronika | 652 |
| D.I.Y. készletek | 82 |
| Egyéb (szerszámok) | 196 |
| LED világítás | 54 |

A teljes kategóriafa a Shopify-handle-ökkel: `docs/import/collections.md` és `docs/import/menus.md`.

### Mintatermékek (valódi; a teljes lista: docs/import/products.csv)
| Termék | Cikkszám | Ár | Készlet |
|---|---|---|---|
| ESP32-C3 Szuper mini, WiFi, BT 5.0, usb-C | 1-2-29 | 1 900 Ft | 37 db |
| Uno R3 – ATmega328P – Arduino kompatibilis, usb-C | 1-1-27 | 2 500 Ft | 14 db |
| DHT11 hőmérséklet- és páratartalom-érzékelő | 2-1-1 | 650 Ft | 31 db |
| 0,96" OLED kijelző, fehér, I2C | 4-1-21 | 1 250 Ft | 13 db |
| LCD 1602 + I2C, kék | 4-1-5 | 1 700 Ft | 5 db |
| XH-M577 sztereó erősítő 2×80 W | 5-1-46 | 2 600 Ft | 15 db |
| Multiméter DT-830B | 8-1-1 | 1 800 Ft | 171 db |
| Relé modul 1 portos 5V/220V | 3-1-36 | 600 Ft | 190 db |

### Megjeleníthető vélemények (szó szerint; további 26 db: docs/research/reviews.md)
- „Elektronikai alkatrészek és modulok széles választéka. A megrendelés akár aznap átvehető a helyszínen. Jó árak, sok akció, profi kiszolgálás. Az egyik legjobb webáruház ebben a kategóriában.” – László, Onlinepénztárca, 10/10, 2026. 07. 13.
- „Hatalmas választék, nagyon barátságos árak. A szállítás és csomagolás nagyon rendben volt. Ajánlom.” – Krisztián, Onlinepénztárca, 10/10, 2026. 07. 21.
- „Jó termékek jó áron, gyors szállítás csomagautomatába.” – Péter, Onlinepénztárca, 10/10, 2026. 08. 19.
- „Megrendelés utáni nap megjött a termék. Az adatkábel sérült volt, telefonos megbeszélés után másnap küldtek egy újat. A temékkel és ugyintézéssel nagyon elégedett vagyok,csakajánlani tudom.” – Garaczi István, modulshop.hu, 5/5, 2026. 02. 18., igazolt vásárlás
- „A modulshop-on vásárolt termékekkel eddig soha semmi probléma nem adódott, minden tökéletesen működött. Jó árak, kitűnő gyorsaság és kiszolgálás.” – Ujvári Gábor, modulshop.hu, 5/5, 2026. 04. 21.
- „Kedvező áron, szakszerűen becsomagolt terméket kaptam.” – Zöldfay András, modulshop.hu, 5/5, 2023. 11. 26., igazolt vásárlás

A véleményeket helyesírási hibáikkal együtt, szó szerint kell idézni, forrással, névvel és dátummal.

### A jelenlegi modulshop.hu UX-hibái (amiket meg kell oldani)
- A főkategória oldala csak a közvetlenül hozzárendelt termékeket mutatja. A „Mikrovezérlők” 1 terméket mutat, holott 116 van alatta.
- A termékek kb. 44%-a nincs raktáron, és vegyesen jelenik meg a raktáron lévőkkel.
- Élesben maradt helyőrző tartalom: „teszt 1”, a Rólunk oldalon csak „Hamarosan” áll.
- Ellentmondó adatok a jogi oldalakon (lásd a 9. pontot).
- Nincsenek márka-, specifikáció- és adatlapmezők, sem kapcsolódó termékek. Minden termék márkája „Modulshop”.

## 4. Technikai keret
- **Tároló:** GitHub `Peti303/modulshop`, munkaág `claude/wizardly-galileo-gs2p4e`, PR: https://github.com/Peti303/modulshop/pull/1
- **Shopify áruház:** `modulshop-hu-dd1b00hc.myshopify.com`. Éles, nem dev típusú, átadható a cégnek. Jelszóval védett, a storefront jelszava a megrendelőtől kérhető. Termék még nincs feltöltve.
- **GitHub-integráció:**
  - a közzétett „modulshop/main” sablon a `main` ágat követi;
  - a munkaág egy közzététel nélküli második sablon (ID **192355959112**);
  - előnézet: `https://modulshop-hu-dd1b00hc.myshopify.com/?preview_theme_id=192355959112`
- **Projektmemória és jegyzetek:**
  - `CLAUDE.md` (szabályok);
  - `docs/decisions.md` (döntések);
  - `docs/horizon-notes.md` (Horizon-térkép: színek, fejléc, JS, sablonok, buktatók);
  - `docs/research/` (elemzés, vélemények, jelenlét);
  - `docs/import/` (költözési csomag: termék-CSV, kollekciók, menük, oldalszövegek, átirányítások, README 19 nyitott kérdéssel).
- **Képernyőkép-eszköz:**
  - `node docs/tools/shot.js <útvonal> <név> [--sizes=desktop,tablet,mobile] [--modes=light,dark] [--viewport]`
  - env: `SHOT_DIR`, `STORE_PASSWORD`;
  - asztali nézetben a Horizon a `.page-wrapper`-t görgeti, az eszköz ezt kezeli.

### Bevált szabályok a Horizon és a Shopify GitHub-szinkron kapcsán (betartandók)
- Az egyedi kód **új fájlokba** kerüljön (`assets/ms-*`, `sections/ms-*`, `blocks/ms-*`, `snippets/ms-*`), hogy a Horizon-frissítések összefésülhetők maradjanak.
- **A szekció-, blokk- és preset-nevek legfeljebb 25 karakteresek** lehetnek (pl. „MS · …”). Ha hosszabb, a Shopify elutasítja a fájlt.
- **Linkbeállításhoz `text` típust használj, ne `url`-t.** A relatív vagy még nem létező céloknál a Shopify elutasíthatja a sablont.
- **Kétlépcsős feltöltés:** előbb az új szekció- és blokkfájlokat kell felküldeni, és megvárni, amíg a Shopify átveszi őket. Csak utána jöhet a rájuk hivatkozó JSON-sablon. Ha a sablon túl korán érkezik, a Shopify elutasítja, és a fájl következő módosításáig nem próbálja újra.
- A `templates/*.json`, `sections/*-group.json` és `config/settings_data.json` fájlokat a szerkesztő is írja. Munka előtt `git pull`.
- **Sötét mód:**
  - `html[data-theme="dark"]` alatt a Horizon változóit is felül kell írni (`--color-*`, `--opacity-*`, gombok, inputok, `.color-custom-*`, fejlécsor-háttér);
  - inline head-script kell, hogy betöltéskor ne villanjon;
  - `color-scheme` és `meta theme-color` beállítása;
  - a View Transitions API-val a kapcsolóból kiinduló kör alakú feltárás az animáció. Csökkentett mozgás beállításnál animáció nélkül vált, régi böngészőben egyszerű színátúszással.
- Asztali nézetben a Horizon a `.page-wrapper`-t görgeti, nem az ablakot. A görgetésre induló animációkat ehhez kell igazítani, és mindig legyen tartalék, hogy semmi ne maradjon láthatatlan.
- Minden szöveg, kép, link és vélemény legyen **szerkeszthető a Shopify szerkesztőjében** (kezelhetőség).

## 5. Ami jelenleg a munkaágon van (első változat, nincs véglegesítve)
- **Dizájnrendszer:** `assets/ms-theme.css`, tokenek `--ms-*`, világos és sötét mód. Kapcsoló: `snippets/ms-theme-toggle.liquid`, `snippets/ms-theme-init.liquid`, `assets/ms-ui.js`. A kapcsoló geometriája pixelpontos (56×30, 24 px-es kör, 26 px elmozdulás).
- **Főoldal szekciói:** `ms-hero`, `ms-usp`, `ms-categories`, Horizon `product-list`, `ms-promo-split`, `ms-testimonials`, `ms-store-info` (átvétel és GYIK), `ms-newsletter`.
- **Lábléc:** `ms-footer`. **Hirdetősáv:** 3 üzenet.
- **Oldalsablonok:** `page.json`, `page.about.json`, `page.contact.json`, `page.faq.json`, `page.shipping.json`, `page.b2b.json`, `page.legal.json`, `404.json`. Szekciók: `ms-page-header`, `ms-page-content`, `ms-contact`, `ms-faq` (FAQ structured data-val), `ms-shipping-table`, `ms-features`, `ms-cta`, `ms-404`.
- **Termékoldal:** Horizon `product-inventory` blokk és `blocks/ms-product-trust.liquid` (szállítás, garancia, cikkszám).
- **Kosár:** `snippets/ms-free-shipping.liquid` haladásjelző. Az értékhatár a témabeállításokban van, a „Modulshop” csoportban.
- **Ellenőrizve:** élő előnézet asztali, tablet és mobil nézetben, világos és sötét módban, Liquid-hiba nélkül.
- **Nincs ellenőrizve:** termékoldal, kategóriaoldal, kosár valódi termékekkel (még nincs termék), kapcsolati űrlap elküldése.
- **Tulajdonosi teendők (admin):**
  - a bolt nyelve még angol, magyarra kell állítani;
  - a „Main menu” még alapértelmezett (Home, Catalog, Contact);
  - a termékek CSV-importja még nem történt meg.

## 6. A jelenlegi dizájn kritikája – ezeket a mintákat NE használd
Az első változat túl sok „AI-landing” klisét tartalmaz:
- színátmenetes kék nyitókép áramköri vonalakkal a háttérben;
- kis „pirula” címke a főcím fölött, nagybetűs eyebrow-feliratok;
- statisztikasor (nagy szám + kis felirat egymás mellett);
- lebegő, eltolt vagy elforgatott termékkártyák (bento);
- ikonos négyes előnyrács ikonbadge-ekkel;
- idézőjel-ikonos véleménykártyák körhinta-csúszkában;
- színátmenetes hírlevéldoboz;
- mindenhol 12–20 px lekerekítés és lágy árnyék;
- egyetlen semleges betűtípus (Inter) mindenre;
- bal oldali színes csíkos kártyák és emojik.

## 7. Feltárt dizájnirányok (vázlatok)
Tervvászon: https://claude.ai/artifact/9uTQpSVqfp75wXsFBkxw1R. Irányonként asztali, mobil és sötét mobil nézet, valódi adatokkal.

**A · Alkatrészkatalógus**
- Adatlap-tipográfia: IBM Plex Sans és IBM Plex Mono.
- Színek:
  - világos: papír #F4F2ED, tinta #15181C, teendőszín #01598B, készletzöld #1F7A4D, vonal #D6D1C7;
  - sötét: #121416, #ECE8DF, #5BB4DE, #5FCB8E.
- Nyitókép helyett „keresés + Gyors rendelés cikkszámmal” doboz.
- Számozott kategóriaindex pontozott vezetővonallal.
- Terméklista készlettel, cikkszámmal és darabszám-választóval.
- A vélemények vonalas listában, a személyes átvétel adatlap-táblázatban.

**B · Alkatrészfiók**
- Szerelőasztal-hangulat. Barlow Condensed és Barlow.
- Színek: vágólapzöld #2F5A4C, régi sárga #FFCF0F címkeként, fiók #D9DDD6.
- A nyitókép cm-rácsos vágólap, rajta termékfotók sárga címkével.
- A kategóriák fiókos alkatrész-szekrényként, a vélemények „szerelőnaplóként”.
- Ismert hibák: 1400 px alatt a nyitókép jobb oldali termékei levágódhatnak; mobilon a vélemények vége kilóghat.

**C · Nyák**
- Archivo és JetBrains Mono.
- Színek: lakk-kék #0D4C77 (csak fejléc, kiemelt sáv, lábléc), arany forrpont #C99A2E a gombokon, alap #FAFAF7.
- A szekciók jelölése nyákszerű (J1, U2, R3, C4), a bal szélen egy vezetékpálya fut, forrpontokkal.
- A csempék sarokjelölésekkel, árnyék nélkül.

**Eddigi javaslat:** az A irány legyen az alap, mert 1800 terméknél a keresés, a készlet és a listanézet konvertál a legjobban. Ebbe érdemes átvenni a B irányból a fiókos kategórianavigációt és a sárga címkét, mint saját karaktert. **A megrendelő még nem döntött.**

## 8. Amit a dizájntervnek tartalmaznia kell (elvárt kimenet)
1. **Koncepció és indoklás:** milyen karakter, miért konvertál, miben különbözik a sablonos AI-oldalaktól.
2. **Dizájnrendszer:**
   - színpaletta világos ÉS sötét módban, tokenekkel, kontrasztértékekkel (szöveg ≥ 4.5:1);
   - tipográfia (betűtípusok, méretskála mobilon és asztalin);
   - térköz-skála, rácsrendszer, lekerekítés, vonalak, árnyékok;
   - ikonstílus, képkezelés (fehér hátterű termékfotók sötét módban is).
3. **Világos és sötét mód kapcsoló:** elhelyezés (asztalin a fejléc, mobilon a menü és a lábléc), pontos geometria (a kör középen az ikonon), animáció (oldalszintű kör alakú feltárás és a kapcsoló saját mozgása), viselkedés csökkentett mozgásnál, és az alapállapot rendszerbeállítás alapján.
4. **Komponensek:**
   - fejléc és hirdetősáv, mega-menü (3 szint), mobilmenü, kereső előnézettel;
   - termékkártya és listasor (készlet, cikkszám, ár, mennyiség, kosárba), kategóriacsempe;
   - gombok, űrlapelemek, badge-ek (akció, kevés készlet, elfogyott);
   - véleményelem, GYIK-elem, lábléc;
   - kosárpanel ingyenes-szállítás-jelzővel, „Gyors rendelés cikkszámmal”.
5. **Oldaltervek** asztali (1440), tablet (820) és mobil (390) nézetben:
   - főoldal;
   - kategóriaoldal (szűrők: raktáron, ár, típus, alkategória; rendezés; lista/rács váltó; a raktáron lévők elöl);
   - termékoldal (galéria, ár, készlet darabra, cikkszám, szállítási és garanciaadatok, leírás, specifikáció, kapcsolódó termékek, mobilon ragadós kosár gomb);
   - keresési találatok, kosár és kosárpanel;
   - fiók (belépés, regisztráció, rendelések);
   - Rólunk, Kapcsolat (űrlappal), GYIK, Szállítás és fizetés, Garancia és visszaküldés, Iskoláknak és cégeknek, Hűségpont, Saját termékeink;
   - jogi oldalak (ÁSZF, Adatvédelem, Elállás, Impresszum);
   - blog és cikk, 404, jelszóoldal.
6. **Konverziós elemek:**
   - keresés az első helyen;
   - valós készletszám, kevés készlet jelzése;
   - 10:00-ig aznapi feladás kommunikálása;
   - ingyenes szállítás haladásjelző;
   - rendelés cikkszámmal iskoláknak és szakköröknek;
   - újrarendelés;
   - valódi vélemények forrással;
   - bizalmi elemek a kosár és a fizetés közelében;
   - hírlevél 5% kedvezménnyel.
7. **Akadálymentesség:** fókuszállapotok, legalább 44 px-es érintési célok, valódi gombok és linkek, címkézett űrlapok, alt szövegek, „csökkentett mozgás” támogatása.
8. **Megvalósítási terv a Horizonra:** mely Horizon-szekciók és blokkok maradnak és mit kapnak; milyen új `ms-*` szekciók kellenek; mi kerül a témabeállításokba; hogyan marad minden szerkeszthető.
9. **Vizuális vázlatok:** legalább a főoldal, a kategóriaoldal és a termékoldal asztali és mobil nézetben, világos és sötét módban.

## 9. Tisztázandó a tulajdonossal (ne találd ki, jelöld helyőrzővel)
1. Az átvételi pont címe: Nefelejcs u. 43. vagy II. János Pál pápa tér 12.?
2. A 15 000 Ft-os ingyenes szállítás érvényes-e?
3. Az adószám: három különböző szerepel.
4. Zárás 18:00 vagy 19:00?
5. GLS-automata: 1300 vagy 1350 Ft?
6. A visszaküldés költsége: az ÁSZF szerint a vevőé, két másik oldal szerint ingyenes.
7. Az ÁSZF-ben más telefonszám áll (06 31 781 5157).
8. A mennyiségi kedvezmény mértéke és feltételei.
9. A hűségpont szabálya.
10. A márka- és specifikációs adatok megléte.

A teljes, 19 pontos lista: `docs/import/README.md`.

## 10. Munkaszabályok
- Magyar nyelv, forint, bruttó árak.
- Csak valódi, forrással igazolt tartalom. A hiányzó adat helyőrzőt kap, például [ÁR], [CÍM?].
- Bejelentkezést igénylő oldalt nem kell kaparni, és a botvédelmet nem szabad megkerülni.
- Facebookról nem veszünk át képet.
- A közzétett (`main`) sablon nem változik. Minden munka a munkaágon és a PR-ban történik.
- Modellnevet nem írunk commitba vagy PR-ba.
- **Most csak tervezés:** a sablon átalakítása a terv jóváhagyása után kezdődik.
