telefon = {
    "Mama": "601 111 222",
    "Kasia": "700 800 900",
    "Pan Józef": "512 000 333"
}
telefon["Bartek"] = "123 456 789"
telefon["Kasia"] = "111 222 333"
del telefon["Pan Józef"]
print(telefon)
imie = input("Kogo szukasz? ")
numer = telefon.get(imie, "brak numeru")
print(f"{imie}: {numer}")
