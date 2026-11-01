
from datetime import date

print("=== Menedżer zadań — etap 4 ===")
print(f"Dziś jest: {date.today()}")

# 1. Tworzymy listę trzech zadań
do_zrobienia = [
    {
        "tytul": "Zrobić zakupy",
        "minuty": 40,
        "priorytet": 2,
        "tagi": set("dom, zakupy".split(", "))
    },
    {
        "tytul": "Napisać raport",
        "minuty": 60,
        "priorytet": 3,
        "tagi": set("praca, urzędy".split(", "))
    },
    {
        "tytul": "Zadzwonić do urzędu",
        "minuty": 65,
        "priorytet": 1,
        "tagi": set("dom, urzędy".split(", "))
    }
]

# 2. Wyświetlamy tytuł drugiego zadania
print("Drugie zadanie:", do_zrobienia[1]["tytul"])

# 3. Obliczamy sumę minut wszystkich zadań
suma_minut = sum(
    zadanie["minuty"] for zadanie in do_zrobienia
)
print("Łącznie minut:", suma_minut)

# 4. Tworzymy listę wykonanych zadań
zrobione = []

# 5. Przenosimy pierwsze zadanie do listy zrobione
zadanie = do_zrobienia.pop(0)
zrobione.append(zadanie)

# Uzupełniamy status wykonania w istniejących zadaniach
for zadanie in zrobione:
    zadanie["zrobione"] = True

for zadanie in do_zrobienia:
    zadanie["zrobione"] = False

# 6. Wyświetlamy liczbę zadań na obu listach
print("Do zrobienia:", len(do_zrobienia))
print("Zrobione:", len(zrobione))

# 7. Łączymy tagi ze wszystkich zadań
wszystkie_tagi = set()

for zadanie in do_zrobienia + zrobione:
    wszystkie_tagi = wszystkie_tagi | zadanie["tagi"]

print("Tagi:", sorted(wszystkie_tagi))

# 8. Pokazujemy pułapkę aliasu
archiwum = zrobione

zadanie_testowe = {
    "tytul": "Zadanie testowe",
    "minuty": 10,
    "priorytet": 1,
    "tagi": {"test"},
    "zrobione": False
}

archiwum.append(zadanie_testowe)

print(
    "Alias: zrobione ma",
    len(zrobione),
    "zadania"
)

# 9. Usuwamy zadanie testowe
zrobione.pop()

# 10. Tworzymy niezależną kopię listy
archiwum = zrobione.copy()
archiwum.append(zadanie_testowe)

print(
    "Kopia: zrobione ma",
    len(zrobione),
    "zadanie"
)

# 11. Łączymy zadania w jedną listę
zadania = do_zrobienia + zrobione

# ==============================
# MENU — ĆWICZENIE 13
# ==============================

while True:
    print("\n--- MENEDŻER ZADAŃ ---")
    print("1. Dodaj zadanie")
    print("2. Pokaż zadania")
    print("3. Oznacz jako zrobione")
    print("4. Zakończ")

    wybor = input("Wybierz opcję: ").strip()

    # OPCJA 1 — dodawanie zadania
    if wybor == "1":
        tytul = input("Podaj tytuł zadania: ").strip()

        if not tytul:
            print("Tytuł nie może być pusty!")
            continue

        zadanie = {
            "tytul": tytul,
            "tagi": set(),
            "minuty": 0,
            "priorytet": 2,
            "zrobione": False
        }

        zadania.append(zadanie)
        print("Dodano zadanie!")

    # OPCJA 2 — wyświetlanie zadań
    elif wybor == "2":
        if not zadania:
            print("Brak zadań na liście.")
            continue

        for i, zadanie in enumerate(zadania, start=1):
            status = (
                "Zrobione"
                if zadanie["zrobione"]
                else "Do zrobienia"
            )

            print(f"\n{i}. {zadanie['tytul']}")
            print(f"   Priorytet: {zadanie['priorytet']}")
            print(f"   Czas: {zadanie['minuty']} min")
            print(f"   Tagi: {', '.join(sorted(zadanie['tagi']))}")
            print(f"   Status: {status}")

    # OPCJA 3 — oznaczanie zadania jako zrobionego
    elif wybor == "3":
        if not zadania:
            print("Brak zadań na liście.")
            continue

        for i, zadanie in enumerate(zadania, start=1):
            print(f"{i}. {zadanie['tytul']}")

        try:
            numer = int(input("Podaj numer zadania: "))
        except ValueError:
            print("Wpisz prawidłowy numer.")
            continue

        if numer < 1 or numer > len(zadania):
            print("Nie ma zadania o takim numerze.")
            continue

        zadania[numer - 1]["zrobione"] = True
        print("Zadanie oznaczone jako zrobione!")

    # OPCJA 4 — zakończenie programu
    elif wybor == "4":
        print("Koniec programu!")
        break

    # Nieprawidłowy wybór
    else:
        print("Nieznana opcja. Wybierz od 1 do 4.")
        continue
