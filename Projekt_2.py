# Bulls & Cows - Hlavní prográm
"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie

author: Evžen Oskin
email: dos333@seznam.cz
"""

import projekt_2_funkce as p2f
from datetime import datetime

if __name__ == "__main__":

      hrajeme = True # proměnná pro ukončení hry
      historie = [] # vytvoří list pro uchování historie hry

      while hrajeme:

            start_time = datetime.now() # začátek hry
            nahodne_cislo = p2f.nahodne_cislo() # vytvoří list 4 čísel
            bull_cow = {"bull": 0, "cow": 0} # vytvoří slovník pro počet Bull a Cow
            pocet_pokusu = 0 # počítadlo pokusů
            statistika = {} # vytvoří slovník pro uchování statistiky za poslední hru

            print(nahodne_cislo) # pro účely rychlejšího testu odstraň komentář #

            p2f.pozdrav() # pozdraví uživatele

            while bull_cow["bull"] != 4:
                  
                  cislo = p2f.vstup() 
                  cislo_list = [int(cislo[i]) for i in range(len(cislo))] # převede vstup od uživatele na list
                  bull_cow = p2f.porovnej(cislo_list, nahodne_cislo)
                  vysledek_bull = p2f.mnozne_cislo(bull_cow['bull'], 'Bull')
                  vysledek_cow = p2f.mnozne_cislo(bull_cow['cow'], 'Cow')
                  pocet_pokusu += 1

                  if bull_cow["bull"] != 4:
                        print(vysledek_bull + ", " + vysledek_cow)
                  else:
                        break
                  
                  p2f.rozdelovnik()
            
            print("Správně, uhodl jsi číslo!",
                  f"Počet pokusů: {pocet_pokusu}",
                  sep="\n")
            
            end_time = datetime.now() # čas konce hry
            doba_hry = end_time - start_time # výpočet doby hry

            print('Doba hraní: {}'.format(doba_hry))
            p2f.rozdelovnik()
            print("Gratuluji!")
            p2f.rozdelovnik()

            # uložení statistiky do historie a omezení na 3 položky

            statistika["Počet_pokusů"] = pocet_pokusu
            statistika["Doba_hry"] = '{}'.format(doba_hry)
            historie = [statistika] + historie

            if len(historie) > 3:
                  historie.pop()
                  
            # dotaz na další hru

            neni_konec_hry = input("Chceš hrát znovu? Napiš \"ano\" pro pokračování, jinak je konec: ")

            if neni_konec_hry == "ano":
                  print("Začínáme znovu!")
                  p2f.rozdelovnik()
            else:
                  print("Děkuji za hru! Měj se hezky!")
                  p2f.rozdelovnik()
                  print("Historie posledních her (max 3):")
                  print(historie)
                  hrajeme = False

      quit()
            