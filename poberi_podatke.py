# Knjiznica za delo z regularnimi izrazi v Pythonu
import re

# Uvozimo knjižnico json
import json

# Strani bomo zajeli s pomočjo knjižnice requsts
import requests

# Uvozimo knjiznico za delo z datotekami oblike csv.
import csv



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

       

#count = 0

#def ime_datoteke(st_strani):
#    return f"stanovanja-{st_strani}.html"

#for st_strani in range(3):
#    url = (
#        'https://www.nepremicnine.net/oglasi-prodaja/'
#        f'ljubljana-mesto/stanovanje/{st_strani + 1}/'
#        '?s=13'
#        )
#    print(f"Zajemam {url}")
#    response = requests.get(url)
#    vsebina = response.text
#    with open(ime_datoteke(st_strani), 'w', encoding='utf-8') as dat:
#        dat.write(vsebina)

count = 0

def ime_datoteke(regija, st_strani):
    return f"stanovanja-{regija}-{st_strani}.html"

regije =[
    "ljubljana-mesto",
    "ljubljana-okolica",
    "gorenjska",
    "juzna-primorska",
    "severna-primorska",
    "notranjska",
    "savinjska",
    "podravska",
    "koroska",
    "dolenjska",
    "posavska",
    "zasavska",    
    "pomurska"
    ]

#for regija in regije:
#    for st_strani in range(3):
#        url = (
#            'https://www.nepremicnine.net/oglasi-prodaja/'
#            f'{regija}/stanovanje/{st_strani + 1}/'
#            '?s=13'
#            )
#        print(f"Zajemam {url}")
#        response = requests.get(url)
#        vsebina = response.text
#        with open(ime_datoteke(regija, st_strani), 'w', encoding='utf-8') as dat:
#            dat.write(vsebina)


# Na neki točki smo samo izpisovali na zaslon.
# Na neki točki smo samo izpisovali na zaslon.
# Za nadaljnje delo je bolje, če podatke spravimo v obliko json.
#for st_strani in range(3):
#    with open(ime_datoteke(st_strani), encoding='utf-8') as dat:
#        vsebina = dat.read()
#    for zadetek in vzorec.finditer(vsebina):
#       print(zadetek.groupdict())
#       count += 1

#print(count)

stanovanja =[]
for regija in regije:
    for st_strani in range(3):
        with open(ime_datoteke(regija, st_strani), encoding='utf-8') as dat:
            vsebina = dat.read()
        for zadetek in vzorec.finditer(vsebina):
            stanovanja.append(zadetek.groupdict())
       
with open("stanovanja.json", "w", encoding="utf-8") as dat:
    json.dump(stanovanja, dat, indent=4, ensure_ascii=False)

# indent=4...lepo oblikovano
# enscure_ascii=False...unicode

# Za analizo je priročno, če imamo podatke v tabelarični obliki. Zato bomo uporabljali csv(comma seperated values)

#with open("stanovanja.csv", "w", encoding= "utf-8") as dat:
#    writer = csv.DictWriter(dat, [
#        "Lokacija",
#        "Leto_gradnje",
#        "Stevilo_sob"
#    ])
#    for stanovanje in stanovanja:
#        writer.writerow(stanovanje)