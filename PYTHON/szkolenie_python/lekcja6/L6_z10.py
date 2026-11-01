# Pułapka domyślnej listy

# Wersja z błędem — lista [] jest tworzona tylko raz
def dodaj_notatke(tresc: str, notatki=[]) -> list:
    notatki.append(tresc)
    return notatki


# Wywołujemy funkcję dwa razy bez podawania listy
wynik1 = dodaj_notatke("Zakupy")
print(wynik1)

wynik2 = dodaj_notatke("Pranie")
print(wynik2)

# Sprawdzamy, czy obie zmienne wskazują na ten sam obiekt
print(wynik1 is wynik2)


# Poprawiona wersja — używamy None
def dodaj_notatke_poprawiona(tresc: str, notatki=None) -> list:
    if notatki is None:
        notatki = []

    notatki.append(tresc)
    return notatki


# Wywołujemy poprawioną funkcję dwa razy bez podawania listy
wynik3 = dodaj_notatke_poprawiona("Zakupy")
print(wynik3)

wynik4 = dodaj_notatke_poprawiona("Pranie")
print(wynik4)

# Sprawdzamy, czy obie zmienne wskazują na ten sam obiekt
print(wynik3 is wynik4)