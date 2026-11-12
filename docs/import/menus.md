# Menük (Shopify Navigáció)

- **Hol hozod létre:** Shopify admin → *Online áruház → Navigáció* (újabb adminban: *Tartalom → Menük*).
- **Menüpont hozzáadása:** a „Link” mezőben válaszd ki a kollekciót vagy oldalt, vagy írd be az útvonalat.
- **Előfeltétel:** a kollekciók és oldalak handle-je egyezzen a `collections.md` és a `pages.md` szerintivel. Ezért a menüket a kollekciók és oldalak **után** hozd létre.
- **Szintek:** a Shopify 3 menüszintet kezel. A mega-menü megjelenése a témán múlik. A témabeállításban a fő menünél kapcsold be a „mega menu” módot, ha a téma tud ilyet.

## 1. Főmenü (`main-menu`) – mega-menü

1. szint: menüpontok. 2. szint: főkollekciók. 3. szint: alkollekciók.

```
Termékek  →  /collections/all
├── Mikrovezérlők, alaplapok      →  /collections/mikrovezerlok-alaplapok
│   ├── Arduino                    →  /collections/arduino
│   ├── ESP8266                    →  /collections/esp8266
│   ├── ESP32                      →  /collections/esp32
│   ├── STM                        →  /collections/stm
│   └── Raspberry                  →  /collections/raspberry
├── Szenzor Modulok               →  /collections/szenzor-modulok
│   ├── Hőmérséklet, pára, nyomás  →  /collections/homerseklet-para-nyomas
│   ├── Feszültség, áram, távolság →  /collections/feszultseg-aram-tavolsag
│   └── Fény, mozgás, giro, gyorsulás, RFID  →  /collections/feny-mozgas-giro-gyorsulas-rfid
├── Egyéb Modulok                 →  /collections/egyeb-modulok
│   ├── Beviteli eszközök          →  /collections/beviteli-eszkozok
│   ├── Kommunikációs modulok      →  /collections/kommunikacios-modulok
│   ├── Motor, DC, léptető, szervó →  /collections/motor-dc-lepteto-szervo
│   ├── Motorvezérlők              →  /collections/motorvezerlok
│   ├── Próbapanelek, shieldek, egyéb  →  /collections/probapanelek-shieldek
│   └── Relék, optocsatolók        →  /collections/relek-optocsatolok
├── Erősítők, Végfokok            →  /collections/erositok-vegfokok
│   ├── 100W fölötti + 2.1         →  /collections/100w-folotti-erositok
│   ├── 2×50W erősítő, végfok      →  /collections/2x50w-erositok-vegfokok
│   ├── Audió kiegészítők          →  /collections/audio-kiegeszitok
│   └── Hangszóró                  →  /collections/hangszorok
├── LCD-k, Kijelzők               →  /collections/lcd-k-kijelzok
├── BMS-ek, 18650 Akkuk           →  /collections/bms-ek-18650-akkuk
│   ├── 1S - 5S BMS                →  /collections/1s-5s-bms
│   ├── Akku cellák, elemek        →  /collections/akku-cellak-elemek
│   ├── 6S - 13S BMS               →  /collections/6s-13s-bms
│   ├── Akku töltők                →  /collections/akku-toltok
│   └── BMS kiegészítők            →  /collections/bms-kiegeszitok
├── DC, AC konverterek            →  /collections/dc-ac-konverterek
│   ├── AC-DC tápegységek, labortáp  →  /collections/ac-dc-tapegysegek-labortap
│   ├── DC-DC step down (feszültségcsökkentő)  →  /collections/dc-dc-step-down
│   └── DC-DC step up (feszültségnövelő)       →  /collections/dc-dc-step-up
├── Műszerek                      →  /collections/muszerek
│   └── Műszerdobozok              →  /collections/muszerdobozok
├── Egyéb                         →  /collections/egyeb
│   └── Szerszámok                 →  /collections/szerszamok
├── Elektronika                   →  /collections/elektronika
│   ├── Ellenállások, potméterek   →  /collections/ellenallasok-potmeterek
│   ├── Fizika óra, áramköri elemek  →  /collections/fizika-ora-aramkori-elemek
│   ├── Hűtőbordák, ventilátorok   →  /collections/hutobordak-ventilatorok
│   ├── IC                         →  /collections/ic
│   ├── Kapcsolók, csatlakozók, vezetékek  →  /collections/kapcsolok-csatlakozok-vezetekek
│   ├── Kondenzátorok, diódák      →  /collections/kondenzatorok-diodak
│   ├── Ledek                      →  /collections/ledek
│   ├── PCB nyáklapok, forrasztási anyagok  →  /collections/pcb-nyaklapok-forrasztasi-anyagok
│   └── Tranzisztor, MOSFET        →  /collections/tranzisztor-mosfet
├── D.I.Y. Készletek              →  /collections/diy-keszletek
│   ├── Csavarok, betétek          →  /collections/csavarok-betetek
│   └── Távtartók                  →  /collections/tavtartok
└── Led világítás                 →  /collections/led-vilagitas
Saját termékeink              →  /collections/sajat-termekeink
Csomagok                      →  /collections/csomagok
Iskoláknak és cégeknek        →  /pages/iskolaknak-es-cegeknek
Blog                          →  /blogs/news
Kapcsolat                     →  /pages/kapcsolat
```

**A menünevekről:**
- A menüben szereplő név lehet barátságosabb, mint a címke. A menüben szerepelhet vessző („Hőmérséklet, pára, nyomás”), a címkében nem. A link a kollekcióra mutat, ezért a menünév szabadon átírható.
- Az alkollekciók sorrendje a régi menüt követi.
- Külön „Összes termék” menüpont helyett a „Termékek” felső menüpont maga mutat a `/collections/all` oldalra.

## 2. Lábléc-menük

A témában jellemzően három „Menü” blokkot kell a láblécbe tenni, mindegyikhez a lenti menük egyikét választva.

### `vasarlas` – „Vásárlás”

| Menüpont | Link |
|---|---|
| Szállítás és fizetés | `/pages/szallitas-es-fizetes` |
| Garancia és visszaküldés | `/pages/garancia-es-visszakuldes` |
| Hűségpont rendszer | `/pages/husegpont` |
| Iskoláknak és cégeknek | `/pages/iskolaknak-es-cegeknek` |
| Regisztráció / Fiókom | `/account` |
| Összes termék | `/collections/all` |

### `informaciok` – „Információk”

| Menüpont | Link |
|---|---|
| Rólunk | `/pages/rolunk` |
| Saját termékeink | `/pages/sajat-termekeink` |
| Gyakran ismételt kérdések | `/pages/gyik` |
| Blog | `/blogs/news` |
| Kapcsolat | `/pages/kapcsolat` |

### `jogi` – „Jogi információk”

| Menüpont | Link |
|---|---|
| ÁSZF | `/pages/aszf` |
| Adatvédelmi nyilatkozat | `/pages/adatvedelem` |
| Elállás | `/pages/elallas` |
| Impresszum | `/pages/impresszum` |
| AI használati szabályzat | `/pages/ai-hasznalati-szabalyzat` |
| Visszatérítési szabályzat (Shopify) | `/policies/refund-policy` *(csak ha kitöltöd: Beállítások → Szabályzatok)* |

**Megjegyzések:**
- A régi láblécből kimaradt a Kapcsolat, a Rólunk és a Blog. Most mindhárom szerepel.
- A régi „ÁSZF” link a `/adatvedelem-45` oldalra mutatott. Az új menüben az ÁSZF és az Adatvédelem külön, helyes handle-lel szerepel.
- A „Rólunk” és az „Iskoláknak és cégeknek” oldal tervezet. Amíg nincs jóváhagyva, maradjon rejtett (nem közzétett), és a menüpontja se kerüljön ki.
- A „Hűségpont rendszer” menüpont is csak akkor kerüljön ki, ha a hűségpont-alkalmazás már működik.
