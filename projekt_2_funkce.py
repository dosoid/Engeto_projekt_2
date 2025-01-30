# v tomto souboru budou funkce pro hlavní projekt
import random

if __name__ == "__main__":
    print("Zde jsou pouze funkce, pro spuštění projektu použij soubor Projekt_2.py")

def rozdelovnik() -> None:
    '''Vytiskne rozdělovací čáru'''
    print("-" * 40)

def nahodne_cislo() -> list:
    '''Vytvoří náhodné čtyřmistné číslo'''
    return random.sample(range(10), 4)

print(nahodne_cislo())
print(type(nahodne_cislo()))