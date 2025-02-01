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
    '''Kontroluje jestli vstupní číslo odpovídá pravidlům hry'''

    if len(set(cislo)) != 4 or not cislo.isdigit() or cislo[0] == "0":
        return False
    return True

def vstup() -> str:
    '''Vratí vstup od uživatele'''

    cislo = input("Zadej číslo:\n")
    rozdelovnik()

    while not kontrola_vstupu(cislo):
      print("Tvůj vstup neodpovídá pravidlům.",
            "Zadej čtyřmistné číslo bez opakování číslic a nuly na začátku:",
            sep="\n")
      cislo = input() # vstup od uživatele
    
    return cislo

def porovnej(cislo: list, nahodne_cislo: list) -> dict:
    '''Porovnává čísla a vrací počet Bull a Cow'''

    bull = 0
    cow = 0

    for pozice in range(4):
        if cislo[pozice] == nahodne_cislo[pozice]:
            bull += 1
        elif cislo[pozice] in nahodne_cislo:
            cow += 1
            
    return {"bull": bull, "cow": cow}

print(nahodne_cislo())
print(type(nahodne_cislo()))