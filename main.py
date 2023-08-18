# BACKGROUND TASKS #

# TODO Mechanizm losowania słówka
# TODO Odgadywanie tłumaczenia polskiego
# TODO Ogdadywanie tłumaczenia angielskieg (z podpowiedzią pierwszej litery)
# TODO Zapisywanie postępów do pliku Excela NA BIEŻĄCO !
# TODO Omijanie słówek bez tłumaczenia

# INTERFEJS GRAFICZNY #

# TODO Wybór trybu pracy
#	- wybór polskiego słówka i napisanie odpowiadającyh mu tłumaczeń
# 	- wybór angielskiego słówka i napisanie odpowiadających mu tłumaczń
#	- wypisywanie słówek które zaczynają się na daną literę
#	- powyższe opcje z możliwością wyboru typu części mowy
# TODO Wyświetlanie słówka które próbujemy odgadnąć
# TODO Wyświetlanie słówka które my podajemy jako odpowiedź
# TODO Weryfikacja naszej odpowiedzi w trybie natychmiastowym (możliwe do zmiany w ustawieniach)

# DODATKOWE - 'JAK STARCZY CZASU' #

# Możliwość zmiany ustawień z poziou okienka ustawień
# 	- wybór szaty graficznej
# Dodanie możliwości wczytywania danych w sposób autmoatyczny dla urzytkownika
# Przeglądanie naszej bazy słówek

import PySimpleGUI as sg
from openpyxl import load_workbook

def pick_word(): ...

def get_display_resolution() -> tuple:
	"""
	This function is responsible to get current resolution of the screen
	It is run on the beginning to determine how big the window should be
	given how many percentage of width and heigh window should be
	"""
	# Stolen from:
	# https://github.com/rr-/screeninfo/blob/master/screeninfo/enumerators/osx.py
	from AppKit import NSScreen

	screens = NSScreen.screens()
	f = screens[0].frame
	if callable(f):
		f = f()
		return int(f.size.width),int(f.size.height)

def get_window_size(width_percent : float, heigh_percent : float) -> tuple:
	width, height = get_display_resolution()
	mul_width = int(width * width_prop)
	mul_height = int(height * height_prop)
	return mul_width, mul_height

width_prop = height_prop = 0.5
window_size = get_window_size(width_prop, width_prop)

wkbk = load_workbook("slowka_angielski_C1.xlsm")
sheet = wkbk.get_sheet_by_name("100k")
#dostęp do zmiennej o tej pozycji
#sheet["A10"].value

sg.theme('DarkAmber')
cz_nagl_ramka = "_ 14"
kolor_tla_popup = "black"
layout = [
	[sg.Text("Oto podstawowy tekst który piszę by sprawdzić działanie mojego"+\
	  "kodu tak by można było zobaczyć ramy mojego pola tekstowego",size=(40,3))]
]

window = sg.Window('Porównanie algorytmów Merge Sort i Quick Sort', layout, size=window_size)

while True:
	ponow_sortowanie = False
	event, values = window.read()	# odczyt interakcji

	# obsługa zdarzeń
	if event == sg.WIN_CLOSED or event=="exit":		# zakończenia działania
		break
	
window.close()
exit()