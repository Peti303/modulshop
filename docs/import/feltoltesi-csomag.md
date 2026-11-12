# Modulshop.hu – feltöltési csomag a Shopify AI asszisztensnek

Ez a dokumentum a modulshop.hu (ShopRenterről Shopifyra költöző elektronikai alkatrész-webáruház) új Shopify-áruházának kezdő tartalmát írja le: 8 terméket, a hozzájuk és a téma főoldalához szükséges kollekciókat, az oldalakat és a menüket. Minden adat a tulajdonos engedélyével, a jelenlegi nyilvános oldalakból készült migrációs csomagból (`docs/import/`) származik; semmit ne egészíts ki és ne találj ki.

## 1. Útmutató a Shopify AI-nak

- Az áruház nyelve **magyar**, pénzneme **magyar forint (HUF)**. Minden szöveget pontosan úgy vegyél fel, ahogy itt áll; ne fordítsd, ne fogalmazd át, ne egészítsd ki.
- Ebben a sorrendben dolgozz: **1) kollekciók → 2) termékek (kollekciókhoz rendelve) → 3) oldalak → 4) menük.** A menüket csak a kollekciók és oldalak után hozd létre, hogy a linkek kiválaszthatók legyenek.
- A **handle-öket pontosan** a megadott formában használd (kollekció, termék, oldal). A téma és a menük ezekre a handle-ökre linkelnek; ha egy handle eltér, a link nem fog működni.
- A kollekciók **automatikus** kollekciók: „A termékeknek bármelyik feltételnek meg kell felelniük”. A főkollekció feltétele „Terméktípus egyenlő …”, az alkollekcióé „Termékcímke egyenlő …” (a 3. pont táblázata szerint). A termék típusát és címkéit ezért karakterre pontosan add meg.
- Termékek: Forgalmazó (vendor) = **Modulshop**; állapot = **Aktív**; **készletkövetés bekapcsolva** (Shopify követi a készletet), a megadott darabszám az alapértelmezett helyszínre kerül; elfogyás után ne lehessen rendelni (készlethiány esetén ne folytassa az értékesítést); fizikai termék, szállítást igényel; adóköteles.
- Az árak **bruttó árak, az áfát (27%) tartalmazzák**. Ellenőrizd, hogy a *Beállítások → Adók és vámok* alatt be legyen kapcsolva, hogy az árak tartalmazzák az adót, különben a Shopify még egyszer rászámolja az áfát.
- A termékképeket a megadott **URL-ekről importáld**, a felsorolt sorrendben (az 1. a főkép). Minden URL-t ellenőriztünk: HTTP 200-at ad.
- A leírásokat a „Leírás” alatti szöveg alapján, a formázás (címsorok, listák, félkövér) megtartásával vedd fel.
- Oldalak: a címet, a handle-t (URL-handle) és a téma sablonját (pl. `page.legal`) a 4. pont adja meg. Ha egy sablon még nincs meg a témában, az oldal kapja az alapértelmezett sablont, és jelezd a tulajdonosnak. A **TERVEZET** jelölésű oldalakat (és a Hűségpont oldalt) **rejtettként** (nem közzétéve) hozd létre.
- A `[[…]]` jelölésű részeket **szó szerint hagyd benne**; ezeket a tulajdonos tölti ki közzététel előtt.

## 2. Termékek (8 db)

Forrás: `docs/import/products.csv`. Készlet: a régi terméklap „N db raktáron” értéke 2026-11-12-én.

### ESP32-C3 Szuper mini, WiFi, BT 5.0, usb-C

| Mező | Érték |
|---|---|
| Handle | `esp32-c3-szuper-mini-wifi-bt-50-usb-c` |
| Cikkszám (SKU) | 1-2-29 |
| Ár (Ft, bruttó) | 1900 |
| Készlet (db) | 37 |
| Terméktípus | Mikrovezérlők, alaplapok |
| Kollekció(k) | Mikrovezérlők, alaplapok (`mikrovezerlok-alaplapok`); ESP32 (`esp32`) |
| Címkék | ESP32 |
| Vonalkód (GTIN) | 5999572386689 |
| SEO-cím | ESP32-C3 Szuper mini, WiFi, BT 5.0, usb-C |
| SEO-leírás | Az ESP32-C3 egy szuper mini, WiFi és Bluetooth 5.0 modullal rendelkező mikrovezérlő. 160 MHz-es 1 magos CPU. 16 digitális pin ebből 4 analóg, I2C,SPI UART,ADC |

**Leírás**

IC: EPS32-C3  
Frekvencia : 160 Mhz  
Csatlakozó : usb-C  
Memória: 384 KBrom ,400 KBsram, 4MB Flash

Az ESP32-C3 egy szuper mini, WiFi és Bluetooth 5.0 modullal rendelkező mikrovezérlő, melyet kifejezetten IoT alkalmazásokhoz terveztek. ESP32C3FN4 cpu-alapú, 160 MHz-es órajelet használó, 1 magos chipet tartalmaz. Az ESP32-C3 digitális és analóg pinjeivel, valamint I2C, SPI, UART és ADC interfészeivel széleskörű lehetőségeket nyújt a fejlesztőknek. Az ESP32C3 biztonsági funkciói közé tartozik a hardveres AES titkosítás, ami biztosítja az adatok biztonságát a továbbítás és tárolás során. Továbbá, az eszköz támogatja a szoftveres frissítéseket a levegőn keresztül (OTA), ami lehetővé teszi a firmware kényelmes és biztonságos frissítését anélkül, hogy fizikailag hozzáférnénk az eszközhöz. Az Espessif által gyártott ESP32-C3 ideális választás olyan projektekhez, ahol a kis méret és a magas teljesítmény fontos szempont. A termék USB-C csatlakozóval is rendelkezik, így könnyen csatlakoztatható számos eszközhöz és rendszerhez. Összefoglalva, az ESP32C3FN4 egy rendkívül hatékony és sokoldalú mikrovezérlő, amely kiválóan alkalmas modern IoT alkalmazások és okos otthoni megoldások fejlesztésére. Számos kommunikációs interfészének és erős biztonsági funkcióinak köszönhetően ideális választás bármilyen projekt számára, ahol a megbízhatóság és az adatvédelem kulcsfontosságú.

**Képek**

1. https://modulshop.cdn.shoprenter.hu/custom/modulshop/image/data/product/01%20Mikrovez%C3%A9rl%C5%91k/02%20ESP/1-2-29_ESP32C3SM-1.webp (alt: ESP32C3 Szupermini)
2. https://modulshop.cdn.shoprenter.hu/custom/modulshop/image/data/product/01%20Mikrovez%C3%A9rl%C5%91k/02%20ESP/1-2-29_ESP32C3SM-2.webp (alt: ESP32C3 Szupermini)
3. https://modulshop.cdn.shoprenter.hu/custom/modulshop/image/data/product/01%20Mikrovez%C3%A9rl%C5%91k/02%20ESP/1-2-29_ESP32C3SM-3.webp (alt: ESP32C3 Szupermini)
4. https://modulshop.cdn.shoprenter.hu/custom/modulshop/image/data/product/01%20Mikrovez%C3%A9rl%C5%91k/02%20ESP/1-2-29_ESP32C3SM-4.webp (alt: ESP32C3 Szupermini)
5. https://modulshop.cdn.shoprenter.hu/custom/modulshop/image/data/product/01%20Mikrovez%C3%A9rl%C5%91k/02%20ESP/1-2-29_ESP32C3SM-5.webp (alt: ESP32C3 Szupermini)
6. https://modulshop.cdn.shoprenter.hu/custom/modulshop/image/data/product/01%20Mikrovez%C3%A9rl%C5%91k/02%20ESP/1-2-29_ESP32C3SM-6.webp (alt: ESP32C3 Szupermini)

### Uno R3 - ATmega328P - Arduino kompatibilis usb C

| Mező | Érték |
|---|---|
| Handle | `uno-r3-atmega328p-arduino-kompatibilis-usb-c` |
| Cikkszám (SKU) | 1-1-27 |
| Ár (Ft, bruttó) | 2500 |
| Készlet (db) | 14 |
| Terméktípus | Mikrovezérlők, alaplapok |
| Kollekció(k) | Mikrovezérlők, alaplapok (`mikrovezerlok-alaplapok`); Arduino (`arduino`) |
| Címkék | Arduino |
| Vonalkód (GTIN) | 5999572384180 |
| SEO-cím | Uno R3 - ATmega328P - Arduino kompatibilis usb C |
| SEO-leírás | Uno R3 - ATmega328P - 100% Arduino kompatibilis usb-c Az Arduino mikrovezérlők legnépszerűbb tagja, az UNO R3-as. A könnyű kezelhetőség, a használtra kész kivitel, a rengeteg hozzá fejlesztett hardver eszköz, és ingyenesen elérhető szoftver, tette a kezdők és a haladók legkedveltebb fejlesztőpaneljává. Az arduino... |

**Leírás**

CPU: ATmega328P  
Csatlakozó : usb-C  
Usb illesztő : ch340

- **Tápfeszültség:** 5-12 V (max. 20V)

**Uno R3 - ATmega328P - 100% Arduino kompatibilis**

Az Arduino mikrovezérlők legnépszerűbb tagja, az UNO R3-as. A könnyű kezelhetőség, a használtra kész  
kivitel, a rengeteg hozzá fejlesztett hardver eszköz, és ingyenesen elérhető szoftver, tette a kezdők és a haladók legkedveltebb fejlesztőpaneljává. Az arduino hivatalos honlapján, ( www.arduino.cc ) mindenki számára elérhető  
az arduino ide szoftver aminek segítségével könnyedén írhatunk programokat, tesztelhetjük azokat, és a feltölthetjük a kártyára.

További információkat találsz a wikipédián : https://hu.wikipedia.org/wiki/Arduino

Paraméterek :

- ATmega328 központi egység,
- 100% Arduino UNO R3 kompatibilis
- Külső tápfeszültség: 5-12 V (max. 20V),
- 14 digitális ki/bemenet (ebből 6 PWM),
- 6 analóg bemenet,
- 32 kbyte Flash memória,
- 2 kbyte SRAM és 1 kbyte EEPROM,
- 16 Mhz órajel,
- CH340 illesztőchip.
- USB-C csatlakozó

**Képek**

1. https://modulshop.cdn.shoprenter.hu/custom/modulshop/image/data/product/01%20Mikrovez%C3%A9rl%C5%91k/01%20Arduino/1-1-27_uno_usbc-3.jpg (alt: Uno R3 usb-c)
2. https://modulshop.cdn.shoprenter.hu/custom/modulshop/image/data/product/01%20Mikrovez%C3%A9rl%C5%91k/01%20Arduino/1-1-27_uno_usbc-2.jpg (alt: Uno R3 usb-c)
3. https://modulshop.cdn.shoprenter.hu/custom/modulshop/image/data/product/01%20Mikrovez%C3%A9rl%C5%91k/01%20Arduino/1-1-27_uno_usbc-4.jpg (alt: Uno R3)

### DHT11 Hőmérséklet és páratartalom érzékelő modul

| Mező | Érték |
|---|---|
| Handle | `dht11-homerseklet-es-paratartalom-erzekelo-modul` |
| Cikkszám (SKU) | 2-1-1 |
| Ár (Ft, bruttó) | 650 |
| Készlet (db) | 31 |
| Terméktípus | Szenzor Modulok |
| Kollekció(k) | Szenzor Modulok (`szenzor-modulok`); Hőmérséklet / pára / nyomás (`homerseklet-para-nyomas`) |
| Címkék | Hőmérséklet / pára / nyomás |
| Vonalkód (GTIN) | 5999572380489 |
| SEO-cím | DHT11 Hőmérséklet és páratartalom érzékelő modul |
| SEO-leírás | DHT11 Hőmérséklet és páratartalom érzékelő modul A DHT11 egy egyszerű és alacsony költségű digitális hőmérséklet és páratartalom-érzékelő modul. Egy kapacitív páratartalom-érzékelő termisztor segítségével méri a környező levegőt, és digitális jelet ad ki a kimeneten. Kifejezetten egyszerű a használata, de... |

**Leírás**

**DHT11 Hőmérséklet és páratartalom érzékelő modul**

A DHT11 egy egyszerű és alacsony költségű digitális hőmérséklet és páratartalom-érzékelő modul. Egy kapacitív páratartalom-érzékelő termisztor segítségével méri a környező levegőt, és digitális jelet ad ki a kimeneten. Kifejezetten egyszerű a használata, de körültekintést igényel az időzítés, hogy a megfelelő adatokat kapjuk.

- Feszültség: 3.5V - 5.5V DC
- 20%-90% páratartalom mérés +-5% pontosság
- 0-50 fok közötti hőmérséklet mérés +-2 % pontosság
- 5 másodperces mérési idő

1-wire kommunikáció

**Képek**

1. https://modulshop.cdn.shoprenter.hu/custom/modulshop/image/data/product/02%20Szenzor%20mofulok/2-1-1%20DHT11-1.jpg (alt: DHT11 Hőmérséklet és páratartalom érzékelő modul)
2. https://modulshop.cdn.shoprenter.hu/custom/modulshop/image/data/product/02%20Szenzor%20mofulok/2-1-1%20DHT11-2.jpg (alt: DHT11 Hőmérséklet és páratartalom érzékelő modul)
3. https://modulshop.cdn.shoprenter.hu/custom/modulshop/image/data/product/02%20Szenzor%20mofulok/2-1-1%20DHT11-3.jpg (alt: DHT11 Hőmérséklet és páratartalom érzékelő modul)
4. https://modulshop.cdn.shoprenter.hu/custom/modulshop/image/data/product/02%20Szenzor%20mofulok/2-1-1%20DHT11-4.jpg (alt: DHT11 Hőmérséklet és páratartalom érzékelő modul)

### 0,96" Oled kijelző/Fehér, 128*64, I2C

| Mező | Érték |
|---|---|
| Handle | `096-oled-kijelzokek-12864-i2c-986` |
| Cikkszám (SKU) | 4-1-21 |
| Ár (Ft, bruttó) | 1250 |
| Készlet (db) | 13 |
| Terméktípus | LCD-k, Kijelzők |
| Kollekció(k) | LCD-k, Kijelzők (`lcd-k-kijelzok`) |
| Vonalkód (GTIN) | 5999572382964 |
| SEO-cím | 0,96 Oled kijelző/Fehér, 128*64, I2C |
| SEO-leírás | 0,96″ fehér OLED kijelző 128 × 64 pixel felbontással, SSD1306 vezérlővel, I2C interfésszel, 160° feletti betekintési szöggel és 3–5 V táppal. |

**Leírás**

- Nagy felbontás: 128 * 64
- Feszültség: 3V - 5V DC
- Illesztőprogram IC: SSD1306

#### 0,96″ fehér OLED kijelző – 128 × 64 pixel, SSD1306, I2C

A **0,96″-os OLED kijelzőmodul** kompakt, nagy kontrasztú megjelenítő **128 × 64 pixeles felbontással**. A fehér OLED képpontok szövegek, számértékek, szimbólumok és egyszerű grafikák megjelenítésére egyaránt alkalmasak.

A modul **SSD1306 vezérlő IC-re** épül, és **I2C (IIC) interfészen** kommunikál. A csatlakoztatáshoz mindössze négy érintkező – **GND, VCC, SCL és SDA** – szükséges, az adatkommunikáció pedig csak két I/O vonalat használ.

A kijelző **3–5 V DC** tápfeszültségről működtethető, és számos mikrokontrolleres rendszerrel használható, többek között Arduino, 51-es sorozatú, MSP430 és STM32 vezérlőkkel. A **160°-nál nagyobb betekintési szög** széles tartományból biztosít jó leolvashatóságot.

Az OLED technológia külön háttérvilágítás nélkül működik, mivel minden képpont saját fényt bocsát ki. A teljes képernyő energiafogyasztása körülbelül **0,08 W**.

#### Milyen csatlakozások szükségesek?

A modul **4 érintkezővel** rendelkezik: GND, VCC, SCL és SDA. Az I2C kommunikációhoz az SCL órajel- és az SDA adatvonalat használja.

#### Milyen vezérlőkkel használható?

Az SSD1306 széles körben támogatott vezérlő, így a modul többek között **Arduino, MSP430, STM32 és 51-es sorozatú mikrokontrollerekkel** is használható.

#### Fontosabb paraméterek

- **Terméktípus:** OLED kijelzőmodul
- **Kijelzőméret:** 0,96″
- **Felbontás:** 128 × 64 pixel
- **Kijelzés színe:** fehér
- **Meghajtó IC:** SSD1306
- **Interfész:** I2C / IIC
- **Tápfeszültség:** 3–5 V DC
- **Csatlakozók:** GND, VCC, SCL, SDA
- **Érintkezők száma:** 4
- **Szükséges I/O vonalak:** 2
- **Betekintési szög:** >160°
- **Teljes képernyős fogyasztás:** kb. 0,08 W
- **Kontraszt:** állítható
- **Meghajtási mód:** 1/64 Duty
- **Működési hőmérséklet:** −30–70 °C
- **Panel mérete:** kb. 26,70 × 19,26 × 1,85 mm
- **Aktív kijelzőterület:** kb. 21,74 × 11,2 mm
- **Kompatibilitás:** Arduino, 51-es sorozat, MSP430, STM32 és egyéb mikrokontrollerek

**Képek**

1. https://modulshop.cdn.shoprenter.hu/custom/modulshop/image/data/product/04%20LCD-TFT-Kijelz%C5%91k/4-1-11%200%2C96%20Oled%20128x64-1.jpg (alt: 0,96" Oled kijelző/kék, 128*64, I2C)
2. https://modulshop.cdn.shoprenter.hu/custom/modulshop/image/data/product/04%20LCD-TFT-Kijelz%C5%91k/4-1-11%200%2C96%20Oled%20128x64-2.jpg (alt: 0,96" Oled kijelző/kék, 128*64, I2C)
3. https://modulshop.cdn.shoprenter.hu/custom/modulshop/image/data/product/04%20LCD-TFT-Kijelz%C5%91k/4-1-21_oled096_white-1.jpg (alt: 0,96" Oled kijelző/Fehér, 128*64, I2C)
4. https://modulshop.cdn.shoprenter.hu/custom/modulshop/image/data/product/04%20LCD-TFT-Kijelz%C5%91k/4-1-21_oled096_white-2.jpg (alt: 0,96" Oled kijelző/Fehér, 128*64, I2C)
5. https://modulshop.cdn.shoprenter.hu/custom/modulshop/image/data/product/04%20LCD-TFT-Kijelz%C5%91k/4-1-21_oled096_white-3.jpg (alt: 0,96" Oled kijelző/Fehér, 128*64, I2C)

*Megjegyzés a forrásból: a CSV ennél a fehér OLED-nél az első két képként a kék változat (4-1-11) képeit adja, „kék” alt-szöveggel. A tulajdonos döntse el, hogy ezek maradjanak-e.*

### XH-M577 sztereó erősítőmodul 2*80W 24 V, hangszínszabályzással

| Mező | Érték |
|---|---|
| Handle | `xh-m577-sztereo-erositomodul-280w-24-v-hangszinszabalyzassal` |
| Cikkszám (SKU) | 5-1-46 |
| Ár (Ft, bruttó) | 2600 |
| Készlet (db) | 15 |
| Terméktípus | Erősítők, Végfokok |
| Kollekció(k) | Erősítők, Végfokok (`erositok-vegfokok`); 2*50W erősítő / végfok (`2x50w-erositok-vegfokok`) |
| Címkék | 2*50W erősítő / végfok |
| SEO-cím | XH-M577 sztereó erősítőmodul 2*80W 24 V, hangszínszabályzással |
| SEO-leírás | XH-M577 TPA3116D2 sztereó erősítőmodul 12–24 V táppal, hangerő-, mély- és magas szabályzással. DIY hangfalhoz és audió projektekhez. |

**Leírás**

**Erősítő IC: TPA3116D2**  
**Tápfeszültség: 12–24 V DC**  
**Ajánlott tápáram: 5 A**  
**Csatornák száma: 2 csatorna / sztereó**  
**Marketing szerinti kimeneti teljesítmény: 2×80 W**  
**TPA3116D2 hivatalos referencia:**  
**2×50 W / 4 Ω / 21 V**, illetve **2×30 W / 8 Ω / 24 V**  
**Kimeneti impedancia: 4–8 Ω**  
**Erősítőosztály: Class-D**  
**Kezelőszervek: hangerő, mély, magas**

#### XH-M577 TPA3116D2 sztereó digitális erősítőmodul – 12–24 V, hangszínszabályzással, 2×80 W névleges teljesítménnyel

Az **XH-M577** egy **sztereó, Class-D audió erősítőmodul**, amely a **TPA3116D2** erősítő IC-re épül, és a forgalmazói adatok szerint **12–24 V DC** tápról működik, **4–8 ohmos hangsugárzókat** kezel, valamint **hangerő-, mély- és magas hangszínszabályzással** rendelkezik. A legtöbb kereskedelmi listázás **2×80 W** névleges kimeneti teljesítménnyel hirdeti, a panel méretét pedig jellemzően **96 × 33 mm** körül adják meg.

A modul egyik legnagyobb előnye, hogy kompakt méretben kínál **sztereó erősítést és analóg hangszínszabályzást**, ezért jól használható DIY hangfalhoz, műhelyhangrendszerhez, asztali erősítőhöz vagy kisebb otthoni audió projektekhez. A kereskedelmi leírások alapján az előlapi kezelőszervek a **master hangerő**, a **mély** és a **magas** hang külön állítását teszik lehetővé, így a hangzás könnyen az adott hangsugárzóhoz vagy helyiséghez igazítható.

Fontos, hogy a **2×80 W** megadás inkább a termékmarketingben használt névleges érték. A **TPA3116D2** hivatalos Texas Instruments adatlapja szerint a chip **2×50 W-ot tud 4 ohmos terhelésen 21 V-on**, kis hűtéssel, illetve **2×30 W-ot 8 ohmos terhelésen 24 V-on**. Ezért a valós, tartósan elérhető teljesítmény mindig függ a **tápfeszültségtől**, a **hangszóró impedanciájától**, a **hűtéstől** és a megengedett torzítástól. Webshopos szempontból ezért korrekt úgy fogalmazni, hogy a modul **2×80 W-osként ismert**, de a tényleges teljesítmény a rendszer kialakításától függ.

Az XH-M577 különösen jó választás lehet azoknak, akik egy egyszerűen beépíthető, mégis jól használható sztereó erősítőt keresnek. A kereskedelmi adatok szerint a modul **5 A körüli tápáramot** igényel, **1 kΩ bemeneti impedanciával** rendelkezik, a hangszínszabályzó előfok pedig az input jel finomhangolását is lehetővé teszi. Emiatt jól illeszthető például Bluetooth vevőmodul mellé, számítógéphez, DAC-hoz vagy más vonalszintű audióforráshoz.

#### Kérdések és válaszok

**Mi ez a termék pontosan?**  
Az XH-M577 egy **kétcsatornás sztereó digitális erősítőmodul**, amely a **TPA3116D2** erősítő IC-re épül, és beépített hangszínszabályzással rendelkezik.

**Milyen tápfeszültséggel működik?**  
A forgalmazói adatok szerint **12–24 V DC** tápfeszültséggel használható.

**Mekkora teljesítményű?**  
A modul piacán jellemzően **2×80 W** teljesítménnyel hirdetik, de a TPA3116D2 hivatalos chipadatai alapján a gyakorlati, tartós teljesítmény inkább a tápfeszültségtől és a hangszóró impedanciájától függ; a chip hivatalosan **2×50 W / 4 Ω / 21 V** körüli teljesítményt tud megfelelő hűtéssel.

**Mit jelent az, hogy TPA3116D2 alapú?**  
Azt, hogy a modul lelke a Texas Instruments **TPA3116D2 Class-D erősítő IC**, amely nagy hatásfokú, sztereó erősítőchip. A TI adatlap szerint ez a chip akár **100 W / 2 Ω mono**, illetve **2×50 W / 4 Ω sztereó** alkalmazásokra is használható megfelelő körülmények között.

**Milyen hangsugárzóval használható?**  
A kereskedelmi listázások szerint **4–8 ohmos** hangszórókhoz ajánlott.

**Van rajta hangerőszabályzó?**  
Igen, a termékleírások szerint van **master volume** szabályzó.

**Van rajta mély- és magashang-állítás is?**  
Igen, az XH-M577 egyik fontos előnye, hogy **külön bass és treble** szabályzást kínál.

**Milyen erősítőosztályba tartozik?**  
**D osztályú** erősítőmodulról van szó, amit a forgalmazói adatok is külön megemlítenek.

**Mekkora áramú tápegység kell hozzá?**  
A listázások szerint a modulhoz **5 A körüli tápegység** ajánlott, különösen nagyobb hangerőn vagy 4 ohmos hangszóró mellett.

**Mekkora a bemeneti impedanciája?**  
A kereskedelmi adatok szerint a bemeneti impedancia **1 kΩ**.

**DIY hangfalhoz jó választás?**  
Igen, kifejezetten jó lehet saját építésű hangfalhoz vagy kis erősítős projekthez, mert a panel kompakt, sztereó, és a hangszín is állítható. Ez a modul felépítéséből és a kezelőszerveiből következik.

**Bluetooth-os önmagában?**  
Nem, a megadott XH-M577 modul alapvetően **erősítőpanel**, nem beépített Bluetooth vevő. Bluetooth-os használathoz külön Bluetooth audio modult vagy Bluetooth forrást kell elé tenni. Ezt a listázások is úgy mutatják, mint önálló audio amplifier boardot.

**Számítógéphez vagy DAC-hoz használható?**  
Igen, ha a forrás vonalszintű analóg jelet ad, az XH-M577 jól használható utána teljesítményerősítőként. Ez a bemeneti impedanciából és az audio amplifier board jellegből következik.

**Kell hűtés a modulnak?**  
Nagyobb teljesítménynél igen, a TPA3116D2 chip hivatalos adatai is jelzik, hogy a nagyobb kimenő teljesítmény megfelelő hőelvezetést igényel. A panelen jellemzően gyári hűtés is található, de a terheléstől függően a jó szellőzés fontos.

**Kezdőknek is jó választás?**  
Igen, mert egyszerűen használható, kevés vezetékezést igényel, és gyorsan beépíthető egy DIY hangprojektbe. A hangszínszabályzás miatt különösen hálás panel első hangfalépítésekhez is.

**Valóban hi-fi hangminőséget ad?**  
A TPA3116D2 chip ismert, jó hatásfokú audió erősítő, de a végső hangminőség a tápegységtől, a hangszóróktól, a doboztól és a bemeneti forrástól is nagyban függ. A modul alkalmas jó minőségű hobbi és DIY hangprojektekhez, de a teljes rendszer együtt határozza meg az eredményt.

#### Konkrét használati példa

Tegyük fel, hogy egy **műhelybe vagy dolgozószobába** szeretnél egy saját építésű sztereó hangrendszert. Az XH-M577 modult összekötöd egy **24 V-os, megfelelő áramerősségű tápegységgel**, rákötsz két **4 vagy 8 ohmos hangszórót**, a bemenetére pedig egy Bluetooth vevőmodult vagy számítógép analóg kimenetét csatlakoztatod. Ezután a panelen külön beállíthatod a **hangerőt**, a **mélyet** és a **magast**, így a hangzást a helyiséghez és a hangsugárzókhoz igazíthatod. Ez egy egyszerű, kompakt és jól használható megoldás lehet saját építésű aktív hangfal vagy kis asztali erősítő készítéséhez.

**Képek**

1. https://modulshop.cdn.shoprenter.hu/custom/modulshop/image/data/product/2026-Q2/5-1-46_XH-M577-1.webp (alt: XH-M577 sztereó erősítőmodul)
2. https://modulshop.cdn.shoprenter.hu/custom/modulshop/image/data/product/2026-Q2/5-1-46_XH-M577-2.webp (alt: XH-M577 sztereó erősítőmodul)
3. https://modulshop.cdn.shoprenter.hu/custom/modulshop/image/data/product/2026-Q2/5-1-46_XH-M577-3.webp (alt: XH-M577 sztereó erősítőmodul)
4. https://modulshop.cdn.shoprenter.hu/custom/modulshop/image/data/product/2026-Q2/5-1-46_XH-M577-4.webp (alt: XH-M577 sztereó erősítőmodul)
5. https://modulshop.cdn.shoprenter.hu/custom/modulshop/image/data/product/2026-Q2/5-1-46_XH-M577-5.webp (alt: XH-M577 sztereó erősítőmodul)
6. https://modulshop.cdn.shoprenter.hu/custom/modulshop/image/data/product/2026-Q2/5-1-46_XH-M577-6.webp (alt: XH-M577 sztereó erősítőmodul)

### Multiméter DT-830B

| Mező | Érték |
|---|---|
| Handle | `multimeter-dt-830b` |
| Cikkszám (SKU) | 8-1-1 |
| Ár (Ft, bruttó) | 1800 |
| Készlet (db) | 171 |
| Terméktípus | Műszerek |
| Kollekció(k) | Műszerek (`muszerek`) |
| Vonalkód (GTIN) | 5999572383473 |
| SEO-cím | Multiméter DT-830B |
| SEO-leírás | Multiméter DT-830B A DT830B digitális multiméter egy megbízható eszköz HOBBI felhasználásra. A műszer ICL7106 IC –re épül. Nagy 3 + 1 / 2 számjegyű, 7 szegmenses, 0,5” LCD kijelző. Max.: 1999. Méréshatárok: - DCV (0,1 mV - 1000V), - ACV (0,1 V - 750V), - DCA (0,1 mA - 10A), - Ohm (0,1 Ω - 2MΩ) - Dióda - PNP és NPN... |

**Leírás**

**Multiméter DT-830B**

A DT830B digitális multiméter egy megbízható eszköz HOBBI felhasználásra.

A műszer ICL7106 IC –re épül.  
Nagy 3 + 1 / 2 számjegyű, 7 szegmenses, 0,5” LCD kijelző. Max.: 1999.

Méréshatárok:

- DCV (0,1 mV - 1000V),
- ACV (0,1 V - 750V),
- DCA (0,1 mA - 10A),
- Ohm (0,1 Ω - 2MΩ)
- Dióda
- PNP és NPN tranzisztorok

Belső ellenállása feszültség mérésekor **1MOhm**

**Képek**

1. https://modulshop.cdn.shoprenter.hu/custom/modulshop/image/data/product/08%20M%C5%B1szerek/8-1-1%20Multimeter-DT830B-1.jpg (alt: Multiméter DT-830B)
2. https://modulshop.cdn.shoprenter.hu/custom/modulshop/image/data/product/08%20M%C5%B1szerek/8-1-1%20Multimeter-DT830B-2.jpg (alt: Multiméter DT-830B)
3. https://modulshop.cdn.shoprenter.hu/custom/modulshop/image/data/product/08%20M%C5%B1szerek/8-1-1%20Multimeter-DT830B-3.jpg (alt: Multiméter DT-830B)

*Megjegyzés a forrásból: ennél a terméknél a régi morzsamenüben csak „Összes termék” állt; a típust a kategórialistából vettük (README, „Adatminőségi megfigyelések”).*

### Relé modul 1 portos 5V/220V

| Mező | Érték |
|---|---|
| Handle | `rele-modul-1-portos-5v220v` |
| Cikkszám (SKU) | 3-1-36 |
| Ár (Ft, bruttó) | 600 |
| Készlet (db) | 190 |
| Terméktípus | Egyéb Modulok |
| Kollekció(k) | Egyéb Modulok (`egyeb-modulok`); Relék / optocsatolók (`relek-optocsatolok`) |
| Címkék | Relék / optocsatolók |
| Vonalkód (GTIN) | 5999572382551 |
| SEO-cím | Relé modul 1 portos 5V/220V - Modulshop |
| SEO-leírás | Ez a modul megfelel a nemzetközi biztonsági szabványnak, az ellenőrzési területeken és a raktéren szigetelő horony van; - Használható mikrokontroller fejlesztőkártya modulként, használható háztartási készülék vezérléseként; - Egyenáramú vagy váltóáramú jelvezérlés, 220 V AC terhelést vezérelhet; - Maximális... |

**Leírás**

**Relé modul 1 portos 5V/220V**

- Ez a modul megfelel a nemzetközi biztonsági szabványnak, az ellenőrzési területeken és a raktéren szigetelő horony van;
- Használható mikrokontroller fejlesztőkártya modulként, használható háztartási készülék vezérléseként;
- Egyenáramú vagy váltóáramú jelvezérlés, 220 V AC terhelést vezérelhet;
- Maximális kapcsolható áram/feszültség: 10A/250VAC
- Méret: 76 x 55,5 x 20mm

**Képek**

1. https://modulshop.cdn.shoprenter.hu/custom/modulshop/image/data/product/03%20egy%C3%A9b%20modulok/01%20Beviteli%20eszk%C3%B6z%C3%B6k/3-1-26-rele.png (alt: Relé modul 1 portos 5V/220V)
2. https://modulshop.cdn.shoprenter.hu/custom/modulshop/image/data/product/03%20egy%C3%A9b%20modulok/01%20Beviteli%20eszk%C3%B6z%C3%B6k/3-1-26-rele-1.png (alt: Relé modul 1 portos 5V/220V)

### Próbapanel/breadboard jumper vezetékek /65 db

| Mező | Érték |
|---|---|
| Handle | `probapanelbreadboard-jumper-vezetekek-65-db` |
| Cikkszám (SKU) | 9-1-16 |
| Ár (Ft, bruttó) | 700 |
| Készlet (db) | 116 |
| Terméktípus | Elektronika |
| Kollekció(k) | Elektronika (`elektronika`); Kapcsolók / csatlakozók / vezetékek (`kapcsolok-csatlakozok-vezetekek`) |
| Címkék | Kapcsolók / csatlakozók / vezetékek |
| Vonalkód (GTIN) | 5999572383725 |
| SEO-cím | Próbapanel/breadboard jumper vezetékek /65 db |
| SEO-leírás | Próbapanel/breadboard jumper vezetékek /65 db - 1LOT = 65PCS 65 tesztvonal teljes hossza: - 24 cm (a tűrésszel együtt) - 20 cm (a tűrésszel együtt) - 16 cm (a tűrésszel együtt) - 12 cm (a tűrésszel együtt) |

**Leírás**

**Próbapanel/breadboard jumper vezetékek /65 db**

- 1LOT = 65PCS 65 tesztvonal teljes hossza:
- 24 cm (a tűrésszel együtt)
- 20 cm (a tűrésszel együtt)
- 16 cm (a tűrésszel együtt)
- 12 cm (a tűrésszel együtt)

**Képek**

1. https://modulshop.cdn.shoprenter.hu/custom/modulshop/image/data/product/09%20Egy%C3%A9b/9-1-15186480915_377505140255958_8558796665788142321_n.png (alt: Próbapanel/breadboard jumper vezetékek /65 db)
2. https://modulshop.cdn.shoprenter.hu/custom/modulshop/image/data/product/09%20Egy%C3%A9b/9-1-15186480915_377505140255958_8558796665788142321_n_2.png (alt: Próbapanel/breadboard jumper vezetékek /65 db)
3. https://modulshop.cdn.shoprenter.hu/custom/modulshop/image/data/product/09%20Egy%C3%A9b/187018000_170231651680812_2481735677109798353_n_2.png (alt: Próbapanel/breadboard jumper vezetékek /65 db)

## 3. Kollekciók

Forrás: `docs/import/collections.md`. Mind automatikus kollekció. Az alkollekció neve a forrás szerint megegyezik a címkével (vessző helyett „ / ”); a vásárlónak látszó cím később átírható, mert a feltétel nem a címhez kötődik.

| Név | Handle | Szülő | Megjegyzés |
|---|---|---|---|
| Mikrovezérlők, alaplapok | `mikrovezerlok-alaplapok` | – | Feltétel: Terméktípus = `Mikrovezérlők, alaplapok`. A csomag termékei: 1-2-29, 1-1-27. |
| Szenzor Modulok | `szenzor-modulok` | – | Feltétel: Terméktípus = `Szenzor Modulok`. A csomag termékei: 2-1-1. |
| Egyéb Modulok | `egyeb-modulok` | – | Feltétel: Terméktípus = `Egyéb Modulok`. A csomag termékei: 3-1-36. |
| Erősítők, Végfokok | `erositok-vegfokok` | – | Feltétel: Terméktípus = `Erősítők, Végfokok`. A csomag termékei: 5-1-46. |
| LCD-k, Kijelzők | `lcd-k-kijelzok` | – | Feltétel: Terméktípus = `LCD-k, Kijelzők`. A csomag termékei: 4-1-21. |
| BMS-ek, 18650 Akkuk | `bms-ek-18650-akkuk` | – | Feltétel: Terméktípus = `BMS-ek, 18650 Akkuk`. Ebben a csomagban nincs termék benne (a főoldali csempék és a menü linkelnek rá). |
| DC, AC konverterek | `dc-ac-konverterek` | – | Feltétel: Terméktípus = `DC, AC konverterek`. Ebben a csomagban nincs termék benne (a főoldali csempék és a menü linkelnek rá). |
| Műszerek | `muszerek` | – | Feltétel: Terméktípus = `Műszerek`. A csomag termékei: 8-1-1. |
| Egyéb | `egyeb` | – | Feltétel: Terméktípus = `Egyéb`. Ebben a csomagban nincs termék benne (a főoldali csempék és a menü linkelnek rá). |
| Elektronika | `elektronika` | – | Feltétel: Terméktípus = `Elektronika`. A csomag termékei: 9-1-16. |
| D.I.Y. Készletek | `diy-keszletek` | – | Feltétel: Terméktípus = `D.I.Y. Készletek`. Ebben a csomagban nincs termék benne (a főoldali csempék és a menü linkelnek rá). |
| Led világítás | `led-vilagitas` | – | Feltétel: Terméktípus = `Led világítás`. Ebben a csomagban nincs termék benne (a főoldali csempék és a menü linkelnek rá). |
| Arduino | `arduino` | Mikrovezérlők, alaplapok (`mikrovezerlok-alaplapok`) | Feltétel: Termékcímke = `Arduino`. A csomag termékei: 1-1-27. A főoldal linkel rá. |
| ESP32 | `esp32` | Mikrovezérlők, alaplapok (`mikrovezerlok-alaplapok`) | Feltétel: Termékcímke = `ESP32`. A csomag termékei: 1-2-29. A főoldal linkel rá. |
| Hőmérséklet / pára / nyomás | `homerseklet-para-nyomas` | Szenzor Modulok (`szenzor-modulok`) | Feltétel: Termékcímke = `Hőmérséklet / pára / nyomás`. A csomag termékei: 2-1-1. |
| Relék / optocsatolók | `relek-optocsatolok` | Egyéb Modulok (`egyeb-modulok`) | Feltétel: Termékcímke = `Relék / optocsatolók`. A csomag termékei: 3-1-36. A főoldal linkel rá. |
| 2*50W erősítő / végfok | `2x50w-erositok-vegfokok` | Erősítők, Végfokok (`erositok-vegfokok`) | Feltétel: Termékcímke = `2*50W erősítő / végfok`. A csomag termékei: 5-1-46. |
| Szerszámok | `szerszamok` | Egyéb (`egyeb`) | Feltétel: Termékcímke = `Szerszámok`. Ebben a csomagban nincs termék benne. A főoldali kategóriacsempe linkel rá (`templates/index.json`). |
| Kapcsolók / csatlakozók / vezetékek | `kapcsolok-csatlakozok-vezetekek` | Elektronika (`elektronika`) | Feltétel: Termékcímke = `Kapcsolók / csatlakozók / vezetékek`. A csomag termékei: 9-1-16. |
| Általunk készített termékek | `sajat-termekeink` | – (kiemelt kollekció) | Feltétel: Termékcímke = `Saját termék`. A főmenü és a téma lábléce linkel rá. Ebben a csomagban nincs termék benne (a 36 mintatermék közül egyik sem ilyen). |
| Csomagok | `csomagok` | – (kiemelt kollekció) | Feltétel: Termékcímke = `Csomag`. A főmenü és a téma lábléce linkel rá. Ebben a csomagban nincs termék benne. |

**Kollekcióleírások a forrásból** (új állítást nem tartalmaznak; ahol a régi oldalon nem volt leírás, ott üresen marad):

- **Mikrovezérlők, alaplapok:** A Modulshop mikrovezérlői ár-érték arányban a legjobbak Magyarországon. Arduino, ESP, STM és sok más kínálatunk mellett rengeteg kiegészítőt is találsz. Folyamatosan bővülő termékpalettánkon megtalálsz mindent, amire csak szükséged van. *(A forrás megjegyzése: az „ár-érték arányban a legjobbak Magyarországon” a régi oldal állítása; hirdetésben csak alátámasztva használd.)*
- **Szenzor Modulok:** Webáruházunk egyik legszélesebb választékával a szenzormodulok rendelkeznek. Hőmérséklet-, pára- és nyomás-, feszültség-, áram- és távolság-, valamint fény-, mozgás-, giroszkóp-, gyorsulás- és RFID-érzékelő modulok közül válogathattok.
- **Egyéb Modulok:** Folyamatosan bővülő kategóriánkban jelenleg beviteli eszközökkel, kommunikációs modulokkal és motorvezérlőkkel találkozhattok.
- **Erősítők, Végfokok:** Nagy teljesítményű erősítők és végfokok audió kiegészítőkkel megspékelve, mindenkinek, aki érdeklődik a hangtechnika iránt.
- **BMS-ek, 18650 Akkuk:** Kategóriánkban akkutöltőket, 1S–13S BMS-eket és a hozzájuk tartozó kiegészítőket találod.
- **DC, AC konverterek:** Webáruházunk DC és AC konverterei. Alkategóriák: AC-DC tápegységek, DC-DC step down (feszültségcsökkentő) és DC-DC step up (feszültségnövelő) konverterek.
- **Arduino:** A Modulshop AVR mikrovezérlői 100%-osan kompatibilisek az Arduino alaplapjaival. Az Uno, Nano, Pro Micro és Leonardo mellett sok más fejlesztőpanelt is megtalálsz a shopban. Termékeinkre maximális csere garanciát vállalunk!
- **ESP32:** ESP32 alaplapok.
- **Hőmérséklet / pára / nyomás:** Hőmérséklet-, pára- és nyomásérzékelő szenzormodulokon felül nagyon sok kiegészítővel találkozhattok, többek között eső- és hóérzékelő panellel.
- **Relék / optocsatolók:** Relémodulok: hagyományos, behúzótekercses és szilárdtest relék.
- **2*50W erősítő / végfok:** 2×50 W fölötti erősítők és végfokok bőséges választéka. Közkedvelt, nagy teljesítményű erősítőink között megtalálod például a ZK-502L HiFi sztereó erősítőt és az APL50L 2×50 W-os erősítőt.
- **Általunk készített termékek:** Általunk készített, tervezett vagy gyártott termékeket találhatsz itt. Fő terméktervezőnk és készítőnk: Bán Péter.
- **Leírás nélkül** (a régi oldalon nem volt, a tulajdonos írja meg): LCD-k, Kijelzők; Műszerek; Egyéb; Elektronika; D.I.Y. Készletek; Led világítás; Szerszámok; Kapcsolók / csatlakozók / vezetékek; Csomagok.

## 4. Oldalak

Forrás: `docs/import/pages.md` és `docs/import/pages/*.html` (a fájlok eleji, a tulajdonosnak szóló HTML-megjegyzés nélkül). A „Sablon” a téma sablonja (`page.<utótag>`). A hosszú jogi szövegeknél itt csak az első bekezdés áll; a teljes szöveget a tulajdonos illeszti be a megadott fájlból, HTML-nézetben.

### Rólunk

Handle: `rolunk` · Sablon: `page.about` (utótag: `about`)

*Állapot / megjegyzés (pages.md):* **TERVEZET.** Csak ellenőrzött tényekből áll. A „2019 óta” csak a copyright-sorból következik.

**TERVEZET – a tulajdonos jóváhagyására vár. Közzététel előtt ezt a sort töröld.**

#### A Modulshopról

A Modulshop magyar elektronikai webáruház. Kínálatunkban Arduino-kompatibilis és ESP mikrovezérlők, szenzor- és egyéb modulok, kijelzők, erősítők, BMS-ek és akkumulátorok, DC-DC és AC-DC átalakítók, műszerek, alkatrészek és DIY készletek találhatók. A kínálat 2026 novemberében több mint 1800 terméket számlál.

2019 óta szolgáljuk ki a hobbielektronikával, robotikával és mikrovezérlős fejlesztéssel foglalkozó vásárlóinkat.

#### Saját fejlesztésű termékek

Nemcsak forgalmazunk: saját magunk által tervezett, készített vagy gyártott termékeink is vannak. Ilyenek például a műszerdobozok, a szív alakú RGB LED lámpa DIY készlet és az ESP32 alapú TankBot 1.0 DIY készlet. Fő terméktervezőnk és készítőnk: **Bán Péter**.

Egyedi, 3D nyomtatott műszerdobozt is készítünk kész STL-fájl vagy méretezett, papíron rajzolt vázlat alapján. Az ajánlatkérés módja: [Saját termékeink](/pages/sajat-termekeink).

[Az általunk készített termékek megtekintése](/collections/sajat-termekeink)

#### Budapesti raktár és átvételi pont

A termékek a budapesti raktárunkból indulnak. Raktárunk egyben átvételi pont is: 1078 Budapest, Nefelejcs utca 43. (bejárat a Marek József utca felől). Az online leadott rendelés a visszaigazoló e-mail után nyitvatartási időben azonnal átvehető. A terméklapokon a raktár aktuális készlete látható.

A Modulshop csak webáruházként működik, helyszíni vásárlásra nincs lehetőség.

#### Iskoláknak, intézményeknek, cégeknek

Iskolákat, intézményeket és cégeket is kiszolgálunk. Nagy értékű rendeléseknél egyedi mennyiségi kedvezményt biztosítunk. Részletek: [Iskoláknak és cégeknek](/pages/iskolaknak-es-cegeknek).

#### Versenyek, közösség

2024-ben saját projektversenyt hirdettünk egyedi elektronikai és programozói projektek számára, Modulshop-vásárlási utalvány díjazással. Blogunkban beszámoltunk a nyíregyházi V. Robot Exatlonról is, amelyen általános iskolás csapatok mérték össze saját építésű robotjaikat.

A kínálatunkba eddig több mint 50 olyan termék került be, amelyet vásárlóink javasoltak. Ha nem találod, amit keresel, írj nekünk: [info@modulshop.hu](mailto:info@modulshop.hu).

#### Üzemeltető

Nováki József egyéni vállalkozó. A teljes cégadatok az [Impresszum](/pages/impresszum) oldalon találhatók.

### Kapcsolat

Handle: `kapcsolat` · Sablon: `page.contact` (utótag: `contact`)

*Állapot / megjegyzés (pages.md):* A `contact` sablon kapcsolati űrlapot ad (a régi oldalon nem volt). Az adószámot javítani kell.

#### Átvételi pontunk címe

1078 Budapest, Nefelejcs utca 43.

**Bejárat a Marek József utca felől. Fehér műanyag ajtó, szuterén.**

Az átvételi ponton csak és kizárólag az online leadott rendeléseket áll módunkban kiadni. Helyszíni vásárlásra nincs lehetőség.

#### Nyitvatartás

Hétfő – péntek: 8:00 – 18:00  
Szombat – vasárnap: 10:00 – 16:00

#### Elérhetőségeink

E-mail: [info@modulshop.hu](mailto:info@modulshop.hu)  
Telefon: [+36 70 944 7641](tel:+36709447641)

Üzenetet az alábbi űrlapon is küldhetsz.

#### Cégadatok

Nováki József egyéni vállalkozó  
Székhely: 1081 Budapest, Szilágyi utca 1/b fsz. 1.  
Nyilvántartási szám: 55371672  
Adószám: [[TISZTÁZANDÓ: 56696741-2-42 vagy 56696741-1-42]]

További adatok: [Impresszum](/pages/impresszum)

### Gyakran ismételt kérdések

Handle: `gyik` · Sablon: `page.faq` (utótag: `faq`)

*Állapot / megjegyzés (pages.md):* A két forrás összefésülve. Kérdés = `<h3>`, így a FAQ-sablon harmonikává alakíthatja.

##### A feltüntetett ár bruttó vagy nettó?

Az árak bruttóban értendők, tartalmazzák az ÁFÁ-t.

##### Elérhető-e a termék, amit rendelni szeretnék?

A terméklapon az elérhetőség mellett látható, hogy az adott termékből aktuálisan mennyi van készleten. Ez az érték mindig a raktár aktuális számait mutatja, ennél több vagy kevesebb nem érhető el a termékből. Ha a vásárolni kívánt mennyiség elérhető a készleten, a kiszállítás 1–4 munkanapon belül megtörténik.

Ha a termék nincs készleten, „értesítés” státuszban van. Ilyenkor e-mail-értesítést kérhetsz, és automatikusan értesítünk a megadott e-mail-címen, amint a termék beérkezett.

##### Mennyi idő alatt kapom meg a megrendelt terméket?

Ha a termék elérhető a raktárunkban, a rendelés leadását követő 1–4 munkanapon belül kiszállítjuk.

Az „értesítés” státuszú termékek átlagosan 14–45 nap alatt érkeznek be.

##### Van lehetőség személyes átvételre?

Igen! A rendelés leadása után a megadott e-mail-címre visszaigazoló üzenet érkezik. Ezt követően a rendelés azonnal átvehető a raktárunkban, az átvételi ponton azonnal csomagolunk:

**1078 Budapest, VII. Nefelejcs utca 43. (Bejárat a Marek József utca felől)**

- Hétfő – péntek: 08:00 – 18:00
- Szombat – vasárnap: 10:00 – 16:00

##### Helyszínen vásárolhatok?

Nem. A Modulshop csak webáruházként üzemel, helyszíni vásárlásra sajnos nincs lehetőség.

##### Jár garancia a megvásárolt árucikkekhez?

Igen. Termékeink mindegyikére 1 éves garanciát vállalunk!

A garancia érvényét veszti, ha a hiba a termék nem szakértő vagy nem rendeltetésszerű használata miatt keletkezett.

Részletek: [Garancia és visszaküldés](/pages/garancia-es-visszakuldes)

##### Van lehetőség előrendelésre?

Természetesen igen. Egyedi megkereséseket az [info@modulshop.hu](mailto:info@modulshop.hu) e-mail-címen fogadunk.

Iskolák és cégek nagy értékű rendelései esetén egyedi mennyiségi kedvezményeket biztosítunk! Részletek: [Iskoláknak és cégeknek](/pages/iskolaknak-es-cegeknek)

##### Nem találom a keresett terméket. Miért?

Készletünk folyamatosan bővül. Az [info@modulshop.hu](mailto:info@modulshop.hu) e-mail-címre várunk minden termékekkel kapcsolatos ajánlást. A webshop kínálatába már több mint 50 olyan termék került fel, amelyet vásárlóink ajánlottak.

### Szállítás és fizetés

Handle: `szallitas-es-fizetes` · Sablon: `page.shipping` (utótag: `shipping`)

*Állapot / megjegyzés (pages.md):* A GLS automata ára `[[TISZTÁZANDÓ]]`.

#### Személyes átvétel (ingyenes)

A rendelésed leadása után nyitvatartási időben azonnal jöhetsz a termékekért. Az átvételi ponton csak és kizárólag az online leadott rendeléseket áll módunkban kiadni.

Átvételi pont: 1078 Budapest, Nefelejcs utca 43. (Bejárat a Marek József utca felől.) Fehér műanyag ajtó, szuterén.

Nyitvatartás:  
Hétfő – péntek: 08:00 – 18:00  
Szombat – vasárnap: 10:00 – 16:00

#### Rendelés kiszállítással

Minden nagyobb futárcéggel szerződésben állunk: MPL, GLS, Foxpost (Packeta).

A rendelésedet kérheted csomagautomatába (jelenleg ez a legnépszerűbb és legolcsóbb), házhoz, csomagpontba vagy postahivatalba. A rendelésedet a lehető leghamarabb becsomagoljuk és átadjuk a futárnak.

#### Szállítási díjak

##### Csomagautomatába

- Foxpost: 1250 Ft
- MPL: 1250 Ft
- GLS: [[TISZTÁZANDÓ: 1300 Ft vagy 1350 Ft]]

##### Házhozszállítás

- MPL: 1700 Ft
- GLS: 1950 Ft

##### Csomagpontba / postára

- Posta: 1400 Ft
- GLS: 2000 Ft

#### Szállítási idő

Ha a termék elérhető a raktárunkban, a rendelés leadását követő 1–4 munkanapon belül kiszállítjuk. Az „értesítés” státuszú (nem készleten lévő) termékek átlagosan 14–45 nap alatt érkeznek be.

Az ÁSZF szerint a szállítási határidő a megrendelés beérkezésétől számított legfeljebb 10 munkanap, kivéve, ha a termék nincs raktáron. Részletek: [ÁSZF](/pages/aszf).

#### Fizetési módok

- **Bankkártyával**, online, a megrendeléskor (BARION rendszeren keresztül). Elfogadott kártyatípusok: Visa, Electron, MasterCard, Maestro, American Express.
- **Előre utalással**, banki átutalással a megrendeléskor.
- **Utánvéttel**, az áru átvételekor. A teljes vételárat a szállítási költséggel együtt a küldemény átvételekor kell kifizetni a kézbesítőnek.
- **Személyes átvételkor** készpénzzel (kizárólag magyar forintban) vagy azonnali banki átutalással.

A termékek árai az általános forgalmi adót tartalmazó bruttó árak. A vételár nem tartalmazza a kiszállítás, csomagküldés, illetve utánvét költségét.

### Garancia és visszaküldés

Handle: `garancia-es-visszakuldes` · Sablon: alapértelmezett (`page`)

*Állapot / megjegyzés (pages.md):* Ellentmond az ÁSZF 15.2 pontjának (a visszaküldés költsége).

*Eltérés a forrásokban: a `pages.md` szerint ez az oldal az alapértelmezett sablont kapja, a `README.md` sablontáblázata szerint `page.shipping`-et. A tulajdonos döntse el.*

#### 1 év garancia

Termékeink mindegyikére 1 éves garanciát (jótállást) vállalunk!

A garancia érvényét veszti, ha a hiba a termék nem szakértő vagy nem rendeltetésszerű használata miatt keletkezett. Meghibásodás esetén vedd fel velünk a kapcsolatot valamelyik elérhetőségünkön, és tájékoztatunk a teendőkről. A jótállás, a kellék- és a termékszavatosság részletes szabályai az [ÁSZF](/pages/aszf)-ben találhatók.

#### 30 napos termék-visszaküldés

Mert mi tisztában vagyunk vele, hogy minőségi termékeket árulunk! Ha nem vagy megelégedve a megvásárolt termékkel, kérjük, jelezd ügyfélszolgálatunknak írásban az [info@modulshop.hu](mailto:info@modulshop.hu) e-mail-címen. Mi pedig a vásárlástól számított 30 napon belül kérdés nélkül visszatérítjük a vételárat, vagy kicseréljük a terméket.

A garancia érvényesítése egyszerű, diszkrét és kérdések nélkül történik. Ebben az esetben a vásárló egyetlen kötelezettsége, hogy a vásárlást követő 30 napon belül e-mailben értesít minket a reklamációról. Mi felvesszük veled a kapcsolatot, tájékoztatunk a visszaküldési lehetőségekről és a csereterméküldésről, és egyeztetünk az esetleges vételár-visszatérítésről.

A visszaküldés vagy a cseretermék küldésének költségeit természetesen mi álljuk.

#### Ingyenes visszaküldés GLS automatán keresztül

Kedves Vásárlónk!

Ha a vásárolt terméket bármely okból vissza szeretnéd küldeni, ezt GLS automatán keresztül a mi költségünkre megteheted. Az alábbi linkre kattintva csak a feladó adatait kell megadni. A kapott kóddal a csomag bármely GLS automatában feladható.

[**GLS visszaküldés**](https://ecsomag.hu/hu/visszaru?data=eSXL0ZVtpyrtWT9XpGIjw6r7uYJ1zsBUuzaAcgN6jngRRe0%2f61ZtH3JfBf3Evv%2bGFK8Vx4r0qpJYjTNyGZZT9g%3d%3d)

#### 14 napos elállási jog

A fenti önként vállalt lehetőségektől függetlenül a fogyasztót a 45/2014. (II. 26.) Korm. rendelet alapján a termék kézhezvételétől számított 14 napon belül megilleti az indokolás nélküli elállás joga. Részletek és nyilatkozatminta: [Elállás](/pages/elallas).

### Hűségpont rendszer

Handle: `husegpont` · Sablon: alapértelmezett (`page`)

*Állapot / megjegyzés (pages.md):* Csak akkor tedd közzé, ha a hűségpont-alkalmazás már működik.

2026. január 1-jétől bevezettük a regisztrációhoz kötött hűségpontgyűjtést. Ezzel visszatérő vásárlóinknak további 5% (akciós termékekre további 1%) kedvezményt adunk.

Minden regisztrált felhasználó hűségpontokat kap a vásárlásai után.

A már megszerzett pontokat a pénztár oldalakon lehet beváltani. 1 pont = 1 Ft. A beváltott pontok után járó forintkedvezményt a fizetendő végösszegből vonjuk le.

A normál áras termékek után a bruttó ár 5%-ának megfelelő pontot kapnak a regisztrált és bejelentkezett vásárlók. A számítás menete: minden elköltött 20 forint után 1 pont jár. Az akcióban részt vevő termékek után 1% a pontjóváírás, vagyis minden 100 forint után 1 pont jár.

#### Miért érdemes regisztrálni?

A pontok a pénztár oldalakon válthatók be, minden pont 1 Ft-ot ér. Kedvezményként is felhasználhatod, vagy beszámíthatod a szállítási költségbe. Sok pont beváltásakor akár ingyen termékekhez vagy ingyenes szállításhoz is juthatsz.

[Regisztráció](/account/register)

### Iskoláknak és cégeknek

Handle: `iskolaknak-es-cegeknek` · Sablon: `page.b2b` (utótag: `b2b`)

*Állapot / megjegyzés (pages.md):* **TERVEZET.** Új oldal, ellenőrzött tényekből.

**TERVEZET – a tulajdonos jóváhagyására vár. Közzététel előtt ezt a sort töröld.**

Iskolákat, intézményeket és cégeket is kiszolgálunk.

#### Mennyiségi kedvezmény

Iskolák és cégek nagy értékű rendeléseire egyedi mennyiségi kedvezményt biztosítunk. Ajánlatkérés: [info@modulshop.hu](mailto:info@modulshop.hu).

#### Előrendelés, egyedi igények

Előrendelésre is van lehetőség. Egyedi megkereséseket az [info@modulshop.hu](mailto:info@modulshop.hu) e-mail-címen fogadunk. Ha a keresett termék nincs a kínálatunkban, azt is jelezd. Már több mint 50 termék került be a kínálatba vásárlói javaslatra.

#### Készlet és szállítás

A terméklapokon a budapesti raktárunk aktuális készlete látható. A raktáron lévő termékeket a rendeléstől számított 1–4 munkanapon belül kiszállítjuk. A rendelés a budapesti átvételi pontunkon (1078 Budapest, Nefelejcs utca 43.) személyesen is átvehető. Részletek: [Szállítás és fizetés](/pages/szallitas-es-fizetes).

#### Fizetés

A megrendelés ellenértéke előre utalással (banki átutalással) is kifizethető. További fizetési módok: bankkártya, utánvét, valamint személyes átvételkor készpénz vagy azonnali átutalás.

#### Egyedi, 3D nyomtatott műszerdobozok

Projektekhez, laborokhoz egyedi, 3D nyomtatott műszerdobozt készítünk kész STL-fájl vagy méretezett, papíron rajzolt vázlat alapján. Az egyedi árajánlat 2000 Ft-tól indul, a szállítási költségen felül. Megrendelés e-mailben az [info@modulshop.hu](mailto:info@modulshop.hu) címen, a levél tárgya legyen: **Műszerdoboz**.

#### Oktatás és versenyek

Kínálatunkban oktatási célra is használható DIY készletek, robotkészletek és alkatrészek találhatók. Ilyen például a [D.I.Y. Készletek](/collections/diy-keszletek) és a [Csomagok](/collections/csomagok) kollekció. 2024-ben saját projektversenyt hirdettünk, blogunkban pedig beszámoltunk a nyíregyházi V. Robot Exatlon általános iskolás robotversenyről.

### Általános Szerződési Feltételek

Handle: `aszf` · Sablon: `page.legal` (utótag: `legal`)

*Állapot / megjegyzés (pages.md):* Szó szerinti szöveg, tisztított formázással. Platformváltás miatt frissíteni kell (tárhely, fizetés).

Az Általános Szerződési Feltételek („ÁSZF”) tartalmazzák a Nováki József egyéni vállalkozó, mint kereskedő által üzemeltetett webáruház használatára vonatkozó általános szerződési feltételeket. Kérjük, figyelmesen olvassa el az általános szerződési feltételeket és csak azt követően vegye igénybe szolgáltatásainkat, amennyiben minden pontjával egyetért, és kötelező érvényűnek tekinti magára nézve. Jelen dokumentum nem kerül iktatásra, kizárólag elektronikus formában kerül megkötésre (nem minősül írásban foglalt szerződésnek), magatartási kódexre nem utal.

*A teljes szöveg (41831 karakter): `docs/import/pages/aszf.html` (a fájl eleji `<!-- … -->` megjegyzés nélkül illeszd be).*

### Adatvédelmi nyilatkozat

Handle: `adatvedelem` · Sablon: `page.legal` (utótag: `legal`)

*Állapot / megjegyzés (pages.md):* Szó szerinti szöveg. A Shopify-t adatfeldolgozóként fel kell venni.

#### ADATKEZELÉSI TÁJÉKOZTATÓ

#### 1. Bevezető

A vállalkozásom kiemelten fontosnak tartja Ügyfelei és Partnerei személyes adatainak védelmét, információs önrendelkezési jogának tiszteletben tartását. A webáruházunk használata során vásárlóink által eljuttatott személyes adatokat bizalmasan kezeli, és megtesz minden olyan biztonsági, technikai és szervezési intézkedést, mely az adatok biztonságát garantálja.

*A teljes szöveg (28609 karakter): `docs/import/pages/adatvedelem.html` (a fájl eleji `<!-- … -->` megjegyzés nélkül illeszd be).*

### Impresszum

Handle: `impresszum` · Sablon: `page.legal` (utótag: `legal`)

*Állapot / megjegyzés (pages.md):* A tárhelyszolgáltató adatai `[[KITÖLTENDŐ]]`.

#### Szolgáltató adatai

A kereskedő neve: Nováki József egyéni vállalkozó  
Székhely: 1081 Budapest, Szilágyi utca 1/b fsz. 1.  
Nyilvántartási szám: 55371672  
Adószám: [[TISZTÁZANDÓ: 56696741-2-42 vagy 56696741-1-42]]  
OKNYIR (Országos Kereskedelmi Nyilvántartás) nyilvántartási szám: 306071/B/1  
A területi nyilvántartásba vétel száma: 8853/2021/B

#### Elérhetőség

E-mail: [info@modulshop.hu](mailto:info@modulshop.hu)  
Telefon: [+36 70 944 7641](tel:+36709447641)  
Átvételi pont: 1078 Budapest, Nefelejcs utca 43. (bejárat a Marek József utca felől)

#### Egyéb adatok

A szerződés nyelve: magyar  
Domain-szolgáltató: Rackhost Zrt.  
Tárhelyszolgáltató: [[KITÖLTENDŐ: a Shopify-szerződésben szereplő szolgáltató neve, címe és elérhetősége (a korábbi tárhelyszolgáltató a Shoprenter.hu Kft. volt)]]

Általános Szerződési Feltételek: [ÁSZF](/pages/aszf) · Adatkezelés: [Adatvédelmi nyilatkozat](/pages/adatvedelem)

### Elállás

Handle: `elallas` · Sablon: `page.legal` (utótag: `legal`)

*Állapot / megjegyzés (pages.md):* Bevezető (a régi űrlap mezőiből) + az ÁSZF 14–16. pontja szó szerint. Az online elállási funkcióra megoldás kell.

#### Online elállás

Az elállási szándékodat e-mailben jelezheted az [info@modulshop.hu](mailto:info@modulshop.hu) címen (vagy az alábbi nyilatkozatminta szerint postai úton). Kérjük, add meg a következőket:

- vezetéknév és keresztnév;
- rendelésszám (a rendelés visszaigazoló e-mailjében található, a rendelést azonosító szám);
- a rendeléskor használt e-mail-cím (csak így tudjuk azonosítani az elállási szándékot);
- az elállás a teljes rendelésre vagy csak bizonyos termékekre vonatkozik-e (több termék esetén a terméknevek vesszővel elválasztva).

A termékeket ingyenesen is visszaküldheted GLS automatán keresztül: [Garancia és visszaküldés](/pages/garancia-es-visszakuldes).

#### Az ÁSZF elállásra vonatkozó rendelkezései

Az alábbi szöveg az ÁSZF 14–16. pontja, változtatás nélkül. A teljes szöveg: [ÁSZF](/pages/aszf).

##### 14. Elállási/ felmondási jog

A Fogyasztó vevőt a 45/2014. (II. 26.) Korm. rendelet 20. § szerint megilleti az indokolás nélküli elállás joga.

A Fogyasztó és a Eladó közötti szerződések részletes szabályairól szóló 45/2014. (II.26.) Korm. rendelet szabályozása értelmében Fogyasztó a megrendelt termék kézhez vételétől számított 14 napon belül indoklás nélkül elállhat a szerződéstől, visszaküldheti a megrendelt terméket.

##### 14.1. Elállási nyilatkozat, a fogyasztót megillető elállási vagy felmondási jog gyakorlása

A fogyasztó a 45/2014. (II. 26.) Korm. rendelet 20. §-ban biztosított jogát az erre vonatkozó egyértelmű nyilatkozat útján gyakorolhatja a címre (e-mail vagy postai úton) megküldéssel.

Nyilatkozat-minta elálláshoz:

- Szolgáltató neve:
- Szolgáltató címe:
- Alulírott/ak kijelentem/kijelentjük, hogy gyakorlom/gyakoroljuk elállási/felmondási jogomat/jogunkat az alábbi termék/ek adásvételére vagy az alábbi szolgáltatás nyújtására irányuló szerződés tekintetében:
- Szerződéskötés időpontja /átvétel időpontja:
- A fogyasztó(k) neve:
- A fogyasztó(k) címe:
- A fogyasztó(k) aláírása: (kizárólag papíron tett nyilatkozat esetén)
- Kelt:

##### 15. A fogyasztó kötelezettségei elállása vagy felmondása esetén

##### 15.1. A termék visszaszolgáltatása

A Fogyasztó köteles az árukat indokolatlan késedelem nélkül, de a szerződéstől való elállására vonatkozó értesítés Eladó részére történő megküldésétől számított 14 napon belül visszaküldeni.

A megrendelt terméket postai úton, vagy futárszolgálat segítségével juttathatja vissza a Fogyasztó az Eladó részére.

Az elállási jog gyakorlására nyitva álló idő attól a naptól számított 14 nap elteltével jár le, amelyen a Fogyasztó, vagy meghatalmazottja a terméket átveszi.

##### 15.2. A termék visszaszolgáltatásával kapcsolatos költségek viselése

A termék visszaküldésének költségét a Fogyasztónak kell viselnie, az Eladó nem vállalja e költség viselését. A Fogyasztót a termék visszajuttatásának költségén kívül más költség nem terheli.

##### 15.3. Fogyasztó felelőssége az értékcsökkenésért

A Fogyasztó elállás esetén is felelős azon károk megtérítéséért, amelyek a termék nem rendeltetésszerű használata miatt keletkeztek.

##### 15.4. Az elállási jog kizártsága

Az Eladó felhívja a Fogyasztó figyelmét, hogy a Fogyasztó nem gyakorolhatja elállási jogát a 45/2014 (II.26.) Korm. Rendelet 29. §. (1) bekezdésében foglalt esetekben romlandó vagy minőségét rövid ideig megőrző Termék (így különösen az emberi vagy állati fogyasztásra alkalmas termékek) tekintetében, olyan zárt csomagolású Termék tekintetében, amely egészségvédelmi vagy higiéniai okokból az átadást követő felbontása után nem küldhető vissza (így különösen: tisztítószerek, higiéniai termékek, fehérneműk, alsóruházati termékek, szőrzetnyírók, borotvák, fogkefék), olyan Termék tekintetében, amely jellegénél fogva az átadást követően elválaszthatatlanul vegyül más termékkel, továbbá a lezárt csomagolású hang-, illetve képfelvétel, valamint számítógépes szoftver példányának adásvétele tekintetében, ha az átadást követően a Fogyasztó a csomagolást felbontotta, vagy olyan Termék esetében, amelyet egyértelműen a fogyasztó személyére szabtak (így különösen az egyedi igények alapján megmunkált vagy méretre vágott lineáris vezetékek, szíjak, orsók, tengelyek és szoftverek esetében)

##### 16. Az Eladó kötelezettségei a fogyasztó elállása esetén

##### 16.1. Az Eladó visszatérítési kötelezettsége

Az Eladó a termék visszaérkezését követően a fenti jogszabályok értelmében haladéktalanul, de legkésőbb 14 napon belül visszatéríti a kifizetett összeget a Fogyasztó részére, beleértve a szállítási díjat is.

##### 16.2. Az Eladó visszatérítési kötelezettségének módja

Az Eladó a visszatérítés során az eredeti ügylet során alkalmazott fizetési móddal egyező fizetési módot alkalmaz, kivéve, ha a Fogyasztó más fizetési mód igénybevételéhez kifejezetten a hozzájárulását adja; e visszatérítési mód alkalmazásából kifolyólag a Fogyasztót semmilyen többletköltség nem terheli.

##### 16.3. Visszatartási jog:

Az Eladó mindaddig visszatarthatja a visszatérítendő összeget, amíg a Fogyasztó a terméket vissza nem szolgáltatta, vagy kétséget kizáróan nem igazolta, hogy azt visszaküldte; a kettő közül a korábbi időpontot kell figyelembe venni. Utánvéttel feladott küldeményeket nem áll módunkban elfogadni.

##### 16.4. Többletköltség:

Ha a Fogyasztó kifejezetten a legkevésbé költséges szokásos fuvarozási módtól eltérő fuvarozási módot választ az Eladó nem köteles visszatéríteni az ebből eredő többletköltségeket. Ilyen esetben a feltüntetett általános szállítási díjtételek erejéig áll fenn visszatérítési kötelezettségünk.

### Saját termékeink

Handle: `sajat-termekeink` · Sablon: alapértelmezett (`page`)

*Állapot / megjegyzés (pages.md):* A kategórialeírás, a 6 saját termék és az egyedi műszerdoboz-szolgáltatás.

Általunk készített, tervezett vagy gyártott termékeket találhatsz itt. Fő terméktervezőnk és készítőnk: **Bán Péter**.

#### Termékeink

- [Rácsos Műszerdoboz DC 400W 15A Step-up Boost-hoz + 8 csavar](/products/racsos-muszerdoboz-dc-400w-15a-step-up-boost-hoz-8-csavar)
- [Műszerdoboz 100*60*22 kapcsolós, fekete, projekt doboz](/products/muszerdoboz-1006022-kapcsolos-fekete-projekt-doboz)
- [Műszerdoboz 100*60*42 kapcsolós, fekete, projekt doboz](/products/muszerdoboz-1006042-kapcsolos-fekete-projekt-doboz)
- [Szív alakú RGB LED lámpa D.I.Y. készlet](/products/sziv-alaku-rgb-led-lampa-diy-keszlet)
- [AI robot KIT](/products/ai-robot-kit)
- [TankBot 1.0 DIY készlet /esp32 alapú](/products/tankbot-10-diy-keszlet-esp32-alapu)

[Az összes saját termék megtekintése](/collections/sajat-termekeink)

#### Egyedi műszerdobozra van szükséged? Mi megvalósítjuk az ötleted!

Biztosan veled is előfordult már, hogy az elektronikai áramköröd vagy saját fejlesztésű eszközöd már tökéletesen működött, de nem találtál hozzá olyan gyári dobozt, amelybe pontosan beleillett volna. Ezért elindítottuk az **egyedi, 3D nyomtatott műszerdobozok készítését**, így pontosan olyan burkolatot kaphatsz, amilyenre a munkádhoz vagy a hobbidhoz szükséged van.

##### Hogyan küldheted el az elképzelésedet?

- **Kész digitális terv:** ha már megtervezted a burkolatot, küldd el nekünk az **STL-fájlt**, és azonnal indítjuk a gyártást.
- **Papíralapú vázlat:** rajzold le az ötletedet egy tiszta lapra, és add meg a pontos méreteket (hosszúság, szélesség, magasság, a furatok és kivágások helye). A rajzod alapján elkészítjük a digitális modellt.

##### Mit tartalmaz az ár?

Az egyedi árajánlat **2000 Ft-tól** indul, a szállítási költségen felül. Az összeg a következőkből áll:

1. **Tervezési órabér:** csak akkor számoljuk fel, ha a dobozt nekünk kell megrajzolnunk a papíralapú vázlatod alapján. Ha kész fájlt küldesz, ez a költség nulla.
2. **Anyagköltség:** a doboz gyártásához ténylegesen felhasznált műanyag alapanyag ára.
3. **Nyomtatási idő költsége:** a 3D nyomtató működési ideje, amely a doboz méretétől, falvastagságától és bonyolultságától függ.

##### Alkatrészek beépítése

Kérésre a gyártás során a szükséges kiegészítőket is beépítjük: kisebb **kapcsolókat, csatlakozókat, visszajelző fényeket** vagy rögzítőcsavarokat. Így a csomag megérkezése után már csak a saját áramkörödet kell a helyére tenned.

##### Hogyan rendelhetsz?

Írj egy levelet az [info@modulshop.hu](mailto:info@modulshop.hu) e-mail-címre. Csatold a rajzodat vagy a kész fájlt, és írd le a különleges kéréseidet!

**Fontos:** a levelek gyorsabb feldolgozása érdekében kérjük, hogy az e-mail tárgya pontosan ez legyen: **Műszerdoboz**

### Mesterséges intelligencia (AI) használati szabályzat

Handle: `ai-hasznalati-szabalyzat` · Sablon: `page.legal` (utótag: `legal`)

*Állapot / megjegyzés (pages.md):* Plusz oldal: a régi láblécben és a sitemapben is szerepel. Szó szerinti szöveg.

#### Modulshop.hu webáruház

**Hatálybalépés:** 2026. augusztus 1.

*A teljes szöveg (12523 karakter): `docs/import/pages/ai-hasznalati-szabalyzat.html` (a fájl eleji `<!-- … -->` megjegyzés nélkül illeszd be).*

## 5. Menük és nyitott kérdések

Forrás: `docs/import/menus.md`. Csak azok a menüpontok szerepelnek, amelyek célja e csomag után létezik (a fenti kollekciók és oldalak, illetve a Shopify beépített oldalai: `/collections/all`, `/account`). A menünév barátságosabb lehet a címkénél; a link a kollekcióra mutat.

### Főmenü (`main-menu`) – mega-menü, 3 szint

- Termékek → `/collections/all`
  - Mikrovezérlők, alaplapok → `/collections/mikrovezerlok-alaplapok`
    - Arduino → `/collections/arduino`
    - ESP32 → `/collections/esp32`
  - Szenzor Modulok → `/collections/szenzor-modulok`
    - Hőmérséklet, pára, nyomás → `/collections/homerseklet-para-nyomas`
  - Egyéb Modulok → `/collections/egyeb-modulok`
    - Relék, optocsatolók → `/collections/relek-optocsatolok`
  - Erősítők, Végfokok → `/collections/erositok-vegfokok`
    - 2×50W erősítő, végfok → `/collections/2x50w-erositok-vegfokok`
  - LCD-k, Kijelzők → `/collections/lcd-k-kijelzok`
  - BMS-ek, 18650 Akkuk → `/collections/bms-ek-18650-akkuk`
  - DC, AC konverterek → `/collections/dc-ac-konverterek`
  - Műszerek → `/collections/muszerek`
  - Egyéb → `/collections/egyeb`
    - Szerszámok → `/collections/szerszamok`
  - Elektronika → `/collections/elektronika`
    - Kapcsolók, csatlakozók, vezetékek → `/collections/kapcsolok-csatlakozok-vezetekek`
  - D.I.Y. Készletek → `/collections/diy-keszletek`
  - Led világítás → `/collections/led-vilagitas`
- Saját termékeink → `/collections/sajat-termekeink`
- Csomagok → `/collections/csomagok`
- Iskoláknak és cégeknek → `/pages/iskolaknak-es-cegeknek` *(TERVEZET: amíg nincs jóváhagyva, a menüpont se kerüljön ki)*
- Kapcsolat → `/pages/kapcsolat`

Kimaradt a főmenüből (a cél még nem létezik): a többi 32 alkollekció a `menus.md` szerint, és a Blog (`/blogs/news`), mert a blogcikkek tartalma nincs a csomagban. Ha ezek elkészülnek, a `menus.md` teljes fája szerint bővíthető.

### Lábléc: `vasarlas` – „Vásárlás”

- Szállítás és fizetés → `/pages/szallitas-es-fizetes`
- Garancia és visszaküldés → `/pages/garancia-es-visszakuldes`
- Hűségpont rendszer → `/pages/husegpont` *(csak akkor kerüljön ki, ha a hűségpont-alkalmazás már működik)*
- Iskoláknak és cégeknek → `/pages/iskolaknak-es-cegeknek` *(TERVEZET: jóváhagyásig ne kerüljön ki)*
- Regisztráció / Fiókom → `/account`
- Összes termék → `/collections/all`

### Lábléc: `informaciok` – „Információk”

- Rólunk → `/pages/rolunk` *(TERVEZET: jóváhagyásig ne kerüljön ki)*
- Saját termékeink → `/pages/sajat-termekeink`
- Gyakran ismételt kérdések → `/pages/gyik`
- Kapcsolat → `/pages/kapcsolat`

(A `menus.md` szerinti „Blog → `/blogs/news`” pont kimaradt, amíg a blogcikkek nincsenek átvive.)

### Lábléc: `jogi` – „Jogi információk”

- ÁSZF → `/pages/aszf`
- Adatvédelmi nyilatkozat → `/pages/adatvedelem`
- Elállás → `/pages/elallas`
- Impresszum → `/pages/impresszum`
- AI használati szabályzat → `/pages/ai-hasznalati-szabalyzat`

(A „Visszatérítési szabályzat (Shopify) → `/policies/refund-policy`” pont csak akkor kerüljön be, ha a *Beállítások → Szabályzatok* alatt kitöltötték.)

### Nyitott kérdések a tulajdonosnak

Forrás: `docs/import/README.md`, „Nyitott kérdések a tulajdonosnak”. Ezekben a Shopify AI ne döntsön; a jelölt helyeken hagyja meg a `[[…]]` jelölést.

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
