# Bulls & Cows - Hlavní prográm
"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie

author: Evžen Oskin
email: dos333@seznam.cz
"""
import random
import projekt_2_funkce as p2f

print("Ahoj! Vítej ve hře Bulls & Cows!")
p2f.rozdelovnik()
print("Vytvořil jsem náhodné čtyřmistné číslo. Tvým úkolem je ho uhodnout.",
      "Pojďme hrát!",
      sep="\n")
p2f.rozdelovnik()
print("Zadej čtyřmistné číslo:")
p2f.rozdelovnik()

nahodne_cislo = p2f.nahodne_cislo()
cislo = input()

