"""Unos ulice, 7 do 15 znakova, unos imena do rijeci "prekid",
nakon toga ispis svih ulica i onu koja ima najduze ime"""

def stupidStreets():
    correctLength = False
    lista = []
    najveci = 0

    while not correctLength:
        ulica = raw_input("Unesi ime ulice")
        if ulica == "prekid":
            correctLength = True
        else:
            if len(ulica) <= 15 and len(ulica) >= 7:
                print ulica + " broj:" + str(len(ulica))
                lista.append(ulica)
            else:
                print "premalo slova: " + str(len(ulica))

    print lista

    print "Uneseno je " + str(len(lista)) + " ulica."
    for i in range(len(lista)):
        if len(lista[i]) > najveci:
            najveci = len(lista[i])
            ime = lista[i]

    print "Najduze ime ima "+ ime +" ulica"
    

#stupidStreets()
    
    
