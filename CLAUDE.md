# Modulshop.hu – Horizon theme redesign

A ShopRenterről Shopifyra költöző **modulshop.hu** (elektronikai alkatrészek, modulok, kiegészítők) új, egyedi Shopify sablonja, a Shopify **Horizon v4.5.0** sablonra építve. A modulshop engedélyével készül, nekik.

## Célok (prioritási sorrendben)
1. Felhasználóbarát, átlátható, könnyen kezelhető (vásárlónak és a bolt adminjának is).
2. Jól konvertál: bizalomépítés, egyértelmű CTA-k, gyors termékkeresés.
3. Reszponzív: mobil, tablet, asztali gép.
4. **Világos + sötét mód**, kapcsolóval, animált átmenettel.
5. Költözés: minden oldal meglegyen, ami egy működő bolthoz kell (főoldal, kategória, termék, kereső, kosár, fiók, blog, Rólunk, kapcsolat, GYIK, szállítás/fizetés, ÁSZF, adatvédelem, garancia/elállás, 404, jelszó).

## Kemény szabályok
- Magyar nyelv, HUF.
- **Csak valódi tartalom**: vélemény, adat vagy állítás csak forrással szerepelhet (`docs/research/*`). Semmit nem találunk ki.
- Bejelentkezést igénylő oldalakat nem scrapelünk, és nem kerülünk meg botvédelmet. Facebook/Instagram csak a hivatalos Graph API-n át, a felhasználó által adott tokennel.
- Modellnevet nem írunk commitba vagy PR-ba.

## Munkamódszer (kontextus- és tokentakarékosság)
- **Ez a fájl a projekt memóriája.** A döntések a `docs/decisions.md`-be, a kutatási eredmények a `docs/research/`-be kerülnek. Ne kutassunk újra azt, ami már ott van.
- Nagy kutatási vagy áttekintő feladat → háttér-subagent, amely fájlba ír, és csak rövid összefoglalót ad vissza.
- A Horizon fájljait célzottan olvassuk (`grep`, `sed -n`). A sablon felépítéséről a `docs/horizon-notes.md` szól.
- A letöltések és a nyers HTML a scratchpadba kerülnek, nem a repóba. A repóba csak a végleges, optimalizált képek mennek (`assets/`).
- Parancskimenetet mindig vágunk (`head`, `wc`, `-o`).

## Kulcsfájlok
- `docs/research/site-analysis.md` – a jelenlegi modulshop.hu elemzése
- `docs/research/reviews.md` – valódi vélemények forrással
- `docs/research/brand-and-presence.md` – közösségi média, arculat, elérhetőségek
- `docs/horizon-notes.md` – a Horizon felépítése: hova kell nyúlni
- `docs/decisions.md` – dizájn- és technikai döntések
- `docs/setup-access.md` – útmutató a Shopify- és Meta-hozzáféréshez

## Shopify
- Éles (nem dev) áruház, amely átadható a cégnek. Feltöltés Shopify CLI-vel, Theme Access jelszóval (`shopify theme push --unpublished`). Az élő sablont soha nem írjuk felül.
- A `docs/` és a `CLAUDE.md` nem része a sablonnak; a `.shopifyignore` kizárja őket.
