# Horizon v4.5.0 – technikai térkép (a módosításokhoz)

## Színek
- Nincs `color_schemes`, csak **egy paletta**: `config/settings_schema.json:59-71` (`color_palette`), értékek: `config/settings_data.json`.
- CSS-változók: `snippets/color-palette.liquid:165-237` → `:root{--color-background(-rgb), --color-foreground(-rgb), --color-border, --color-primary/secondary-button-*, --color-input-*, --color-variant-*, --color-foreground-muted/subdued, shadows}` + `body{}`.
- A hover-színeket Liquid számolja (`util-palette-hover-shift`); a `--opacity-*` értékek a háttér fényességétől függnek (`snippets/brightness-opacities.liquid:17-30`).
- Szekciónkénti szín: `background_color`/`text_color` → `snippets/contrast-override.liquid` (`.color-custom-{id}` újradefiniálja a változókat). **Sötét módban ezeket felül kell írni**, vagy a szekciószíneket üresen kell hagyni.
- Fejléc soronkénti színei: `sections/header.liquid:1712-1724`, inline `--color-background-top-row/bottom-row` (360-361). `meta theme-color`: `snippets/meta-tags.liquid:16-19`.

## Tipográfia, betöltés
- `snippets/theme-styles-variables.liquid`: font-face 45-121, `--font-*` 162-174, típusméretek 239-348, `--padding-*`/`--gap-*` 404-441, lekerekítések 446-455, animációk 467-510, gombok 562-590.
- `assets/base.css` (body 5, :root 15). A stíluslapokat a `snippets/stylesheets.liquid` tölti be.
- A `layout/theme.liquid` `<head>` sorrendje (18-31): view-transition-opt-in, meta-tags, stylesheets, card-hover, scripts, theme-styles-variables, color-palette, theme-editor, content_for_header.
- Body: header-group 40-42, main 137-146, footer-group 148-150, drawerek és modalok 153-160.

## Fejléc
- `sections/header-group.json`: `header-announcements` + `header`.
- `sections/header.liquid`: actions capture 102-104, search 134-150, `<header-component>` 338.
- Ikonok: `snippets/header-actions.liquid` (account 86-112, a kosár gombja ~116). **A témaváltó kapcsoló ide kerül**, a kosár elé; mobilon a `snippets/header-drawer.liquid`-be is.
- Menü: `blocks/_header-menu.liquid`; mobilos menü (drawer): `snippets/header-drawer.liquid`.

## JS
- `assets/component.js`: `Component` osztály, `ref=""` → `this.refs`, deklaratív események: `on:click="method"`.
- Új komponens: `import { Component } from '@theme/component'`; `customElements.define`. Az import map a `snippets/scripts.liquid:7-41`-ben van.
- `assets/utilities.js`: `startViewTransition` (118), `supportsViewTransitions` (39), `prefersReducedMotion` (273).
- Nincs semmilyen meglévő sötét mód vagy `prefers-color-scheme` kezelés.

## Sablonok
- index: hero, product-list | collection: section, main-collection | product: product-information, product-recommendations | cart: main-cart, product-list | page.contact: main-page + contact-form | 404, password, search, blog, article, list-collections.
- Szekciók: carousel, collection-list, collection-links, featured-blog-posts, hero, slideshow, marquee, media-with-content, product-list, section (FAQ, multicolumn, icons-with-text, image-with-text, pull_quote, email_signup, contact_form presetek).
- **Nincs vásárlói vélemény (testimonial) blokk**: sajátot kell készíteni. A `blocks/review.liquid` csak a termék csillagos értékelését mutatja.

## Nyelv
- Van `locales/hu.json` (storefront). Nincs `hu.schema.json` (az editor angol).

## Buktatók
- A `settings_data.json`, a `*-group.json` és a `templates/*.json` fájlokat az editor felülírja. Élő boltnál push előtt `shopify theme pull`.
- Az egyedi kód **új fájlokba** kerül (`assets/ms-*.css|js`, `snippets/ms-*`), hogy a Horizon-frissítések könnyen összefésülhetők legyenek.
- Sötét mód: `html[data-theme=dark]` változófelülírások; inline head-script a villanás ellen; `color-scheme`; meta theme-color frissítése.
