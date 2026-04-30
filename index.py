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
    t.pencolor(farg)
    for i in range(4):
        t.forward(sida)
        t.left(90)

    # TODO: Implementera funktionen
    # 1. Sätt pennans färg med t.pencolor(farg)
    # 2. Upprepa 4 gånger:
    #    - Gå framåt med t.forward(sida)
    #    - Sväng vänster 90 grader med t.left(90)
    pass


def rita_triangel(t, sida, farg):
    t.pencolor(farg)
    for i in range(3):
        t.forward(sida)
        t.left(120)

    # TODO: Implementera funktionen
    # 1. Sätt pennans färg med t.pencolor(farg)
    # 2. Upprepa 3 gånger:
    #    - Gå framåt med t.forward(sida)
    #    - Sväng vänster 120 grader med t.left(120)
    pass


def rita_cirkel(t, radie, farg):
    t.pencolor(farg)
    t.circle(radie)

    # TODO: Implementera funktionen
    # 1. Sätt pennans färg med t.pencolor(farg)
    # 2. Använd t.circle(radie) för att rita cirkeln
    pass


def rita_blomma(t, kronblad, sida, farg):
    vinkel = 360 / kronblad
    for i in range(kronblad):
        rita_kvadrat(t, sida, farg)
        t.left(vinkel)
    
    # TODO: Implementera funktionen
    # 1. Beräkna vinkeln mellan varje kronblad: 360 / kronblad
    # 2. Upprepa kronblad gånger:
    #    - Anropa rita_kvadrat(t, sida, farg)
    #    - Sväng med den beräknade vinkeln med t.left(vinkel)
    pass


# === HUVUDPROGRAM ===

def huvudprogram():
    t = turtle.Turtle()
    t.speed(5)

    # TODO: Skapa en turtle
    # t = turtle.Turtle()
    
    # TODO: Ställ in hastighet med t.speed()
    # Standard: 5 (medel), 0 (snabbast), 10 (snabb)
    
    while True:
        print("\n--- TURTLE MÖNSTER ---")
        print("1. Rita kvadrat")
        print("2. Rita triangel")
        print("3. Rita cirkel")
        print("4. Rita blomma")
        print("5. Avsluta")

        # TODO: Visa meny
        # print("\n--- TURTLE MÖNSTER ---")
        # print("1. Rita kvadrat")
        # print("2. Rita triangel")
        # print("3. Rita cirkel")
        # print("4. Rita blomma")
        # print("5. Avsluta")
        
        val = input("Valj: ")
        
        if val == "1":
            sida = int(input("Sida: "))
            farg = input("Farg: ")
            rita_kvadrat(t, sida, farg)

            # TODO: Fråga efter sida och färg
            # sida = int(input("Sida: "))
            # farg = input("Farg: ")
            # Anropa rita_kvadrat(t, sida, farg)
            pass
        elif val == "2":
            sida = int(input("Sida: "))
            farg = input("Farg: ")
            rita_triangel(t, sida, farg)

            # TODO: Fråga efter sida och färg
            # Anropa rita_triangel(t, sida, farg)
            pass
        elif val == "3":
            radie = int(input("Radie: "))
            farg = input("Farg: ")
            rita_cirkel(t, radie, farg)

            # TODO: Fråga efter radie och färg
            # Anropa rita_cirkel(t, radie, farg)
            pass
        elif val == "4":
            kronblad = int(input("Antal kronblad: "))
            sida = int(input("Sida: "))
            farg = input("Farg: ")
            rita_blomma(t, kronblad, sida, farg)

            # TODO: Fråga efter antal kronblad, sida och färg
            # kronblad = int(input("Antal kronblad: "))
            # sida = int(input("Sida: "))
            # farg = input("Farg: ")
            # Anropa rita_blomma(t, kronblad, sida, farg)
            pass
        elif val == "5":
            print("Programmet avslutas.")
            turtle.done()
            break

            # TODO: Avsluta
            # turtle.done()  # Håller fönstret öppet
            # break
            pass
        else:
            print("Ogiltigt val, forsok igen.")


# Starta programmet om filen körs direkt
if __name__ == "__main__":
    huvudprogram()