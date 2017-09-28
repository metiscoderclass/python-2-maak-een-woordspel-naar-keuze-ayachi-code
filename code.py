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



def welkom():
    print("Welkom bij: ")
    print("/ __)  /__\  (  )  / __) (_  _)( ___)")
    print("( (_-. /(__)\  )(__( (_-..-_)(   )__) ")
    print("\___/(__)(__)(____)\___/\____) (____)  ")





woord = "python"
counter = 0
gebruikte_letters = ""
goed = ""


welkom()

print("als je het woord hebt druk dan op ? teken ")

while True:
    letter = input("type een letter ")
    lengte = len(letter)
    print("deze letters heb je gebruikt: " + gebruikte_letters)
    if lengte >= 2:
        print("Oeps het letter is lang")
    elif counter == 6:
        print("Oooh je manetje is om het leven de woord was python : )))")
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
        for l in woord:
            if l in goed:
                print (l)
            else:
                print("-")
        if woord == goed:
            print("Hoera je hebt gewonnen")
            break
    else:
        gebruikte_letters = gebruikte_letters + "," + letter
        print("Jammer de letter " + letter + " zit niet in het woord" )
        counter += 1
        check()
