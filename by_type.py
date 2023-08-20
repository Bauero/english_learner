from openpyxl import load_workbook
from excel_functions import colToLetter

workbook = load_workbook("slowka_angielski_C1.xlsm")

sheet_by_type = workbook.get_sheet_by_name("by_type")
sheet_100k = workbook.get_sheet_by_name("100k")
plik = open("plik.txt","w")

kolumn_type = {"nieprzydzielone" : "A" , "czasownik" : "B"}

kat_slowoPowt = {"czasownik" : [], "nieprzydzielone" : []}

kat_slow = ["czasownik"]

for nr_wiersza in range(2,102):
    slowkoA = sheet_100k[f"A{nr_wiersza}"].value
    typ = sheet_100k[f"B{nr_wiersza}"].value
    slowkoP = sheet_100k[f"D{nr_wiersza}"].value
    powtorzenia = sheet_100k[f"E{nr_wiersza}"].value

    if typ.strip() == "":
        kat_slowoPowt["nieprzydzielone"].append((slowkoA, powtorzenia))
        continue

    elif typ not in kat_slow:
        kat_slowoPowt[typ] = []
        kat_slow.append(typ)
        kolumn_type[typ] = colToLetter(len(kolumn_type.keys())+1)

    kat_slowoPowt[typ].append((slowkoA, powtorzenia))

# SORTOWANIE I WPISYWANIE#

wiersze = [""]

for kat in kat_slowoPowt:
    kat_slowoPowt[kat] = sorted(kat_slowoPowt[kat], key=lambda x: x[1], reverse=True)
    kolumna = kolumn_type[kat]
    sheet_by_type[kolumna+"1"] = kat
    wiersze[0] += kat + "\t"
    for wiersz in range(len(kat_slowoPowt[kat])):
        sheet_by_type[kolumna+str(wiersz+2)] = kat_slowoPowt[kat][wiersz][0]
        if wiersz > len(wiersze)-1:
            wiersze.append("")
        wiersze[wiersz] += kat_slowoPowt[kat][wiersz][0] + "\t"

for l in wiersze:
    plik.write(l+"\n")
plik.close()
workbook.close()
