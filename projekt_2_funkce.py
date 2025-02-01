# v tomto souboru budou funkce pro hlavní projekt
import random

if __name__ == "__main__":
    print("Zde jsou pouze funkce, pro spuštění projektu použij soubor Projekt_2.py")

def rozdelovnik() -> None:
    '''Vytiskne rozdělovací čáru'''
    print("-" * 40)

def nahodne_cislo() -> list:
    '''Vytvoří náhodné čtyřmistné číslo'''

    cislo = random.sample(range(10), 4)
    while cislo[0] == 0:
        cislo = random.sample(range(10), 4)

    return cislo

def kontrola_vstupu(cislo: str) -> bool:
    '''Kontroluje jestli uživatel zadal správně 4-mistné číslo'''

    if len(cislo) != 4 or not cislo.isgidit() or cislo[0] == "0":
        return False
    return True

def vstup() -> str:
    '''Vratí vstup od uživatele'''

    cislo = input("Zadej čtyřmistné číslo bez 0 na začátku: ")
    
    while not kontrola_vstupu(cislo):
      print("Tvůj vstup neodpovídá pravidlům, zadej znovu: ")
      cislo = input() # vstup od uživatele
    
    return cislo

def porovnej(cislo: list, nahodne_cislo: list) -> tuple:
    '''Porovnává čísla a vrací počet Bull a Cow'''

    bull = 0
    cow = 0

    for  pozice in range(4):
        if cislo[pozice] == nahodne_cislo[pozice]:
            bull += 1
        elif cislo[pozice] in nahodne_cislo:
            cow += 1
            
    return bull, cow

print(nahodne_cislo())
print(type(nahodne_cislo()))