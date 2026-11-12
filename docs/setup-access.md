# Hozzáférések beállítása – lépésről lépésre

Két hozzáférés kell: **Shopify** (a sablon feltöltéséhez) és **Meta / Facebook + Instagram** (a képekhez és értékelésekhez).
A titkos kulcsokat (jelszó, token) **soha ne írd be a csetbe.** Amikor szólsz, hogy megvagy, egy biztonságos űrlapot kapsz, és oda kell beilleszteni. Én a kulcsot nem látom, a rendszer csak a megfelelő szervernek küldi el.

---

## 1. Shopify – Theme Access jelszó

Ezzel csak **sablonokat** tudok feltölteni és szerkeszteni. A rendeléseket, a vásárlókat, a fizetést és a beállításokat nem látom. Az élő sablont nem írom felül: az új sablon **közzététel nélkül**, külön sablonként kerül fel, és te döntöd el, mikor élesíted.

1. Lépj be a Shopify adminba: `https://admin.shopify.com`.
2. A bal menüben: **Alkalmazások (Apps)**, majd az áruház megnyitása (*Shopify App Store*).
3. Keress rá erre: **Theme Access** (a Shopify saját, ingyenes appja), majd **Install / Telepítés**.
4. Nyisd meg az appot, és kattints a **Create password / Jelszó létrehozása** gombra.
   - Név: `Modulshop sablonfejlesztés`
   - E-mail: a saját e-mail címed (ide jön a jelszó)
5. Megérkezik az e-mail. Nyisd meg benne a linket **7 napon belül**. A jelszót (`shptka_…` kezdetű) **csak egyszer** mutatja meg, ezért másold ki.
6. Küldd el nekem a csetben az áruház **myshopify címét**, például `modulshop-xyz.myshopify.com`. Ez nem titkos. A Shopify adminban a *Beállítások → Domainek* alatt találod.
7. Szólj, és megjelenik az űrlap, oda illeszd be a `shptka_…` jelszót.

**Visszavonás:** a Theme Access appban bármikor törölheted a jelszót.

**Átadás a cégnek:** ha az áruház a te fiókodon van, később a *Beállítások → Felhasználók → Tulajdonjog átruházása* alatt adhatod át a modulshopnak. A sablon ezzel együtt átkerül.

**Termékek, kategóriák, oldalak:** ezeket nem a sablon tartalmazza. A termékekhez Shopify-formátumú CSV-t készítek, ezt az adminban a *Termékek → Importálás* menüpontban egy kattintással feltöltheted. Ha később teljesen automatikus költöztetés kell (menük, oldalak, átirányítások), arról külön útmutatót írok.

---

## 2. Meta (Facebook + Instagram) – Graph API token

A Facebook bejelentkezés nélkül nem enged robotot az oldalakra, a bejelentkezés megkerülése pedig tilos és kockázatos is. A hivatalos és biztonságos út a **Meta Graph API**: egy csak olvasási jogú token, amellyel az oldal saját posztjait, fotóit, értékeléseit és az Instagram-posztokat le tudom tölteni.

### Előfeltételek (egyszer kell, a cég segítségével)
- **Adminnak kell lenned a modulshop Facebook-oldalán**, teljes hozzáféréssel. A cég ezt a **Meta Business Suite → Beállítások → Személyek / Oldalhozzáférés** alatt adhatja meg neked.
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
| | Shopify Theme Access | Meta oldaltoken |
|---|---|---|
| Látom | sablonfájlok | az oldal posztjai, fotói, értékelései; Instagram-posztok |
| Nem látom | rendelések, vásárlók, fizetés, beállítások | privát üzenetek, a személyes profilod, hirdetési fiók |
| Módosíthatok | csak sablont, közzététel nélkül | semmit (csak olvasás) |

A kulcsok ennek a felhőkörnyezetnek a hálózati titkai között tárolódnak. A projekt végén a környezet beállításaiban törölhetők.
