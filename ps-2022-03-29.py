casy = [11.23, 12.31, 11.18, 13.98, 15.48, 10.95, 12.39]

# Za kolik sekund uběhl vzdálenost vítěz závodu?
print(min(casy))

# Vytvoř seznam, který bude pro každého závodníka udávat, o kolik byl pomalejší než držitel světového rekordu Usain Bolt, který 100 metrů uběhl za 9.58 sekund.
bolt = [round(cas - 9.58, 2) for cas in casy]

# Vytvoř seznam, který bude pro každého závodníka udávat, o kolik byl pomalejší než vítěz závodu.
ztrata_na_viteze = [round(cas - min(casy), 2) for cas in casy]

rodna_cisla = ["6805218280", "7058284849", "7411242432", "6908037642", "6604232404", "7904017748", "9154056219", "9462207975"]

# Vytvoř seznam, který bude obsahovat roky narození pacientů (jako celá čísla).
roky = [f'19{int(cislo[:2])}' for cislo in rodna_cisla]

# Vytvoř seznam, který bude obsahovat měsíce narození (jako celá čísla).
# Alternativně je možné použít celočíselné dělení
mesic_naroz = [cislo[2].replace("5","0") + cislo[3] for cislo in rodna_cisla]
mesic_naroz = [cislo[0].replace("6","1") + cislo[1] for cislo in mesic_naroz]

# Vytvoř dvourozměrný seznam, kde vnitřní seznamy budou obsahovat rok, měsíc a den narození jednotlivých pacientů.
rok_mesic_den = [[int(cislo[:2])+1900, int(cislo[2:4]) %50, int(cislo[4:6])] for cislo in rodna_cisla]
# [[1968, 5, 21], [1970, 8, 28]]


"""
Příklad vytvoření datetime - hodnoty, která skutečně je datum, nikoli trojice čísel.
Je to spíše ukázka, k čemu ta operace je.
Více o datetime je zde: https://kodim.cz/czechitas/progr2-python/python-pro-data-1/datum
"""
pacient_1 = rok_mesic_den[0]
import datetime
datum_narozeni = datetime.datetime(pacient_1[0], pacient_1[1], pacient_1[2])
stari = datetime.datetime.today() - datum_narozeni

# Vytvoř seznam, který bude obsahovat pouze ženy. Kolik procent pacientů ordinace tvoří ženy?
zeny = [cislo for cislo in rodna_cisla if int(cislo[2:4]) > 50]

# Úkol navíc - přidání popisku s pohlavím ke každému rodnému číslu
cisla = [[cislo, "žena" * (int(cislo[2]) > 1) + "muž" * (int(cislo[2]) <= 1)] for cislo in rodna_cisla]


zavody = [[10.39, 11.23], [13.86, 12.31], [11.94, 11.18], [14.35, 13.98], [12.64, 15.48], [11.24, 10.95], [13.37, 12.39]]

# Vytvoř seznam, ve kterém bude vidět změna v čase závodníka (změna může být kladná i záporná).
zmeny = [round(zavod[1]-zavod[0], 2) for zavod in zavody]

# O kolik se v průměru změnil čas závodníka?
import statistics
print(statistics.mean(zmeny))

"""
Vypočti medián dat. Dokážeš podle něj říct, jestli se zvětšina závodníků zlepšíla nebo zhoršila?
Medián je záporný, takže se většina závodníků zlepšila.
"""
print(statistics.median(zmeny))

# Vytvoř seznam, kde budou rozdíly časů pouze těch závodníků, kteří se zlepšili. Kolik jich bylo?
# Dva různé způsoby řešení
zlepseni = [cas for cas in zmeny if cas < 0]
print(len(zlepseni))
zlepseni = [cas[1]-cas[0] for cas in zavody if cas[1]-cas[0]<0]
print(len(zlepseni))

"""
Dostala jsi následující seznam, kde jsou vzdálenosti mezi nápravami přípojných vozidel nákladních automobilů.

* Vytvoř dvourozměrný seznam, kde budou jednotlivé vzdálenosti jako samostatné prvky seznamu.
* Spočti průměrný počet náprav v našem vzorku.
"""

napravy = ["1323;1341", "3459;1023;1094", "1241;1231;1247", "3421,983,956,954", "3981"]
napravy = [vozidlo.replace(",", ";") for vozidlo in napravy]
napravy = [vozidlo.split(";") for vozidlo in napravy]
pocty = [len(vozidlo) + 1 for vozidlo in napravy]
print(f"Průměrný počet náprav je {statistics.mean(pocty)}.")
# Kdybychom chtěli vzdálenosti jako čísla
napravy = [[int(naprava) for naprava in auto] for auto in napravy]
