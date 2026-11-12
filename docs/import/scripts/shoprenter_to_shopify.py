#!/usr/bin/env python3
"""ShopRenter (modulshop.hu) -> Shopify migration helper.

Standard library only. Run it isolated:  python3 -I shoprenter_to_shopify.py ...
All HTTP goes through plain `curl` (subprocess), with a fixed, honest
User-Agent, no login, and at most 1 request per second (MIN_INTERVAL).

Subcommands
-----------
  products   Fetch ShopRenter product pages and write a Shopify product CSV.
             Input: product URLs (args and/or --url-file), or explicitly
             --all-from-sitemap (the 0.6-priority URLs = the full catalog;
             about 1856 requests, ~35 min - only run it deliberately).
  redirects  Build the Shopify URL-redirect CSV (Redirect from,Redirect to)
             for every URL in the sitemap.
  clean      Clean a ShopRenter HTML fragment/file to simple semantic HTML
             (helper used for pages / collection descriptions).

Examples
--------
  python3 -I shoprenter_to_shopify.py products --url-file urls.txt \
      --sitemap sitemap.xml --cache-dir RAW/products --out products.csv \
      --ids-out product_ids.json --verify-images
  python3 -I shoprenter_to_shopify.py redirects --sitemap sitemap.xml \
      --ids product_ids.json --out redirects.csv

Cached HTML in --cache-dir is reused (each page is fetched once); pass
--refresh to download again (e.g. for fresh stock numbers before go-live).
"""

import argparse
import csv
import html
import json
import os
import re
import subprocess
import sys
import time
import unicodedata
from html.parser import HTMLParser

BASE = "https://modulshop.hu"
UA = "modulshop-shopify-migration/1.0 (curl; owner-authorised data export)"
MIN_INTERVAL = 1.1  # seconds between requests (<= 1 request / second)

# ---------------------------------------------------------------------------
# Category table (ShopRenter path -> Shopify product type / tag / handle)
# Type  = main collection name (kept exactly as on the current site).
# Tag   = subcategory name; commas are not allowed in Shopify tags, so they
#         are replaced by " / "; obvious typos of the old names are fixed
#         (see collections.md for the list of changes).
# ---------------------------------------------------------------------------
MAIN = {
    "/mikrovezerlok-alaplapok-157": ("Mikrovezérlők, alaplapok", "mikrovezerlok-alaplapok"),
    "/szenzor-modulok-158": ("Szenzor Modulok", "szenzor-modulok"),
    "/egyeb-modulok-159": ("Egyéb Modulok", "egyeb-modulok"),
    "/erositok-vegfokok-160": ("Erősítők, Végfokok", "erositok-vegfokok"),
    "/lcd-k-kijelzok-161": ("LCD-k, Kijelzők", "lcd-k-kijelzok"),
    "/bms-ek-18650-akkuk-162": ("BMS-ek, 18650 Akkuk", "bms-ek-18650-akkuk"),
    "/dc-ac-konverterek-163": ("DC, AC konverterek", "dc-ac-konverterek"),
    "/muszerek-164": ("Műszerek", "muszerek"),
    "/egyeb-165": ("Egyéb", "egyeb"),
    "/elektronika-177": ("Elektronika", "elektronika"),
    "/diy-keszletek-225": ("D.I.Y. Készletek", "diy-keszletek"),
    "/led-vilagitas-197": ("Led világítás", "led-vilagitas"),
}
# Featured (tag-based) collections: not product types, membership via tag.
FEATURED = {
    "/sajat-termekeink-244": ("Saját termék", "sajat-termekeink"),
    "/csomagok-190": ("Csomag", "csomagok"),
}
SUB = {
    "/mikrovezerlok-alaplapok-157/avr-duino": ("Arduino", "arduino"),
    "/mikrovezerlok-alaplapok-157/esp-167": ("ESP8266", "esp8266"),
    "/mikrovezerlok-alaplapok-157/esp32-205": ("ESP32", "esp32"),
    "/mikrovezerlok-alaplapok-157/stm-168": ("STM", "stm"),
    "/mikrovezerlok-alaplapok-157/raspberry-208": ("Raspberry", "raspberry"),
    "/szenzor-modulok-158/homerseklet-para-nyomas-184": ("Hőmérséklet / pára / nyomás", "homerseklet-para-nyomas"),
    "/szenzor-modulok-158/feszultseg-aram-tavolsag-185": ("Feszültség / áram / távolság", "feszultseg-aram-tavolsag"),
    "/szenzor-modulok-158/feny-mozgas-erzekeles-186": ("Fény / mozgás / giro / gyorsulás / RFID érzékelés", "feny-mozgas-giro-gyorsulas-rfid"),
    "/egyeb-modulok-159/beviteli-eszkozok-189": ("Beviteli eszközök", "beviteli-eszkozok"),
    "/egyeb-modulok-159/komunikacios-modulok-187": ("Kommunikációs modulok", "kommunikacios-modulok"),
    "/egyeb-modulok-159/motork-dc-lepteto-szervo-192": ("Motor / DC / léptető / szervó", "motor-dc-lepteto-szervo"),
    "/egyeb-modulok-159/motor-vezerlok-188": ("Motorvezérlők", "motorvezerlok"),
    "/egyeb-modulok-159/probapanelekshieldekegyeb-196": ("Próbapanelek / shieldek / egyéb", "probapanelek-shieldek"),
    "/egyeb-modulok-159/relek-211": ("Relék / optocsatolók", "relek-optocsatolok"),
    "/erositok-vegfokok-160/100w-folotti-21-171": ("100W fölötti + 2.1", "100w-folotti-erositok"),
    "/erositok-vegfokok-160/250w-erositovegfok-170": ("2*50W erősítő / végfok", "2x50w-erositok-vegfokok"),
    "/erositok-vegfokok-160/audio-kiegeszitok-173": ("Audió kiegészítők", "audio-kiegeszitok"),
    "/erositok-vegfokok-160/hangszoro-222": ("Hangszóró", "hangszorok"),
    "/bms-ek-18650-akkuk-162/1s-5s-bms-169": ("1S - 5S BMS", "1s-5s-bms"),
    "/bms-ek-18650-akkuk-162/akku-cellak-elemek-236": ("Akku cellák / elemek", "akku-cellak-elemek"),
    "/bms-ek-18650-akkuk-162/6s-13s-bms-172": ("6S - 13S BMS", "6s-13s-bms"),
    "/bms-ek-18650-akkuk-162/akku-toltok-175": ("Akku töltők", "akku-toltok"),
    "/bms-ek-18650-akkuk-162/egyeb-176": ("BMS kiegészítők", "bms-kiegeszitok"),
    "/dc-ac-konverterek-163/dc-tapegysegek-194": ("AC-DC tápegységek / labortáp", "ac-dc-tapegysegek-labortap"),
    "/dc-ac-konverterek-163/dc-dc-step-down-feszcsokkento-181": ("DC-DC step down / feszültségcsökkentő", "dc-dc-step-down"),
    "/dc-ac-konverterek-163/dc-dc-step-up-fesznovelo-182": ("DC-DC step up / feszültségnövelő", "dc-dc-step-up"),
    "/muszerek-164/muszerdobozok-227": ("Műszerdobozok", "muszerdobozok"),
    "/egyeb-165/szerszamok-220": ("Szerszámok", "szerszamok"),
    "/elektronika-177/ellenallasok-potmeterek-180": ("Ellenállások / potméterek", "ellenallasok-potmeterek"),
    "/elektronika-177/fizika-ora-aramkori-elemek-203": ("Fizika óra / áramköri elemek", "fizika-ora-aramkori-elemek"),
    "/elektronika-177/csatlakozok-vezetekek-202": ("Hűtőbordák / ventilátorok", "hutobordak-ventilatorok"),
    "/elektronika-177/ic-178": ("IC", "ic"),
    "/elektronika-177/kapcsolok-csatlakozok-vezetekek-200": ("Kapcsolók / csatlakozók / vezetékek", "kapcsolok-csatlakozok-vezetekek"),
    "/elektronika-177/kondenzatorok-195": ("Kondenzátorok / diódák", "kondenzatorok-diodak"),
    "/elektronika-177/ledek-183": ("Ledek", "ledek"),
    "/elektronika-177/pcb-nyaklapok-forrasztasi-anyagok-193": ("PCB nyáklapok / forrasztási anyagok", "pcb-nyaklapok-forrasztasi-anyagok"),
    "/elektronika-177/tranzisztor-mosfet-179": ("Tranzisztor / MOSFET", "tranzisztor-mosfet"),
    "/diy-keszletek-225/csavarok-betetek-239": ("Csavarok / betétek", "csavarok-betetek"),
    "/diy-keszletek-225/tavtartok-237": ("Távtartók", "tavtartok"),
}
# Other category-like URLs (redirect targets only)
OTHER_CAT = {
    "/csomag-ajanlataink-242": "/collections/csomagok",
    "/csomag-ajanlataink-101": "/collections/csomagok",
    "/osszes-termek-191": "/collections/all",
    "/modulshop-m-32": "/collections/vendors?q=Modulshop",
}
# Information pages / blog (sitemap priority 0.3) -> new path.
INFO = {
    "/husegpont-rendszer-85": "/pages/husegpont",
    "/ingyenes-visszakuldes-77": "/pages/garancia-es-visszakuldes",
    "/30-napos-termek-visszakuldes-38": "/pages/garancia-es-visszakuldes",
    "/kereses": "/search",
    "/index.php?route=product/list&latest=52": "/collections/all?sort_by=created-descending",
    "/index.php?route=product/list&special=1": "/collections/all",
    "/mesterseges-intelligencia-ai-hasznalati-szabalyzat-115": "/pages/ai-hasznalati-szabalyzat",
    "/withdrawal": "/pages/elallas",
    "/regisztracio-87": "/account/register",
    "/szallitasi-informaciok-65": "/pages/szallitas-es-fizetes",
    "/szallitasi-modok-71": "/pages/szallitas-es-fizetes",
    "/gyakran-ismetelt-kerdesek-36": "/pages/gyik",
    "/adatvedelmi-nyilatkozat-44": "/pages/adatvedelem",
    "/adatvedelem-45": "/pages/aszf",  # this old URL holds the ÁSZF
    "/vasarlasi-feltetelek-5": "/pages/aszf",  # outdated terms, superseded by ÁSZF
    "/kapcsolat-32": "/pages/kapcsolat",
    "/rolunk-51": "/pages/rolunk",
    # blog lists (ShopRenter information lists) -> the single Shopify blog
    "/almodd-meg-otleted-es-valositsd-meg-2": "/blogs/news",
    "/hirek-3": "/blogs/news",
    "/hasznos-dolgok-4": "/blogs/news",
    "/uj-termekeink-7": "/blogs/news",
    "/egyedi-muszerdobozok-10": "/blogs/news",
    "/tankbot-8": "/blogs/news",
    "/arduino-vagy-esp32-99": "/blogs/news",
    # blog posts (handles: old slug without id; broken slugs -> title-based)
    "/modulshop-projekt-verseny-79": "/blogs/news/modulshop-projekt-verseny",
    "/httpsmodulshophunodemcu-autos-kit-wifi-iot-761-58": "/blogs/news/nodemcu-autos-kit-wifi-iot",
    "/nodemcu-autos-kit-wifi-iot-60": "/blogs/news/nodemcu-autos-kit-wifi-iot",
    "/dekoracio-led-szalaggal-61": "/blogs/news/dekoracio-led-szalaggal",
    "/httpswwwmodulshophublogerosito-modulok-elektronikai-projektekhezhttpswwwmodulshophublogerosito-modulok-elektronikai-projektekhez": "/blogs/news/erosito-modulok-elektronikai-projektekhez",
    "/esp32-mi-az-es-hogyan-mukodik": "/blogs/news/esp32-mi-az-es-hogyan-mukodik",
    "/fnirsi-meromuszerek-oszcilloszkopok-teszterek": "/blogs/news/fnirsi-meromuszerek-oszcilloszkopok-teszterek",
    "/kozepiskolai-project-1-59": "/blogs/news/irfz44-mosfet-teszt-arduinoval",
    "/egyedi-muszerdoboz-tervezes": "/blogs/news/egyedi-muszerdoboz-tervezes",
    "/almodd-meg-otleted-es-valositsd-meg-2/robot-exatlon-nyiregyhaza-altalanos-iskolas-verseny": "/blogs/news/robot-exatlon-nyiregyhaza-altalanos-iskolas-verseny",
    "/vonalkoveto-robot-arduino-alapok": "/blogs/news/vonalkoveto-robot-arduino-alapok",
    "/soft-starter-kicsi-egyszeru-es-hatekony-74": "/blogs/news/soft-starter-kicsi-egyszeru-es-hatekony",
    "/tankbot-v10-105": "/blogs/news/tankbot-v10",
    "/raspberry-pi-pico2-80": "/blogs/news/raspberry-pi-pico2",
}

CSV_COLUMNS = [
    "Handle", "Title", "Body (HTML)", "Vendor", "Product Category", "Type", "Tags",
    "Published", "Option1 Name", "Option1 Value", "Variant SKU", "Variant Grams",
    "Variant Inventory Tracker", "Variant Inventory Qty", "Variant Inventory Policy",
    "Variant Fulfillment Service", "Variant Price", "Variant Compare At Price",
    "Variant Requires Shipping", "Variant Taxable", "Variant Barcode", "Image Src",
    "Image Position", "Image Alt Text", "SEO Title", "SEO Description", "Status",
]

# ---------------------------------------------------------------------------
# HTTP (plain curl, rate limited)
# ---------------------------------------------------------------------------
_last_request = [0.0]


def curl(url, out_path=None, head=False):
    """Run plain curl. Returns (http_code:int, body:str|None)."""
    wait = MIN_INTERVAL - (time.time() - _last_request[0])
    if wait > 0:
        time.sleep(wait)
    cmd = ["curl", "-sS", "--max-time", "60", "-A", UA, "-o",
           out_path if out_path else os.devnull, "-w", "%{http_code}"]
    if head:
        cmd.append("-I")
    cmd.append(url)
    try:
        res = subprocess.run(cmd, capture_output=True, text=True, timeout=90)
    finally:
        _last_request[0] = time.time()
    code = res.stdout.strip()[-3:]
    try:
        code = int(code)
    except ValueError:
        code = 0
    if res.returncode != 0:
        sys.stderr.write("curl error %s for %s: %s\n" % (res.returncode, url, res.stderr.strip()))
    return code


def fetch_cached(url, cache_dir, refresh=False):
    os.makedirs(cache_dir, exist_ok=True)
    name = re.sub(r"[^A-Za-z0-9._-]+", "_", url.split("://", 1)[-1].split("/", 1)[-1] or "index")
    name = (name[:150] or "index") + ".html"
    path = os.path.join(cache_dir, name)
    if refresh or not os.path.exists(path) or os.path.getsize(path) == 0:
        tmp = path + ".part"
        code = curl(url, tmp)
        if code != 200:
            if os.path.exists(tmp):
                os.remove(tmp)
            raise RuntimeError("HTTP %s for %s" % (code, url))
        os.replace(tmp, path)
    with open(path, encoding="utf-8", errors="replace") as fh:
        return fh.read()


# ---------------------------------------------------------------------------
# Slugs / handles
# ---------------------------------------------------------------------------
def hu_ascii_slug(text):
    """Hungarian-ASCII slug: á->a, ő->o, ű->u ..., lowercase, [a-z0-9-]."""
    text = unicodedata.normalize("NFKD", text)
    text = "".join(c for c in text if not unicodedata.combining(c))
    text = text.lower()
    text = re.sub(r"[^a-z0-9]+", "-", text)
    return re.sub(r"-{2,}", "-", text).strip("-")


def url_path(url):
    url = html.unescape(url.strip())
    if url.startswith(BASE):
        url = url[len(BASE):]
    return url or "/"


def base_handle(url, product_id=None):
    """Old slug without the trailing ShopRenter id.

    If the product id is known (from the page), only "-<id>" is stripped.
    Otherwise heuristic: a trailing 3-4 digit number without leading zero
    is treated as the id (e.g. -1789), 1-2 digit or 5+ digit endings are
    part of the name (e.g. -22, -803450)."""
    slug = url_path(url).rstrip("/").rsplit("/", 1)[-1]
    if product_id:
        if slug.endswith("-%s" % product_id):
            slug = slug[: -(len(str(product_id)) + 1)]
    else:
        m = re.search(r"-([1-9]\d{2,3})$", slug)
        if m:
            slug = slug[: m.start()]
    return hu_ascii_slug(slug)


def build_handle_map(urls, ids=None):
    """url -> unique handle. Colliding handles (e.g. the blue/white variants
    096-oled-...-733 / -986) keep their full old slug, for every member of
    the collision group (order independent)."""
    ids = ids or {}
    base = {u: base_handle(u, ids.get(u)) for u in urls}
    groups = {}
    for u, h in base.items():
        groups.setdefault(h, []).append(u)
    result = {}
    for h, members in groups.items():
        if len(members) == 1:
            result[members[0]] = h
        else:
            for u in members:
                result[u] = hu_ascii_slug(url_path(u).rsplit("/", 1)[-1])
    return result


def read_sitemap(src):
    if re.match(r"https?://", src):
        import tempfile
        fd, tmp = tempfile.mkstemp(suffix=".xml")
        os.close(fd)
        if curl(src, tmp) != 200:
            raise RuntimeError("could not download %s" % src)
        src = tmp
    with open(src, encoding="utf-8") as fh:
        t = fh.read()
    out = []
    for block in re.findall(r"<url>(.*?)</url>", t, re.S):
        loc = re.search(r"<loc>\s*(.*?)\s*</loc>", block, re.S)
        pr = re.search(r"<priority>\s*(.*?)\s*</priority>", block, re.S)
        if loc:
            out.append((html.unescape(loc.group(1)), pr.group(1) if pr else ""))
    return out


# ---------------------------------------------------------------------------
# HTML cleaning: ShopRenter WYSIWYG markup -> simple semantic HTML
# ---------------------------------------------------------------------------
BLOCKS = {"p", "h2", "h3", "h4", "ul", "ol", "li", "table", "thead", "tbody",
          "tr", "th", "td", "blockquote"}
INLINE = {"strong", "em", "a", "br", "sub", "sup", "img"}
RENAME = {"b": "strong", "i": "em", "u": "strong", "h1": "h2", "h5": "h4", "h6": "h4"}
DROP_WITH_CONTENT = {"script", "style", "noscript", "svg", "form", "iframe", "button",
                     "input", "textarea", "select", "fieldset", "video", "object",
                     "template", "head", "title"}
VOID = {"br", "img", "hr", "input", "meta", "link", "wbr", "col", "source"}
TEXTBLOCK = {"p", "h2", "h3", "h4"}


class _Node(object):
    __slots__ = ("tag", "attrs", "children")

    def __init__(self, tag, attrs=None):
        self.tag = tag
        self.attrs = attrs or {}
        self.children = []


class _Cleaner(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self, convert_charrefs=True)
        self.root = _Node("root")
        self.stack = [self.root]
        self.skip = 0

    @property
    def cur(self):
        return self.stack[-1]

    def _close(self, tag):
        for i in range(len(self.stack) - 1, 0, -1):
            if self.stack[i].tag == tag:
                del self.stack[i:]
                return True
        return False

    def handle_starttag(self, tag, attrs):
        tag = tag.lower()
        if self.skip:
            if tag in DROP_WITH_CONTENT and tag not in VOID:
                self.skip += 1
            return
        if tag in DROP_WITH_CONTENT:
            if tag not in VOID:
                self.skip = 1
            return
        tag = RENAME.get(tag, tag)
        a = dict(attrs)
        if tag in BLOCKS:
            # a text block cannot contain other blocks
            if any(n.tag in TEXTBLOCK for n in self.stack[1:]) and tag not in ("li",):
                for t in TEXTBLOCK:
                    self._close(t)
            if tag in TEXTBLOCK:
                for t in TEXTBLOCK:
                    self._close(t)
            if tag == "li":
                for i in range(len(self.stack) - 1, 0, -1):
                    if self.stack[i].tag in ("ul", "ol"):
                        break
                    if self.stack[i].tag == "li":
                        del self.stack[i:]
                        break
            if tag in ("tr",):
                self._close("tr")
            if tag in ("td", "th"):
                for t in ("td", "th"):
                    self._close(t)
            keep = {}
            if tag in ("td", "th"):
                for k in ("colspan", "rowspan"):
                    if a.get(k, "").isdigit():
                        keep[k] = a[k]
            node = _Node(tag, keep)
            self.cur.children.append(node)
            self.stack.append(node)
        elif tag in INLINE:
            keep = {}
            if tag == "a":
                href = (a.get("href") or "").strip()
                if re.match(r"(https?:|mailto:|tel:|/)", href):
                    keep["href"] = href
            if tag == "img":
                src = (a.get("src") or "").strip()
                if not re.match(r"https?://", src):
                    return
                keep["src"] = src
                keep["alt"] = (a.get("alt") or "").strip()
            node = _Node(tag, keep)
            self.cur.children.append(node)
            if tag not in VOID:
                self.stack.append(node)
        # everything else (div, span, font, article, section, hr ...) is unwrapped/dropped

    def handle_startendtag(self, tag, attrs):
        self.handle_starttag(tag, attrs)
        if tag.lower() not in VOID:
            self.handle_endtag(tag)

    def handle_endtag(self, tag):
        tag = tag.lower()
        if self.skip:
            if tag in DROP_WITH_CONTENT:
                self.skip -= 1
            return
        tag = RENAME.get(tag, tag)
        if tag in BLOCKS or (tag in INLINE and tag not in VOID):
            self._close(tag)

    def handle_data(self, data):
        if self.skip:
            return
        self.cur.children.append(data)


def _is_blank(node):
    if isinstance(node, str):
        return not node.strip()
    if node.tag == "img":
        return False
    if node.tag == "br":
        return True
    return all(_is_blank(c) for c in node.children)


def _serialize(node, out):
    if isinstance(node, str):
        node = re.sub("[\u200b\u200c\u200d\ufeff\u00ad]", "", node)
        out.append(html.escape(re.sub(r"\s+", " ", node), quote=False))
        return
    if node.tag == "root":
        for c in node.children:
            _serialize(c, out)
        return
    if node.tag in INLINE and node.tag != "br" and node.tag != "img" and _is_blank(node):
        # drop empty <strong></strong> etc. but keep their whitespace
        out.append(" ")
        return
    if node.tag in BLOCKS and node.tag not in ("td", "th") and _is_blank(node):
        return
    attrs = "".join(' %s="%s"' % (k, html.escape(v, quote=True)) for k, v in node.attrs.items())
    if node.tag in ("br", "img"):
        out.append("<%s%s>" % (node.tag, attrs))
        return
    out.append("<%s%s>" % (node.tag, attrs))
    for c in node.children:
        _serialize(c, out)
    out.append("</%s>" % node.tag)


def _wrap_inline(root):
    """Wrap inline runs that sit directly in root/blockquote into <p>."""
    def fix(container):
        new, run = [], []

        def flush():
            if run and not all(_is_blank(x) for x in run):
                p = _Node("p")
                p.children = list(run)
                new.append(p)
            run[:] = []
        for c in container.children:
            if isinstance(c, str) or c.tag in INLINE:
                run.append(c)
            else:
                flush()
                new.append(c)
                if c.tag == "blockquote":
                    fix(c)
        flush()
        container.children = new
    fix(root)


_DASH = re.compile(r"^\s*(?:[-–•*·]|&gt;)\s*")


def _p_to_lists(m):
    inner = m.group(1)
    segs = [s.strip() for s in re.split(r"(?:<br>\s*)+", inner)]
    segs = [s for s in segs if s and s != " "]
    if not segs:
        return ""
    dash = [bool(_DASH.match(s)) and len(_DASH.sub("", s)) > 0 for s in segs]
    if sum(dash) < 2:
        # only split paragraphs on double line breaks
        parts = [s.strip() for s in re.split(r"<br>\s*(?:<br>\s*)+", inner)]
        return "".join("<p>%s</p>" % s for s in parts if s.strip())
    out, items = [], []
    for s, d in zip(segs, dash):
        if d:
            items.append(_DASH.sub("", s))
        else:
            if items:
                out.append("<ul>%s</ul>" % "".join("<li>%s</li>" % i for i in items))
                items = []
            out.append("<p>%s</p>" % s)
    if items:
        out.append("<ul>%s</ul>" % "".join("<li>%s</li>" % i for i in items))
    return "".join(out)


def clean_html(fragment):
    """ShopRenter WYSIWYG HTML -> simple semantic HTML (p, h2-h4, ul/ol/li,
    strong/em, a, table, blockquote, br, img). Styles, classes, spans, fonts,
    hr and forms are removed; '-' prefixed lines become lists."""
    p = _Cleaner()
    p.feed(fragment)
    p.close()
    _wrap_inline(p.root)
    out = []
    _serialize(p.root, out)
    s = "".join(out)
    # whitespace tidy
    s = re.sub(r"\s*(<br>)\s*", r"\1", s)
    s = re.sub(r"<(p|h2|h3|h4|li|td|th)>\s*(?:<br>\s*)*", r"<\1>", s)
    s = re.sub(r"(?:\s*<br>)*\s*</(p|h2|h3|h4|li|td|th)>", r"</\1>", s)
    s = re.sub(r"<p>(.*?)</p>", _p_to_lists, s, flags=re.S)
    s = re.sub(r"<(strong|em)>\s*</\1>", " ", s)
    s = s.replace("</strong><strong>", "</strong> <strong>")
    for _ in range(3):
        s = re.sub(r"<(strong|em)>\s*<\1>(.*?)</\1>\s*</\1>", r"<\1>\2</\1>", s, flags=re.S)
        # a heading does not need bold
        s = re.sub(r"<(h2|h3|h4)>\s*<strong>([^<]*)</strong>\s*</\1>", r"<\1>\2</\1>", s)
    # leading list dash left in front of headings / bold lines
    s = re.sub(r"<(h2|h3|h4|p)>(<strong>)?\s*-\s*(?=[^\d\s])", r"<\1>\2", s)
    s = re.sub(r"<(p|h2|h3|h4|li)>\s*</\1>", "", s)
    s = re.sub(r" {2,}", " ", s)
    s = re.sub(r">\s+<", "><", s)
    # a single paragraph inside a list item / table cell is unwrapped
    s = re.sub(r"<(li|td|th)([^>]*)><p>((?:(?!</?p>).)*)</p></\1>", r"<\1\2>\3</\1>", s, flags=re.S)
    # readable line breaks between blocks
    s = re.sub(r"(</(?:p|h2|h3|h4|ul|ol|table|blockquote|li|tr|td|th|thead|tbody)>)", r"\1\n", s)
    s = re.sub(r"(<(?:ul|ol|table|thead|tbody|tr|blockquote)>)", r"\1\n", s)
    return "\n".join(line.strip() for line in s.splitlines() if line.strip())


def html_to_text(fragment):
    t = re.sub(r"<br\s*/?>|</p>|</li>|</h\d>", "\n", fragment, flags=re.I)
    t = re.sub(r"<[^>]+>", "", t)
    return html.unescape(t)


# ---------------------------------------------------------------------------
# ShopRenter product page parsing
# ---------------------------------------------------------------------------
def extract_element(doc, open_regex):
    """Return inner HTML of the first element whose opening tag matches."""
    m = re.search(open_regex, doc, re.S)
    if not m:
        return None
    start = doc.rfind("<", 0, m.start() + 1)
    tm = re.match(r"<([a-zA-Z0-9]+)", doc[start:])
    if not tm:
        return None
    tag = tm.group(1).lower()
    open_end = doc.find(">", m.end() - 1)
    if open_end < 0:
        return None
    depth = 1
    pat = re.compile(r"<(/?)%s\b[^>]*?(/?)>" % tag, re.I)
    pos = open_end + 1
    while depth:
        n = pat.search(doc, pos)
        if not n:
            return doc[open_end + 1:]
        if n.group(1):
            depth -= 1
        elif not n.group(2):
            depth += 1
        pos = n.end()
    return doc[open_end + 1:n.start()]


def _attr(tag_html, name):
    m = re.search(r'\s%s="([^"]*)"' % re.escape(name), tag_html)
    return html.unescape(m.group(1)).strip() if m else ""


def _text(fragment):
    return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", fragment or ""))).strip()


def valid_gtin(code):
    if not re.fullmatch(r"\d{8}|\d{12,14}", code):
        return False
    digits = [int(c) for c in code]
    check = digits.pop()
    total = sum(d * (3 if i % 2 == 0 else 1) for i, d in enumerate(reversed(digits)))
    return (10 - total % 10) % 10 == check


def original_image_url(cache_url):
    """ShopRenter cache URL -> original upload URL (image/data/...)."""
    u = cache_url.split("?", 1)[0]
    m = re.match(r"(https://[^/]+/custom/[^/]+/image)/cache/[^/]+/(.+)$", u)
    if not m:
        return u
    path = m.group(2)
    if re.search(r"\.(jpe?g|png|gif)\.webp$", path, re.I):
        path = path[:-5]
    return m.group(1) + "/data/" + path


BOILER_PREFIX = re.compile(r"^\s*(?:\w+\s*-\s*Gyors kiszállítás\s*(?:-\s*|$))?(?:[\d.\s]+Ft\b\s*-?\s*)?", re.I)
BOILER_SUFFIX = re.compile(r"\s*-\s*Modulshop webáruház\s*$", re.I)


def parse_product(doc, url):
    p = {"url": url, "warnings": []}
    m = re.search(r'class="product-page-product-name"[^>]*>(.*?)</span>', doc, re.S)
    p["title"] = _text(m.group(1)) if m else ""
    m = (re.search(r'id="form-element-product_id"\s+value="(\d+)"', doc)
         or re.search(r'name="product_id"[^>]*value="(\d+)"', doc))
    p["product_id"] = m.group(1) if m else None
    m = re.search(r'itemprop="sku" content="([^"]*)"', doc)
    p["sku"] = html.unescape(m.group(1)).strip() if m else ""
    m = re.search(r'itemprop="gtin\d*" content="([^"]*)"', doc)
    p["gtin"] = m.group(1).strip() if m else ""
    if p["gtin"] and not valid_gtin(p["gtin"]):
        p["warnings"].append("invalid GTIN %r (not a GTIN-8/12/13/14) -> left empty" % p["gtin"])
        p["gtin"] = ""
    m = re.search(r'itemprop="price" content="([\d.]+)"', doc)
    p["price"] = m.group(1) if m else ""
    if p["price"].endswith(".00"):
        p["price"] = p["price"][:-3]
    # special price: ShopRenter shows the old (original) price struck through
    p["compare_at"] = ""
    box = extract_element(doc, r'data-test-id="product-page-price"') or ""
    m = re.search(r'class="[^"]*product-price--(?:original|old)[^"]*"[^>]*>(.*?)</', box, re.S)
    if m:
        digits = re.sub(r"[^\d]", "", _text(m.group(1)))
        if digits and p["price"] and int(digits) > float(p["price"]):
            p["compare_at"] = digits
    m = re.search(r'itemprop="availability" href="[^"]*/(\w+)"', doc)
    p["availability"] = m.group(1) if m else ""
    m = re.search(r'class="product-stock__label">(.*?)</span>', doc, re.S)
    p["stock_text"] = _text(m.group(1)) if m else ""
    m = re.search(r"(\d[\d\s]*)\s*db\b", p["stock_text"])
    if m:
        p["qty"] = int(re.sub(r"\s", "", m.group(1)))
    else:
        p["qty"] = 0
        if p["availability"] == "InStock":
            p["warnings"].append("InStock without a quantity (%r) -> qty 0" % p["stock_text"])
    # breadcrumb
    bc = extract_element(doc, r'<ol class="breadcrumb') or ""
    crumbs = []
    for li in re.findall(r'itemprop="itemListElement".*?(?=itemprop="itemListElement"|$)', bc, re.S):
        href = re.search(r'itemprop="item" href="([^"]+)"', li)
        name = re.search(r'itemprop="name"[^>]*>(.*?)</', li, re.S)
        crumbs.append((url_path(href.group(1)) if href else "", _text(name.group(1)) if name else ""))
    p["breadcrumb"] = crumbs
    short = extract_element(doc, r'data-test-id="product-short-description"') or ""
    p["short_html"] = short
    feats = []
    for li in re.findall(r'<li class="product-parameter product-parameter__featured[^"]*">(.*?)</li>', doc, re.S):
        lab = re.search(r'product-parameter__label">(.*?)</span>', li, re.S)
        val = re.search(r'product-parameter__value">(.*?)</span>', li, re.S)
        if lab and val and _text(val.group(1)):
            feats.append((_text(lab.group(1)), _text(val.group(1))))
    p["featured"] = feats
    p["desc_html"] = extract_element(doc, r'class="product-desc[^"]*"\s+itemprop="description"') or ""
    if not _text(p["desc_html"]):
        p["warnings"].append("empty long description")
    # images (main gallery, in order)
    gallery = extract_element(doc, r'<div id="product-image"') or ""
    imgs, seen = [], set()
    for tag in re.findall(r"<img\b[^>]*>", gallery, re.S):
        if 'itemprop="image"' not in tag:
            continue
        src = _attr(tag, "data-popup-src") or _attr(tag, "src")
        key = src.split("?", 1)[0]
        if not src or key in seen:
            continue
        seen.add(key)
        imgs.append({"cache": key, "src": original_image_url(key),
                     "alt": _attr(tag, "alt") or p["title"]})
    if not imgs:
        m = re.search(r'<meta property="og:image" content="([^"]+)"', doc)
        if m:
            key = m.group(1).split("?", 1)[0]
            imgs.append({"cache": key, "src": original_image_url(key), "alt": p["title"]})
            p["warnings"].append("no gallery images, used og:image")
    p["images"] = imgs
    m = re.search(r"<title>(.*?)</title>", doc, re.S)
    t = _text(m.group(1)) if m else p["title"]
    t = re.sub(r"^Modulshop\s*-\s*", "", t)
    t = re.sub(r"\s*-\s*[\d.\s]+Ft\s*$", "", t)  # price in <title> would go stale
    t = BOILER_PREFIX.sub("", t).strip(" -")
    p["seo_title"] = t if len(t) > 3 else p["title"]
    m = re.search(r'<meta name="description" content="([^"]*)"', doc, re.S)
    d = _text(m.group(1)) if m else ""
    d = BOILER_SUFFIX.sub("", BOILER_PREFIX.sub("", d)).strip(" -")
    if re.search(r"\d[\d.\s]*\s*Ft-os áron", d):
        d = ""  # ShopRenter default template with the price in it -> would go stale
    p["seo_desc"] = d
    # manufacturer, only when explicitly stated ("Gyártó: X")
    txt = html_to_text(short + "\n" + p["desc_html"])
    m = re.search(r"Gyártó\s*:\s*([^\n,;]{2,40})", txt)
    p["manufacturer"] = m.group(1).strip(" .-") if m else ""
    return p


def categorize(p, members):
    """Type = main collection, Tags = subcategory names (+ featured tags).

    Primary source: the product page breadcrumb. Additional/fallback source:
    category membership, either crawled (--crawl-categories,
    --featured-category) or given as hints (--category-hints)."""
    main_type, tags = "", []
    paths = [path for path, _ in p["breadcrumb"][1:]]
    me = url_path(p["url"])
    for cat_path, urls in members.items():
        if me in urls and cat_path not in paths:
            paths.append(cat_path)
    names = dict(p["breadcrumb"])
    for path in paths:
        if not path or path == "/" or path == me or path in OTHER_CAT:
            continue  # home, the product itself, "Összes termék" etc.
        if path in MAIN:
            main_type = main_type or MAIN[path][0]
        elif path in SUB:
            main_type = main_type or MAIN.get("/" + path.strip("/").split("/")[0], ("", ""))[0]
            if SUB[path][0] not in tags:
                tags.append(SUB[path][0])
        elif path in FEATURED:
            if FEATURED[path][0] not in tags:
                tags.append(FEATURED[path][0])
        else:
            p["warnings"].append("unknown category: %s (%s)" % (path, names.get(path, "")))
            tag = re.sub(r"\s*\(\d+\)$", "", names.get(path, "")).replace(",", " /").strip()
            if tag and tag not in tags:
                tags.append(tag)
    if not main_type:
        p["warnings"].append("no main category (breadcrumb: %s) -> Type empty, set it manually"
                             % " > ".join(n for _, n in p["breadcrumb"]))
    return main_type, tags


def build_body(p):
    parts = []
    desc = clean_html(p["desc_html"])
    short = clean_html(p["short_html"])
    norm = lambda s: re.sub(r"\W+", "", _text(s)).lower()
    if short and norm(short) not in norm(desc):
        parts.append(short)
    if p["featured"]:
        parts.append("<ul>\n" + "\n".join(
            "<li><strong>%s:</strong> %s</li>" % (html.escape(k, quote=False), html.escape(v, quote=False))
            for k, v in p["featured"]) + "\n</ul>")
    if desc:
        parts.append(desc)
    return "\n".join(parts)


def crawl_category(path, cache_dir, refresh=False, max_pages=40):
    """Return set of product paths listed in a category (all pages)."""
    members = set()
    for page in range(1, max_pages + 1):
        url = BASE + path + ("?page=%d" % page if page > 1 else "")
        doc = fetch_cached(url, cache_dir, refresh)
        found = set(url_path(h) for h in re.findall(
            r'href="([^"]+)" class="product-card__title-link', doc))
        if not found or found <= members:
            break
        members |= found
        m = re.search(r"(\d+)\s*-\s*(\d+)\s*/\s*(\d+)\s*termék", doc)
        if m and int(m.group(2)) >= int(m.group(3)):
            break
    return members


def cmd_products(a):
    urls = list(a.urls)
    if a.url_file:
        with open(a.url_file, encoding="utf-8") as fh:
            urls += [l.strip() for l in fh if l.strip() and not l.startswith("#")]
    sitemap_urls = []
    if a.sitemap:
        sitemap_urls = [u for u, pr in read_sitemap(a.sitemap) if pr == "0.6"]
        if a.all_from_sitemap:
            urls += sitemap_urls
    urls = list(dict.fromkeys(urls))
    if not urls:
        sys.exit("no product URLs given")
    ids = {}
    if a.ids_out and os.path.exists(a.ids_out):
        with open(a.ids_out, encoding="utf-8") as fh:
            ids = json.load(fh)
    members = {}
    crawl = list(a.featured_category)
    if a.crawl_categories:
        crawl += list(MAIN) + list(SUB) + list(FEATURED)
    for path in dict.fromkeys(crawl):
        members[path] = crawl_category(path, os.path.join(a.cache_dir, "categories"), a.refresh)
    if a.category_hints:
        with open(a.category_hints, encoding="utf-8") as fh:
            for u, cats in json.load(fh).items():
                for c in ([cats] if isinstance(cats, str) else cats):
                    members.setdefault(url_path(c), set()).add(url_path(u))
    products, report = [], {"failed": [], "warnings": {}}
    for i, u in enumerate(urls, 1):
        try:
            doc = fetch_cached(u, a.cache_dir, a.refresh)
            p = parse_product(doc, u)
        except Exception as e:  # keep going, report at the end
            report["failed"].append({"url": u, "error": str(e)})
            sys.stderr.write("FAILED %s: %s\n" % (u, e))
            continue
        if p["product_id"]:
            ids[u] = p["product_id"]
        products.append(p)
        sys.stderr.write("[%d/%d] %s\n" % (i, len(urls), p["title"]))
    hmap = build_handle_map(list(dict.fromkeys(sitemap_urls + urls)), ids)
    status_file = os.path.join(a.cache_dir, "image_status.json")
    img_status = {}
    if os.path.exists(status_file):
        with open(status_file, encoding="utf-8") as fh:
            img_status = json.load(fh)
    rows = []
    for p in products:
        handle = hmap[p["url"]]
        p["handle"] = handle
        ptype, tags = categorize(p, members)
        if a.verify_images:
            for im in p["images"]:
                code = 200 if im["src"] == im["cache"] else img_status.get(im["src"])
                if code != 200:
                    code = curl(im["src"], head=True)
                    if code == 0:  # curl/network error: retry once
                        code = curl(im["src"], head=True)
                    img_status[im["src"]] = code
                if code != 200:
                    p["warnings"].append("original image HTTP %s, using cache URL: %s" % (code, im["src"]))
                    im["src"] = im["cache"]
        imgs = p["images"] or [{"src": "", "alt": ""}]
        seo_title = (p["seo_title"] or p["title"])[:70]
        seo_desc = p["seo_desc"]
        if len(seo_desc) > 320:
            seo_desc = seo_desc[:317].rsplit(" ", 1)[0] + "..."
        for n, im in enumerate(imgs, 1):
            row = dict.fromkeys(CSV_COLUMNS, "")
            row.update({"Handle": handle, "Image Src": im["src"],
                        "Image Position": str(n) if im["src"] else "",
                        "Image Alt Text": im["alt"] if im["src"] else ""})
            if n == 1:
                row.update({
                    "Title": p["title"], "Body (HTML)": build_body(p),
                    "Vendor": p["manufacturer"] or "Modulshop", "Product Category": "",
                    "Type": ptype, "Tags": ", ".join(tags), "Published": "TRUE",
                    "Option1 Name": "Title", "Option1 Value": "Default Title",
                    "Variant SKU": p["sku"], "Variant Grams": "",
                    "Variant Inventory Tracker": "shopify", "Variant Inventory Qty": str(p["qty"]),
                    "Variant Inventory Policy": "deny", "Variant Fulfillment Service": "manual",
                    "Variant Price": p["price"], "Variant Compare At Price": p["compare_at"],
                    "Variant Requires Shipping": "TRUE", "Variant Taxable": "TRUE",
                    "Variant Barcode": p["gtin"], "SEO Title": seo_title,
                    "SEO Description": seo_desc, "Status": "active"})
            rows.append(row)
        if p["warnings"]:
            report["warnings"][p["url"]] = p["warnings"]
    if a.verify_images:
        with open(status_file, "w", encoding="utf-8") as fh:
            json.dump(img_status, fh, indent=1, sort_keys=True)
    with open(a.out, "w", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=CSV_COLUMNS, lineterminator="\n")
        w.writeheader()
        w.writerows(rows)
    if a.ids_out:
        with open(a.ids_out, "w", encoding="utf-8") as fh:
            json.dump(ids, fh, ensure_ascii=False, indent=1, sort_keys=True)
    if a.report:
        report["products"] = [{k: p[k] for k in ("url", "handle", "title", "sku", "product_id",
                                                 "price", "qty", "stock_text", "gtin", "manufacturer")}
                              | {"images": len(p["images"])} for p in products]
        with open(a.report, "w", encoding="utf-8") as fh:
            json.dump(report, fh, ensure_ascii=False, indent=1)
    sys.stderr.write("wrote %d rows for %d products to %s; failed: %d\n"
                     % (len(rows), len(products), a.out, len(report["failed"])))


# ---------------------------------------------------------------------------
# Redirects
# ---------------------------------------------------------------------------
def collection_handle(path):
    for table in (MAIN, FEATURED, SUB):
        if path in table:
            return table[path][1]
    return None


def cmd_redirects(a):
    entries = read_sitemap(a.sitemap)
    ids = {}
    if a.ids and os.path.exists(a.ids):
        with open(a.ids, encoding="utf-8") as fh:
            ids = json.load(fh)
    product_urls = [u for u, pr in entries if pr == "0.6"]
    hmap = build_handle_map(product_urls, ids)
    rows, unmapped = [], []
    for u, pr in entries:
        path = url_path(u)
        if path in ("/", ""):
            continue  # home page needs no redirect
        if pr == "0.6":
            target = "/products/" + hmap[u]
        elif collection_handle(path):
            target = "/collections/" + collection_handle(path)
        elif path in OTHER_CAT:
            target = OTHER_CAT[path]
        elif path in INFO:
            target = INFO[path]
        else:
            unmapped.append(u)
            target = "/pages/" + base_handle(u)
        rows.append((path, target))
    with open(a.out, "w", encoding="utf-8", newline="") as fh:
        w = csv.writer(fh, lineterminator="\n")
        w.writerow(["Redirect from", "Redirect to"])
        w.writerows(rows)
    sys.stderr.write("wrote %d redirects to %s\n" % (len(rows), a.out))
    if unmapped:
        sys.stderr.write("UNMAPPED (guessed /pages/<slug>), check manually:\n  %s\n" % "\n  ".join(unmapped))


def cmd_clean(a):
    with open(a.file, encoding="utf-8", errors="replace") as fh:
        doc = fh.read()
    if a.selector:
        doc = extract_element(doc, a.selector) or ""
    print(clean_html(doc))


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("products", help="product pages -> Shopify CSV")
    p.add_argument("urls", nargs="*")
    p.add_argument("--url-file")
    p.add_argument("--sitemap", help="sitemap.xml path or URL (used for handle collision checks)")
    p.add_argument("--all-from-sitemap", action="store_true",
                   help="convert ALL 0.6-priority sitemap URLs (full catalog, ~1856 requests)")
    p.add_argument("--cache-dir", required=True, help="where raw HTML is stored/reused")
    p.add_argument("--refresh", action="store_true", help="re-download cached pages")
    p.add_argument("--featured-category", action="append", default=[],
                   help="category path (e.g. /sajat-termekeink-244) whose members get its tag; repeatable")
    p.add_argument("--crawl-categories", action="store_true",
                   help="crawl ALL category lists (~150 requests) so every product gets all its "
                        "subcategory tags and a type even if its breadcrumb is only 'Összes termék'")
    p.add_argument("--category-hints",
                   help="JSON {product_url: category_url or [category_urls]} used like crawled membership")
    p.add_argument("--verify-images", action="store_true",
                   help="HEAD-check original image URLs, fall back to cache URL")
    p.add_argument("--out", required=True)
    p.add_argument("--ids-out", help="JSON url->ShopRenter product id (merged; reuse for redirects)")
    p.add_argument("--report", help="JSON report of warnings/failures")
    p.set_defaults(func=cmd_products)
    r = sub.add_parser("redirects", help="sitemap -> Shopify redirect CSV")
    r.add_argument("--sitemap", required=True)
    r.add_argument("--ids", help="product id JSON written by 'products --ids-out'")
    r.add_argument("--out", required=True)
    r.set_defaults(func=cmd_redirects)
    c = sub.add_parser("clean", help="clean a ShopRenter HTML file/fragment")
    c.add_argument("file")
    c.add_argument("--selector", help="regex matching the opening tag of the element to extract")
    c.set_defaults(func=cmd_clean)
    a = ap.parse_args(argv)
    a.func(a)


if __name__ == "__main__":
    main()
