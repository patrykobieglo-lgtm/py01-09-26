
import random

liczba = random.randint(1, 100)

for proba in range(1, 8):
    strzal = int(input(f"Próba {proba}/7: "))

    if strzal == liczba:
        print(f"Brawo! Zgadłeś w {proba} próbach.")
        break
    elif strzal < liczba:
        print("Za mało!")
    else:
        print("Za dużo!")
else:
    print(f"Koniec prób! Wylosowana liczba to {liczba}.")
