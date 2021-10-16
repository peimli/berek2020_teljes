f = open("berek2020.txt", "r", encoding = "UTF-8")
lista = []
for sor in f:
    lista.append(sor.strip().split(";"))
lista.remove(lista[0])
f.close()
#3.feladat: Dolgozók száma:
print(f"3.feladat: Dolgozók száma: {len(lista)} fő")
#4.feladat:bérek átlaga:
p2v = lambda x: x.replace(".", ",")
berek = []
for sor in lista:
    berek.append(int(sor[-1]))
atlag = f"A bérek átlaga: {sum(berek) / len(lista) / 1000:.1f}"
print(f"4.feladat: {p2v(atlag)}")
#5.feladat:
reszleg = input("5.feladat: Kérem egy részleg nevét: ")
#6.feladat:
nincs = "A megadott részleg nem létezik a cégnél"
for sor in lista:
    if reszleg in sor:
        xxx = max( [ (int(sor[-1]),sor )for sor in lista if reszleg in sor])
        print(f"6.feladat: A legtöbbet kereső dolgozó a megadott részlegen:")
        print(f"    Név:{xxx[1][0]}")
        print(f"    Neme:{xxx[1][1]}")
        print(f"    Belépés:{xxx[1][3]}")
        print(f"    bér:{xxx[0]} Forint")
        if True:
            break
else:
    print(f"6.feladat: {nincs}")
#7.feladat:
statisztika = dict()
for sor in lista:
    reszleg = sor[2]
    statisztika[reszleg] = statisztika.get(reszleg, 0) + 1
print(f"7.feladat: Statisztika:")
for sor in statisztika.items():
    print(f"        {sor[0]} - {sor[1]}")