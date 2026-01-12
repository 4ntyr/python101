def hanoi(scheiben, start, ziel):
    if scheiben == 1:
        print(f"Bewege Scheibe von {start} nach {ziel}")
    else:
        zwischen = 6 - start - ziel
        hanoi(scheiben - 1, start, zwischen)
        print(f"Bewege Scheibe von {start} nach {ziel}")
        hanoi(scheiben - 1, zwischen, ziel)

# Variabler Aufruf mit Input
hanoi(int(input("Scheiben?: ")),1,3)