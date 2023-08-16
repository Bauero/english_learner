import PySimpleGUI as sg
from openpyxl import load_workbook

# Legaly stolen from:
# https://github.com/rr-/screeninfo/blob/master/screeninfo/enumerators/osx.py

from AppKit import NSScreen

screens = NSScreen.screens()
f = screens[0].frame
if callable(f):
    f = f()
    width=int(f.size.width)
    height=int(f.size.height)

width_prop = height_prop = 0.5
mul_width = int(width * width_prop)
mul_height = int(height * height_prop)
rozmiary_okna = (mul_width,mul_height)



wkbk = load_workbook("slowka_angielski_C1.xlsm")
sheet = wkbk.get_sheet_by_name("100k")
#dostęp do zmiennej o tej pozycji
#sheet["A10"].value

"""
Do zaprogramowania:
- wylosowanie konkretnego słówka (powinno ono losować przede wszyskim takie które nie 
    były zbyt często losowane, i sporadycznie pokazywać te które już są oznaczone jako zapoznane)
    - możliwość wylosowania słówka, które jest po angielsku i które ma podaną pierwszą literę
        ale nie jest w całości widoczne
	- możliwość wylosowania słówka po polsku do przetłumaczenia na angielski (w całości)
- losowanie powinno uwzględniać ilość pokayzwanych słówek - tak by słówka które juz sie pojawiały
    nie były co chwila wyświetlane
- Możliwość sprawdzenia jakie słówka były pokazywane podczas ostatniej sesji nauki
- Zapisywanie postępów do naszego pliku
"""

sg.theme('DarkAmber')
cz_nagl_ramka = "_ 14"
kolor_tla_popup = "black"
layout = [
	[sg.Text("Oto podstawowy tekst który piszę by sprawdzić działanie mojego"+\
	  "kodu tak by można było zobaczyć ramy mojego pola tekstowego",size=(40,3))]
]

window = sg.Window('Porównanie algorytmów Merge Sort i Quick Sort', layout, size=rozmiary_okna)

while True:
	ponow_sortowanie = False
	event, values = window.read()	# odczyt interakcji

	# obsługa zdarzeń
	if event == sg.WIN_CLOSED or event=="exit":		# zakończenia działania
		break
	
window.close()
exit()