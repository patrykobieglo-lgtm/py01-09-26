nazwa = input("nazwa_zadania: ")
czas = int(input("Planowany czas (min): "))
priorytet = int(input("Priorytet (1-3): "))
godziny = czas // 60
minuty = czas % 60
pilne = priorytet >= 2
print("=" * 20)
print("KARTA_ZADANIA:", nazwa)
print("Czas:", godziny, "godz.", minuty, "min")
print("Priorytet:", priorytet, end=" | ")
print("Pilne:", pilne)
print("=" * 20)
