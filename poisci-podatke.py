# Knjiznica za delo z regularnimi izrazi v Pythonu
import re

# Odpremo html datoteko z vsebino, po kateri bomo iskali določene vzorce, ki nas zanimajo
with open('stanovanja-zasavska-1.html') as f:
    vsebina = f.read()

# Surovi nizi: r'', nočemo ubeznih znakov.
# Compile: vzame niz in vrne objekt, ki predstavlja vzorec in bomo ta objekt v nadaljevanju uporabili in lahko pokličemo metodo finditer
# Drugače bi vsakič znova pretvarjalo v objekt
vzorec = re.compile(
    r'<span class="title">'
    r'(?P<Lokacija>.+?)'
    r'</span></a></h2>\s*' # Lokacija stanovanja
    r'<a class="slika" href="/oglasi-prodaja/.*\d*/"><img class="lazyload" data-src=("https://img.nepremicnine.link/sIonep_oglasi2/\d*.jpg"|"/images/n-1.jpg") ' # Dodala |, ker ima stanovanje na tretji strani napisano drugače
    r'itemprop="image" /><a class="ikona-sh3 utility save-ad" id="msave-ad-\d*" href="#" data-id="\d*" onclick="save_ad\(\d*\); return false;"><i class="fa fa-heart-o"></i></a><div class="vec"></div></a>\s*'
    r'<meta itemprop="businessFunction" content="sell" />\s*'
    r'<div class="teksti_container" data-href="/oglasi-prodaja/.*\d*/">\s*'
    r'<span class="posr">Prodaja: <span class="vrsta">Stanovanje</span>(<span class="new-label">novo</span>)?'
    r'<span class="tipi">(?P<Stevilo_sob>\d*).*</span></span>\s*' # Število sob
    r'<!--<div class="new-container">\s*'
    r'(<div class="new sl"><i class="fa fa-certificate"></i><span>novo</span></div>)?\s*'
    r'</div>-->\s*'
    r'<div class="atributi" itemprop="disambiguatingDescription">\s*'
    r'.*<span class="invisible">, ' # Nekatera imajo tu napisana nadstropje v katerem je stanovanje zato .*. V nadaljevanju zajemi tudi nadstropje.
    r'</span></span><span class="atribut leto">Leto: <strong>(?P<Leto_gradnje>\d*)</strong></span><span class="invisible">, '
    r'(</span><span class="atribut">Zemljišče: <strong>4433 m2</strong></span>)?\s*' # Samo prvo ima podano zemljišče
    r'(<!--<div class="new sl"><i class="fa fa-certificate"></i><span>novo</span></div>-->)?')


       



# findall:vse pojavitve določenega izraza. Vrne vse nize, ki ustrezajo vzorce. Sprejme vzorec in niz v katerem naj išče.
# search: Isto sprejme niz in vzorec. Vsak zadetek je objekt.
# groupdict: slovar vseh poimenovanih skupin
# finditer: iterator čez vse zadetke

#stevec = 0
for i, zadetek in enumerate(vzorec.finditer(vsebina), 1):

    print(i, zadetek.groupdict())
    #stevec += 1
#print(stevec)



#Pomurska: Na prvi strani eno stanovanje premalo