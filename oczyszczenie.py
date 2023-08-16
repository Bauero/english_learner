#https://medium.com/analytics-vidhya/how-to-translate-text-with-python-9d203139dcf5
from deep_translator import GoogleTranslator

# przeliczanie kolumny (liczba) na excela
def colToLetter(kolumn: int) -> str:

    # program operuje na wartosciach liczonych od 1
    if kolumn <= 0:
        return None

    litery = []
    while kolumn % 26 > 0:
        reszta = kolumn % 26
        litery.insert(0,chr(reszta + 64))
        kolumn //= 26
    return "".join(litery)

# przeliczanie litery (kol. excela) na liczbe
def letterToCol(letter: str) -> int:
    if not letter.isalpha():
        return None
    wynik = 0
    potega = 0
    for l in range(len(letter)-1,-1,-1):
        wynik += 26**potega * (ord(letter[l]) - 64)
        potega += 1
    return wynik

# zmiana rzedu i kolumny z liczb na zapis excela
def toExclNot(kol: int, rzad: int):
    return colToLetter(kol) + str(rzad)

f = open("100k_english_words.txt","r")
g = open("100k_english_words_clean.txt","w")

# for _ in range(1000):
#     l = f.readline()
#     if not "#" in l:
#         to_translate = l.strip()
#         translated = GoogleTranslator(source='en', target='pl').translate(to_translate).lower()
#         g.write(f"{to_translate}\t{translated}\n")
kontynuuj = True
while kontynuuj:
    lista = []
    for __ in range(500):
        try:
            line = f.readline()
        except EOFError:
            kontynuuj = False
            break
        if not "#" in line:
            lista.append(line.strip())
    to_translate = "\n".join(lista)
    translated = GoogleTranslator(source='en', target='pl').translate(to_translate).lower()
    przetl = translated.strip().split("\n")
    for i in range(len(lista)):
        g.write(f"{lista[i]}\t{przetl[i]}\n")

g.close()
f.close()
exit()