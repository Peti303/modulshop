# Hozzáférések beállítása – lépésről lépésre

A sablon a GitHubon keresztül kerül a Shopifyba. Külön hozzáférés csak a **Meta / Facebook + Instagram** tartalmakhoz kell.
A titkos kulcsokat (jelszó, token) **soha ne írd be a csetbe.** Amikor szólsz, hogy megvagy, egy biztonságos űrlapot kapsz, és oda kell beilleszteni. Én a kulcsot nem látom, a rendszer csak a megfelelő szervernek küldi el.

---

## 1. Shopify – GitHub-integráció (Theme Access nem kell)

Az áruház (`modulshop-hu-dd1b00hc.myshopify.com`) **„modulshop/main” nevű, közzétett sablonja** a GitHub-tároló `main` ágához van kötve. Ami a `main`-be kerül, az élesben is megjelenik. Az áruház jelszóval védett, és még nincs benne termék.

Én a `claude/wizardly-galileo-gs2p4e` ágon dolgozom. Ha ezt az ágat is bekötöd egy **második, közzététel nélküli sablonként**, minden commitom után azonnal látjuk az eredményt, és az élő sablon érintetlen marad:

1. Shopify admin → **Online áruház → Sablonok → Sablon hozzáadása → Csatlakozás a GitHubról**.
2. Tároló: `Peti303/modulshop`, ág: `claude/wizardly-galileo-gs2p4e`.
3. A megjelenő sablonnál: **⋯ → Előnézet** → **Előnézet megosztása**. A kapott linket (benne a `preview_theme_id`) küldd el a csetben.

Ha kész vagyunk, a PR-t összevonod a `main`-be, és az új dizájn élesedik.

**Figyelem:** a sablonszerkesztőben tett módosításokat a Shopify visszacommitolja a bekötött ágra. Ezért én mindig lehúzom a legfrissebb állapotot, mielőtt dolgozom.

**Termékek, kategóriák, oldalak:** ezek nem a sablon részei. A termékekhez Shopify-formátumú CSV-t készítek a modulshop.hu valódi adataiból, ezt a *Termékek → Importálás* menüpontban egy kattintással feltöltheted. A menüket, oldalakat és átirányításokat lépésenkénti listában adom meg, vagy később egy Admin API kulccsal én viszem fel.

---

## 2. Meta (Facebook + Instagram) – Graph API token

A Facebook bejelentkezés nélkül nem enged robotot az oldalakra, a bejelentkezés megkerülése pedig tilos és kockázatos is. A hivatalos és biztonságos út a **Meta Graph API**: egy csak olvasási jogú token, amellyel az oldal saját posztjait, fotóit, értékeléseit és az Instagram-posztokat le tudom tölteni.

### Miért kell az admin szerepkör és az Instagram szakmai fiók?
- **A Graph API nem „mindenhez” ad hozzáférést.** A token mindig egy Facebook-felhasználóhoz tartozik, és csak azokat az oldalakat éri el, amelyeken annak a felhasználónak szerepköre van. Idegen oldal tartalmához a „Page Public Content Access” funkció kellene. Ehhez Meta-ellenőrzés és cégellenőrzés szükséges, ami heteket vesz igénybe, és ilyen célra jellemzően nem engedélyezik.
- **Instagram:** a magánfiókokhoz tartozó API-t (Basic Display) a Meta 2024 decemberében megszüntette. Ma API-n csak **szakmai (Business vagy Creator) fiók** érhető el. A váltás ingyenes, kb. 1 perc, és nem jár hátránnyal. Hogy már szakmai-e, onnan látszik, hogy a profilon megjelenik a „Professzionális irányítópult”.
- **Nem neked kell adminnak lenned:** a tokent bárki létrehozhatja, akinek már van szerepköre az oldalon, például valaki a modulshoptól. A lépések ugyanazok.

### Előfeltételek (egyszer kell, a cég segítségével)
- **A tokent létrehozó személynek szerepköre kell legyen a modulshop Facebook-oldalán**, teljes hozzáféréssel (te vagy egy modulshopos kolléga). A cég ezt a **Meta Business Suite → Beállítások → Személyek / Oldalhozzáférés** alatt adhatja meg neked.
- Az **Instagram-fióknak szakmai (Business vagy Creator) fióknak kell lennie, és a Facebook-oldalhoz kell kapcsolódnia.** Ha nem így van: Instagram app → Beállítások → *Fióktípus és eszközök* → *Váltás szakmai fiókra*, majd a Business Suite-ban az Instagram-fiók összekapcsolása az oldallal.

### A) Fejlesztői fiók és app (kb. 5 perc)
1. Nyisd meg: `https://developers.facebook.com`, és lépj be a saját Facebook-fiókoddal.
2. Jobb fent **Get Started / Kezdés**: regisztrálj fejlesztőként (telefonszámos megerősítés kellhet).
3. **My Apps → Create App / App létrehozása.**
   - App neve: `Modulshop weboldal`
   - Felhasználási eset: **Other / Egyéb**, típus: **Business**. (Ha a felület mást kínál: a „Facebook-oldal kezelése” jellegű eset is jó.)
   - Az app maradhat **fejlesztői módban**. Mivel a saját oldaladat olvasod, Meta-jóváhagyás nem kell.

### B) Token létrehozása
4. Nyisd meg a **Graph API Explorert**: `https://developers.facebook.com/tools/explorer`
5. Jobb oldalt a *Meta App* mezőben válaszd ki a `Modulshop weboldal` appot.
6. *User or Page:* **Get User Access Token**. A *Permissions* listában pipáld be:
   - `pages_show_list`
   - `pages_read_engagement`
   - `pages_read_user_content` (az értékelésekhez)
   - `instagram_basic`
   - `business_management` (ha felkínálja)
7. **Generate Access Token**: a felugró ablakban válaszd ki a **modulshop oldalt** és a **modulshop Instagram-fiókot**, majd engedélyezd.

### C) Lejárat nélküli oldaltoken (ajánlott, különben 1–2 óra után lejár)
8. Másold ki a kapott tokent, és nyisd meg: `https://developers.facebook.com/tools/debug/accesstoken`. Illeszd be, **Debug**, majd alul **Extend Access Token**. Ez egy 60 napos tokent ad; másold ki.
9. Menj vissza a Graph API Explorerbe, és illeszd be ezt a hosszú tokent az *Access Token* mezőbe.
10. A lekérdezés mezőbe írd be: `me/accounts`, majd **Submit**.
11. Az eredményben keresd meg a modulshop oldalt. Az ott látható `access_token` értéke a **lejárat nélküli oldaltoken**. Ezt kérem.
12. Szólj, és megjelenik az űrlap, oda illeszd be. **A csetbe ne írd be.**

**Visszavonás a projekt végén:** a developers.facebook.com oldalon töröld az appot, vagy a Facebookon: *Beállítások → Üzleti integrációk / Alkalmazások* → eltávolítás. A token ezzel azonnal érvényét veszti.

---

## Mit kapok és mit nem
| | Meta oldaltoken |
|---|---|
| Látom | az oldal posztjai, fotói, értékelései; Instagram-posztok |
| Nem látom | privát üzenetek, a személyes profilod, hirdetési fiók |
| Módosíthatok | semmit (csak olvasás) |

A kulcsok ennek a felhőkörnyezetnek a hálózati titkai között tárolódnak. A projekt végén a környezet beállításaiban törölhetők.
