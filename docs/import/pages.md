# Oldalak (Shopify Pages) – index

- **Hol vannak a szövegek:** a `pages/<handle>.html` fájlokban.
- **Mi van a fájlok elején:** minden fájl egy HTML-megjegyzéssel (`<!-- … -->`) kezdődik, a tulajdonosnak szól. Benne van a forrás, a fájlhoz tartozó megjegyzések és a jelenlegi oldalon talált **ellentmondások listája**. **A Shopify-ba csak a megjegyzés utáni részt másold be.**
- **Hogyan illeszd be:** Shopify admin → *Online áruház → Oldalak → Oldal hozzáadása*. A tartalomszerkesztőben kattints a `<>` (HTML megjelenítése) gombra, és ide illeszd be a szöveget.
- **Handle:** a *Keresőmotoros előnézet szerkesztése → URL-handle* mezőben add meg.
- **Sablon:** a *Téma sablon* legördülő listában válaszd ki. Ha a témában még nincs meg az adott sablon (pl. `page.about`), előbb hozd létre: *Online áruház → Témák → Testreszabás → Oldalak → Sablon létrehozása*. Kiindulásnak az alapértelmezett oldalsablon is jó.
- **A `[[…]]` jelölésű részek:** közzététel előtt ki kell tölteni vagy javítani (pl. adószám, GLS-ár, tárhelyszolgáltató).
- **Tervezetek:** a **TERVEZET** jelölésű oldalak csak tulajdonosi jóváhagyás után kerülhetnek ki.

| # | Oldal címe | Handle | Sablon-utótag | Fájl | Régi URL(-ek) | Állapot / megjegyzés |
|---|---|---|---|---|---|---|
| 1 | Rólunk | `rolunk` | `about` | pages/rolunk.html | /rolunk-51 | **TERVEZET.** Csak ellenőrzött tényekből áll. A „2019 óta” csak a copyright-sorból következik. |
| 2 | Kapcsolat | `kapcsolat` | `contact` | pages/kapcsolat.html | /kapcsolat-32 | A `contact` sablon kapcsolati űrlapot ad (a régi oldalon nem volt). Az adószámot javítani kell. |
| 3 | Gyakran ismételt kérdések | `gyik` | `faq` | pages/gyik.html | /gyakran-ismetelt-kerdesek-36 + főoldali GYIK | A két forrás összefésülve. Kérdés = `<h3>`, így a FAQ-sablon harmonikává alakíthatja. |
| 4 | Szállítás és fizetés | `szallitas-es-fizetes` | `shipping` | pages/szallitas-es-fizetes.html | /szallitasi-modok-71, /szallitasi-informaciok-65 | A GLS automata ára `[[TISZTÁZANDÓ]]`. |
| 5 | Garancia és visszaküldés | `garancia-es-visszakuldes` | (alapértelmezett) | pages/garancia-es-visszakuldes.html | /30-napos-termek-visszakuldes-38, /ingyenes-visszakuldes-77 | Ellentmond az ÁSZF 15.2 pontjának (a visszaküldés költsége). |
| 6 | Hűségpont rendszer | `husegpont` | *(alapértelmezett)* | pages/husegpont.html | /husegpont-rendszer-85, /regisztracio-87 | Csak akkor tedd közzé, ha a hűségpont-alkalmazás már működik. |
| 7 | Iskoláknak és cégeknek | `iskolaknak-es-cegeknek` | `b2b` | pages/iskolaknak-es-cegeknek.html | – (új oldal) | **TERVEZET.** Új oldal, ellenőrzött tényekből. |
| 8 | Általános Szerződési Feltételek | `aszf` | `legal` | pages/aszf.html | /adatvedelem-45, /vasarlasi-feltetelek-5 | Szó szerinti szöveg, tisztított formázással. Platformváltás miatt frissíteni kell (tárhely, fizetés). |
| 9 | Adatvédelmi nyilatkozat | `adatvedelem` | `legal` | pages/adatvedelem.html | /adatvedelmi-nyilatkozat-44 | Szó szerinti szöveg. A Shopify-t adatfeldolgozóként fel kell venni. |
| 10 | Impresszum | `impresszum` | `legal` | pages/impresszum.html | – (új oldal, az ÁSZF 1. pontjából) | A tárhelyszolgáltató adatai `[[KITÖLTENDŐ]]`. |
| 11 | Elállás | `elallas` | `legal` | pages/elallas.html | /withdrawal | Bevezető (a régi űrlap mezőiből) + az ÁSZF 14–16. pontja szó szerint. Az online elállási funkcióra megoldás kell. |
| 12 | Saját termékeink | `sajat-termekeink` | *(alapértelmezett)* | pages/sajat-termekeink.html | (/sajat-termekeink-244 → kollekció) | A kategórialeírás, a 6 saját termék és az egyedi műszerdoboz-szolgáltatás. |
| 13 | Mesterséges intelligencia (AI) használati szabályzat | `ai-hasznalati-szabalyzat` | `legal` | pages/ai-hasznalati-szabalyzat.html | /mesterseges-intelligencia-ai-hasznalati-szabalyzat-115 | Plusz oldal: a régi láblécben és a sitemapben is szerepel. Szó szerinti szöveg. |

**Nem visszük át (átirányítással kezeljük):**

| Régi oldal | Mi lesz vele |
|---|---|
| Vásárlási feltételek (/vasarlasi-feltetelek-5) | Elavult, ütközik az ÁSZF-fel → `/pages/aszf` |
| Regisztráció (/regisztracio-87) | A tartalma a Hűségpont oldalra került → `/account/register` |
| Csomag ajánlataink (/csomag-ajanlataink-101) | Üres oldal → `/collections/csomagok` |
| Keresés (/kereses) | → `/search` |

A lejárt projektverseny (/modulshop-projekt-verseny-79) és a többi blogbejegyzés **blogcikként** kerül át (`/blogs/news/...`). A blogcikkek tartalmát ez a csomag nem tartalmazza, a handle-ök listája a README-ben van.
