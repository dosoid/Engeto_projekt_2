# Bulls & Cows - Hlavní prográm
"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie

author: Evžen Oskin
email: dos333@seznam.cz
"""

import projekt_2_funkce as p2f

if __name__ == "__main__":

      nahodne_cislo = p2f.nahodne_cislo() # vytvoří list 4 čísel
      bull_cow = {"bull": 0, "cow": 0} # vytvoří slovník pro počet Bull a Cow
      pocet_pokusu = 0

      print("Ahoj! Vítej ve hře Bulls & Cows!")
      p2f.rozdelovnik()
      print("Vytvořil jsem náhodné čtyřmistné číslo. Tvým úkolem je ho uhodnout.",
            "Pojďme hrát!",
            sep="\n")
      p2f.rozdelovnik()

      while bull_cow["bull"] != 4:
            
            cislo = p2f.vstup() 
            cislo_list = [int(cislo[i]) for i in range(4)] # převede vstup od uživatele na list
            bull_cow = p2f.porovnej(cislo_list, nahodne_cislo)
            pocet_pokusu += 1

            if bull_cow["bull"] == 1 or bull_cow["cow"] == 1:
                  print(f"{bull_cow["bull"]} Bull, {bull_cow["cow"]} Cow")
            else:
                  print(f"{bull_cow["bull"]} Bulls, {bull_cow["cow"]} Cows")
            print("Zkus to znovu:")
            p2f.rozdelovnik()
      else:
            print("Správně, uhodl jsi číslo!",
                  f"Počet pokusů: {pocet_pokusu}",
                  sep="\n")
            p2f.rozdelovnik()
            print("Gratuluji!")
            quit()
            