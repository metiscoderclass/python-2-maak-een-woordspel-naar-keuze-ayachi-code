import hangmat
import time



def check():
    if counter == 1:
        hangmat.een()
    elif counter == 2:
        hangmat.twee()
    elif counter == 3:
        hangmat.drie()
    elif counter == 4:
        hangmat.vier()
    elif counter == 5:
        hangmat.vijf()
    elif counter == 6:
        hangmat.zes()




woord = "bilal"
counter = 0
gebruikte_letters = ""
goed = ""


while True:
    letter = input("type een letter ")
    lengte = len(letter)
    print("deze letters heb je gebruikt: " + gebruikte_letters)
    if lengte >= 2:
        print("Oeps het letter is lang")
    elif counter == 6:
        print("Oooh je manetje is om het leven de woord was bilal : )))")
        break
    elif letter == "?":
         raad = input("probeer het woord te raden dan: ")
         if raad == woord:
            print("je hebt het woord geraden")
            break
         else:
             print("fout je hebt het woord niet geraden")
             counter += 1
             check()
    elif letter in woord:
        gebruikte_letters = gebruikte_letters + "," + letter
        print("goed zo de " + letter + " zit in het woord")
        goed += letter
        print(goed)
        if goed == woord:
            print("hoera je hebt het woord geraden")
            break
    else:
        gebruikte_letters = gebruikte_letters + "," + letter
        print("Jammer de letter " + letter + " zit niet in het woord" )
        counter += 1
        check()
