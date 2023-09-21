wejscie = open("notepad.txt")
wyjscie = open("output.txt","w")

for rekord in wejscie:
    pocz = rekord.find("(")
    wyjscie.write(rekord.strip()[pocz+1:-1]+"\n")

wejscie.close()
wyjscie.close()