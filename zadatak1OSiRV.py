import random


def pogodiBroj():
    print "Zamislio sam broj izmedu 0 i 15. Pogodi ga!"
    x=random.randint(0,15)
    brojPokusaja = 0

    tocan = False

    while not tocan:
        y = raw_input("Ja kazem... ")

        if int(y) == x:
            brojPokusaja = brojPokusaja + 1
            tocan = True
            if brojPokusaja > 5:
                print "Kako si mogao pogoditi u " + str(brojPokusaja) + " pokusaja???... Luzeru"
            elif brojPokusaja == 5:
                print "Prosjecno, u " + str(brojPokusaja) + " pokusaja."
            elif brojPokusaja < 5:
                print "Bravo! To je bilo u " + str(brojPokusaja) + " pokusaja."

        elif int(y) > x:
            brojPokusaja = brojPokusaja + 1
            print "Ti kazes previse"
        elif int(y) < x:
            brojPokusaja = brojPokusaja + 1
            print "Ti kazes premalo"
        else:
            print "Jesi pijan?"
#pogodiBroj()

    
