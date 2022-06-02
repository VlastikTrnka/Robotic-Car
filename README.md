# RoboCar project P1A 2021

Robotické auto by mělo zvládat "semi-autonomní" řízení. Po *bílé* nebo *černé* čáře se bude pohybovat převážně samostatně, ideálně bez nutnosti zásahů do řízení.

Je vhodné si pomoci zasíláním "instrukcí" prostřednictvím aplikace [**Mbit**](https://play.google.com/store/apps/details?id=com.yahboom.mbit&hl=cs&gl=US) z Google Play nebo App Store.

- Pro splnění algoritmické úlohy nesmí vozidlo opustit svým obrysem vytyčenou čáru. 
- Druhým faktorem hodnocení je čas potřebný na úspěšné zdolání tratě. 
- Počet nutných korekcí (manuálních zásahů do řízení) také ovlivní výsledek.
- Čitelnost a dekompozice kódu **je** předmětem hodnocení

## Požadavky na schopnosti vozidla

- [x] autonomní jízda po bílé / černé čáře bez nutných zásahů do řízení
- [ ] překonání křižovatek ve tvaru písmene **+**
- [ ] schopnost na "vyžádání" odbočit na křižovatce vlevo nebo vpravo
- [ ] možnost obrátit se do protisměru

### Volitelně (bonusové hodnocení)

- [ ] schopnost najet do křižovatky jiného tvaru než **+**, typicky **Y**
- [ ] čára končící u mechanické překážky = otočení se do protisměru
- [ ] čára končící mechanickou překážkou = pokus o objetí a pokračování v autonomní jízdě
(překážka nebude nikdy větší jak 20 × 20 × 20 cm)

## Omezení v hodnocení práce
Algoritmicky totožná řešení napříč skupinami budou snižovat procento maximálního hodnocení. A to o 10 % za každý duplicitní výskyt.
Například pokud u 3 vozidel bude signifikantní část funkcionality totožná, odečítá se 30 % (z maxima) od celkového hodnocení.

#### Metadata (used for search, rendering)

* for PXT/microbit
<script src="https://makecode.com/gh-pages-embed.js"></script><script>makeCodeRender("{{ site.makecode.home_url }}", "{{ site.github.owner_name }}/{{ site.github.repository_name }}");</script>


> Otevřít tuto stránku v aplikaci [https://vlastiktrnka.github.io/robotic-car/](https://vlastiktrnka.github.io/robotic-car/)

## Použít jako rozšíření

Toto úložiště lze přidat jako **rozšíření** v aplikaci MakeCode.

* otevřít [https://makecode.microbit.org/](https://makecode.microbit.org/)
* klikněte na možnost **Nový projekt**
* klikněte na možnost **Rozšíření** v nabídce s ozubeným kolem
* vyhledat **https://github.com/vlastiktrnka/robotic-car** a importovat

## Upravit tento projekt ![Odznak stavu sestavení](https://github.com/vlastiktrnka/robotic-car/workflows/MakeCode/badge.svg)

Slouží k úpravě tohoto úložiště v aplikaci MakeCode.

* otevřít [https://makecode.microbit.org/](https://makecode.microbit.org/)
* klikněte na možnost **Import** a poté na **Import adresy URL**
* vložte **https://github.com/vlastiktrnka/robotic-car** a klikněte na možnost import

## Náhled bloků

Tento obrázek znázorňuje kód z Bloků od posledního potvrzení v hlavní verzi.
Tento obrázek se může aktualizovat až za několik minut.

![Vykreslený náhled bloků](https://github.com/vlastiktrnka/robotic-car/raw/master/.github/makecode/blocks.png)

#### Metadata (slouží k vyhledávání, vykreslování)

* for PXT/microbit
<script src="https://makecode.com/gh-pages-embed.js"></script><script>makeCodeRender("{{ site.makecode.home_url }}", "{{ site.github.owner_name }}/{{ site.github.repository_name }}");</script>
