
slowo = input("Podaj tekst: ")

samogloski = "aąeęioóuy"
wynik = ""
licznik = 0

for litera in slowo:
    if litera.lower() not in samogloski:
        continue

    wynik += litera + " "
    licznik += 1

print(wynik.strip())
print(f"Liczba samogłosek: {licznik}")
