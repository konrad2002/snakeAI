import random

#spielfeld generieren
spielfeld = []

for i in range(10):
    spielfeld.append(random.randint(0, 1))
    

def spielfeld_ausgeben():
    print("aktuelles Spielfeld:")
    print(str(spielfeld[1])+ " " +str(spielfeld[2])+ " "+str(spielfeld[3]))
    print(str(spielfeld[4])+" "+ str(spielfeld[5])+" "+str(spielfeld[6]))
    print(str(spielfeld[7])+" "+str(spielfeld[8])+" "+str(spielfeld[9]))


def spielzug():

  schalter = int(input("Welcher Schalter soll betätigt werden? "))

  print("Schalter:  " + str(schalter))
  print("Wert:      " + str(spielfeld[schalter]))
    
  if spielfeld[schalter] == 0:
    spielfeld.pop(schalter)
    spielfeld.insert(schalter, 1)
    spielfeld.pop(schalter + 1)
    spielfeld.insert(schalter + 1, 1)
    spielfeld.pop(schalter - 1)
    spielfeld.insert(schalter - 1, 1)
    spielfeld.pop(schalter + 3)
    spielfeld.insert(schalter + 3, 1)
    spielfeld.pop(schalter - 3)
    spielfeld.insert(schalter - 3, 1)

  elif spielfeld[schalter] == 1:
    spielfeld.pop(schalter)
    spielfeld.insert(schalter, 0)
    spielfeld.pop(schalter + 1)
    spielfeld.insert(schalter + 1, 0)
    spielfeld.pop(schalter - 1)
    spielfeld.insert(schalter - 1, 0)
    spielfeld.pop(schalter + 3)
    spielfeld.insert(schalter + 3, 0)
    spielfeld.pop(schalter - 3)
    spielfeld.insert(schalter - 3, 0)


  print("So sieht dein Spielfeld jetzt aus: ")
  spielfeld_ausgeben()

spielfeld_ausgeben()

spielzug()