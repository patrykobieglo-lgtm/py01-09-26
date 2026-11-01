
PIN = "1234"
saldo = 500
zalogowany = False

for proba in range(3):
    wpisany_pin = input("Podaj PIN: ")

    if wpisany_pin == PIN:
        zalogowany = True
        break
    else:
        print("Błędny PIN.")

if not zalogowany:
    print("Karta zablokowana")
else:
    while True:
        print("\n1 - Saldo")
        print("2 - Wypłata")
        print("3 - Wpłata")
        print("4 - Koniec")

        wybor = input("Wybierz opcję: ")

        if wybor == "1":
            print(f"Twoje saldo: {saldo} zł")

        elif wybor == "2":
            kwota_txt = input("Podaj kwotę wypłaty: ")

            if not kwota_txt.isdigit():
                print("Wpisz poprawną liczbę.")
                continue

            kwota = int(kwota_txt)

            if kwota <= 0 or kwota % 10 != 0:
                print("Kwota musi być wielokrotnością 10.")
                continue

            if kwota > saldo:
                print("Brak wystarczających środków.")
                continue

            saldo -= kwota
            print(f"Wypłacono {kwota} zł.")

        elif wybor == "3":
            kwota_txt = input("Podaj kwotę wpłaty: ")

            if not kwota_txt.isdigit():
                print("Wpisz poprawną liczbę.")
                continue

            kwota = int(kwota_txt)

            if kwota <= 0:
                print("Kwota musi być większa od zera.")
                continue

            saldo += kwota
            print(f"Wpłacono {kwota} zł.")

        elif wybor == "4":
            print("Do widzenia!")
            break

        else:
            print("Nieznana opcja.")
