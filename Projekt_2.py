# Bulls & Cows - Hlavní prográm
"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie

author: Evžen Oskin
email: dos333@seznam.cz
"""

import projekt_2_funkce as p2f

nahodne_cislo = p2f.nahodne_cislo() # vytvoří list 4 čísel

print("Ahoj! Vítej ve hře Bulls & Cows!")
p2f.rozdelovnik()
print("Vytvořil jsem náhodné čtyřmistné číslo. Tvým úkolem je ho uhodnout.",
      "Pojďme hrát!",
      sep="\n")
p2f.rozdelovnik()
cislo = p2f.vstup() # vstup od uživatele
p2f.rozdelovnik()

cislo_list = [int(cislo[i] for i in range(4))] # převede vstup od uživatele na list

bull_cow = p2f.porovnej(cislo = cislo_list, nahodne_cislo = nahodne_cislo)

while bull_cow[0] != 4:
      if bull_cow[0] == 1 or bull_cow[1] == 1:
            print(f"{bull_cow[0]} Bull, {bull_cow[1]} Cow")
      else:
            print(f"{bull_cow[0]} Bulls, {bull_cow[1]} Cows")
      print("Zkus to znovu:")
      p2f.rozdelovnik()
      cislo = p2f.vstup() 
else:
      print("Správně, uhodl jsi číslo!")
      p2f.rozdelovnik()
      print("Gratuluji!")
      