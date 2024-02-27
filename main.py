SCHERMBREEDTE = 80
HELFT_SCHERMBREEDTE = SCHERMBREEDTE/2
MAX_WOORD_LENGTE = 20
naam_woordenlijsten = ['NL-EN', 'NL-DU', 'NL-FR' ]
import os
import sys

def main():
  doorgaan = 'ja'
  while doorgaan != 'nee':
    print_menu()
    keuze = input("| Wat wil je doen: ")
    if keuze == "N":
      clear_scherm()
      nieuwe_lijst_naam()
      
    elif keuze == "T":
      clear_scherm()
      woordenlijst = kies_lijst()
      woorden_toevoegen(woordenlijst)

    elif keuze == "O":
      woordenlijst = kies_lijst()
      clear_scherm()
      print_header("Hoe werkt het overhoren?")
      print_regel("1. Ik geef een woord.")
      print_regel("2. Jij geeft de vertaling.")
      print_regel("3. Ik check of het goed is.")
      print_footer("4. Daarna krijg je de vraag of je door wil gaan.")
      overhoren(woordenlijst)
            
    elif keuze == "Q":
      doorgaan = "nee"
      clear_scherm()
      print_afscheid()
    else:
      clear_scherm()
      print_regel("Deze keuze bestaat niet, probeer het opnieuw.")

def woorden_toevoegen(woordenlijst):
  doorgaan_woorden_toevoegen = "doorgaan"
  while doorgaan_woorden_toevoegen != "stop":
    doorgaan3 = "ja"
    woorden = nieuwe_woorden()
    schrijf_woordenlijst(woorden, woordenlijst)
    while doorgaan3 != "nee":
      doorgaan_woorden_toevoegen = input("Wil je meer woorden toevoegen (ja/nee): ")
      if doorgaan_woorden_toevoegen == "ja":
        clear_scherm()
        doorgaan3 = "nee"
      elif doorgaan_woorden_toevoegen == "nee":
        doorgaan_woorden_toevoegen = "stop"
        clear_scherm()
        doorgaan3 = "nee"
      else:
        print("Je hebt iets fout getyped.")


def schrijf_woordenlijst(woorden, woordenlijst):
  woordenlijst = lees_verander_woordenlijst(woordenlijst)
  woordenlijst.write("\n"+ woorden)

def nieuwe_woorden():
  clear_scherm()
  print_header(" ")
  woord1 = input("| Geef een woord: ")
  woord2 = input("| Geef de vertaling: ")
  return woord1+'='+woord2
  clear_scherm()



def print_afscheid():
  print("+" + "-"*(SCHERMBREEDTE-2) + "+")
  print(("| {:>" + str(MAX_WOORD_LENGTE)+ "}").format("Dankjewel voor he  gebruiken van dit overhoorprogramma, tot de volgende keer") + " |")
  print("+" + "-"*(SCHERMBREEDTE-2) + "+")

def print_footer(zin):
  print(("| {:" + str(SCHERMBREEDTE - 4)+ "} |").format(zin))
  print("="*(SCHERMBREEDTE))
    
def print_header(zin):
  print("="*(SCHERMBREEDTE))
  print(("| {:" + str(SCHERMBREEDTE - 4)+ "} |").format(zin))

  
def print_menu():
  print("+" + "-"*(SCHERMBREEDTE-2) + "+")
  print_regel("Maak een keuze uit de onderstaande mogenlijkheden")
  #print_regel("Je gebruikt nu de woordenlijst: " + woordenlijst)
  print("+" + "-"*(SCHERMBREEDTE-2) + "+")
  print_regel("Nieuwe woordenlijst -- N")
  print_regel("Verwijder woorden -- V")
  print_regel("Woorden toevoegen -- T")
  print_regel("Woordenlijst overhoren -- O")
  print_regel("Stoppen -- Q")
  print("+" + "-"*(SCHERMBREEDTE-2) + "+")
    
def print_regel(regel):
  print(("| {:" + str(SCHERMBREEDTE - 4)+ "} |").format(regel))

def kies_lijst():
  clear_scherm()
  print_header("Dit zijn je lijsten:")

  for l in range(len(naam_woordenlijsten)):
    print_regel(str(naam_woordenlijsten[l]))
  print_footer(" ")

  woordenlijst = input("| Welke lijst wil je gebruiken: ")
  return woordenlijst

def overhoren(bestandsnaam):
  doorgaan_overhoren = "ja"
  f = lees_woordenlijst(bestandsnaam)
  while doorgaan_overhoren != 'stop':
    for line in f:
      if doorgaan_overhoren != 'stop':
        woord, vertaling = line.strip('\n').split('=')
        print(woord)
        antwoord = input("Vertaling: ")
        clear_scherm()
        if antwoord == vertaling:
          print_regel("Goedzo!")
        else:
          print_regel("Dat is fout, de goede vertaling is: " + vertaling)
        print_header(" ")
        print_regel("Wil je verder klik  op enter.")
        print_regel("Wil je stoppen type stop.")
        doorgaan_overhoren = input("| Wat wil je doen: ")
        clear_scherm()
  f.close()

def nieuwe_lijst_naam():
  print_header(" ")
  print_regel("Dit is een voorbeeld van hoe je je lijst kan noemen:  NL-EN")
  lijst_nieuwe_naam = input("| Hoe wil je dat je nieuwe lijst gaat heten: ")
  naam_woordenlijsten.append(lijst_nieuwe_naam)
  open(lijst_nieuwe_naam + ".txt", "w")
  clear_scherm()
  print("Er is een woordenlijst aangemaakt met de naam: " + lijst_nieuwe_naam)

  naam_woordenlijsten

def lees_woordenlijst(bestandsnaam):
  f = open(bestandsnaam + '.txt')
  return f

def lees_verander_woordenlijst(bestandsnaam):
  f = open(bestandsnaam + '.txt', 'a')
  return f

def clear_scherm():
  os.system("cls" if os.name == "nt" else "clear")
    

main()



