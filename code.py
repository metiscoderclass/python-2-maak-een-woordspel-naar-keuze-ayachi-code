import hangmat
import time
from random import *




#belangenrijke variables

woorden = ["bilal ", "test ", "janhendrik ", "pythoniscool "]

counter = 0
gebruikte_letters = ""
goed = ""




def woordtoevoegen():
    global woorden
    hallo=input("type een woord ")
    woorden.append(hallo)
    with open('woorden', 'w') as f:
        for count in range(0,len(woorden)):
            print(woorden[count])
            f.write(woorden[count] + "\n")


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


def laat_zien():
    global woorden
    for count in range(0,len(woorden)):
        print(woorden[count])


def welkom():
    print("Welkom bij: ")
    print("/ __)  /__\  (  )  / __) (_  _)( ___)")
    print("( (_-. /(__)\  )(__( (_-..-_)(   )__) ")
    print("\___/(__)(__)(____)\___/\____) (____)  ")
    
    
    
welkom()

def galgje():
    while True:
        
        #varibales global maken
        global woord
        global counter
        global gebruikte_letters
        global goed
        
        print("als je het woord hebt druk dan op ? teken ")
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




begin = input("type 1 voor galgje type 2 voor beheren typen 3 als je wilt afsluiten ")


if begin == "1":
    galgje()




class qwer:
    def beheren(self):
        global kies
        kies=input("welkom bij beheren type 1 om een woord toe tevoegen en 2 om alle woorden te bekijken en 3 om galgje te spelen ")
        if kies == "1":
            woordtoevoegen()
        elif kies == "2":
            laat_zien()
        return kies
        


classbeheren=qwer()
beheren=classbeheren.beheren()



while begin=="2":
    if beheren == "1":
        laso=input("druk op 1 om een woord toetevoegen, en 2 naar beheren en 3 om galgje te spelen ")
        if laso == "1":
            woordtoevoegen()
        elif laso == "2":
            classbeheren.beheren()
        elif laso == "3":
            with open('woorden', 'w') as f:
                random_index = randrange(0,len(woorden))
                woord=woorden[random_index]
            galgje()
    elif beheren == "2":
        ctes=input("Type 1 om alle woorden te zien,2 naar beheren,3 naar galgje ")
        if ctes == "1":
            for count in range(0,len(woorden)):
                print(woorden[count])
        elif ctes == "2":
            classbeheren.beheren()
        elif laso == "3":
            galgje()
    
        
        
            
            
            
            
        

        


   
    
 
    
    
    
        
    
    
    
    