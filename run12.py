import zadatak1OSiRV
import zadatak2OSiRV

def pokreni():
    print "Odaberi <1> za prvi zadatak"
    print "Odaberi <2> za drugi zadatak"
    x = raw_input()
    if int(x) == 1:
        print "Pokrecem "+x+"."
        zadatak1OSiRV.pogodiBroj()
    elif int(x) == 2:
        print "Pokrecem "+x+"."
        zadatak2OSiRV.stupidStreets()

pokreni()
