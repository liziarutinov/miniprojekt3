"""
Projekt 3: Geometriska mönster med Turtle
Ett menybaserat program som ritar geometriska figurer med Turtle-grafik.
Funktioner som ska implementeras:
- rita_kvadrat(t, sida, farg)
- rita_triangel(t, sida, farg)
- rita_cirkel(t, radie, farg)
- rita_blomma(t, kronblad, sida, farg)
- huvudprogram() med meny
"""

import turtle


# === FIGURER ===

def rita_kvadrat(t, sida, farg):
    """
    Ritar en kvadrat.
    
    Parametrar:
        t: Turtle-objektet
        sida (int): Längden på sidan
        farg (str): Färg på linjen
    """
    # TODO: Implementera funktionen
    # 1. Sätt pennans färg med t.pencolor(farg)
    # 2. Upprepa 4 gånger:
    #    - Gå framåt med t.forward(sida)
    #    - Sväng vänster 90 grader med t.left(90)
    pass


def rita_triangel(t, sida, farg):
    """
    Ritar en liksidig triangel.
    
    Parametrar:
        t: Turtle-objektet
        sida (int): Längden på sidan
        farg (str): Färg på linjen
    """
    # TODO: Implementera funktionen
    # 1. Sätt pennans färg med t.pencolor(farg)
    # 2. Upprepa 3 gånger:
    #    - Gå framåt med t.forward(sida)
    #    - Sväng vänster 120 grader med t.left(120)
    pass


def rita_cirkel(t, radie, farg):
    """
    Ritar en cirkel.
    
    Parametrar:
        t: Turtle-objektet
        radie (int): Cirkelns radie
        farg (str): Färg på linjen
    """
    # TODO: Implementera funktionen
    # 1. Sätt pennans färg med t.pencolor(farg)
    # 2. Använd t.circle(radie) för att rita cirkeln
    pass


def rita_blomma(t, kronblad, sida, farg):
    """
    Ritar en blomma genom att upprepa en kvadrat i en cirkel.
    
    Parametrar:
        t: Turtle-objektet
        kronblad (int): Antal kronblad (kvadrater)
        sida (int): Sidlängd på varje kvadrat
        farg (str): Färg på linjen
    """
    # TODO: Implementera funktionen
    # 1. Beräkna vinkeln mellan varje kronblad: 360 / kronblad
    # 2. Upprepa kronblad gånger:
    #    - Anropa rita_kvadrat(t, sida, farg)
    #    - Sväng med den beräknade vinkeln med t.left(vinkel)
    pass


# === HUVUDPROGRAM ===

def huvudprogram():
    """
    Huvudprogrammet som styr menyn och programflödet.
    """
    # TODO: Skapa en turtle
    # t = turtle.Turtle()
    
    # TODO: Ställ in hastighet med t.speed()
    # Standard: 5 (medel), 0 (snabbast), 10 (snabb)
    
    while True:
        # TODO: Visa meny
        # print("\n--- TURTLE MÖNSTER ---")
        # print("1. Rita kvadrat")
        # print("2. Rita triangel")
        # print("3. Rita cirkel")
        # print("4. Rita blomma")
        # print("5. Avsluta")
        
        val = input("Valj: ")
        
        if val == "1":
            # TODO: Fråga efter sida och färg
            # sida = int(input("Sida: "))
            # farg = input("Farg: ")
            # Anropa rita_kvadrat(t, sida, farg)
            pass
        elif val == "2":
            # TODO: Fråga efter sida och färg
            # Anropa rita_triangel(t, sida, farg)
            pass
        elif val == "3":
            # TODO: Fråga efter radie och färg
            # Anropa rita_cirkel(t, radie, farg)
            pass
        elif val == "4":
            # TODO: Fråga efter antal kronblad, sida och färg
            # kronblad = int(input("Antal kronblad: "))
            # sida = int(input("Sida: "))
            # farg = input("Farg: ")
            # Anropa rita_blomma(t, kronblad, sida, farg)
            pass
        elif val == "5":
            # TODO: Avsluta
            # turtle.done()  # Håller fönstret öppet
            # break
            pass
        else:
            print("Ogiltigt val, forsok igen.")


# Starta programmet om filen körs direkt
if __name__ == "__main__":
    huvudprogram()