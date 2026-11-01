ksiazka = {
    "Ania": "504417241",
    "Patryk": "501512145",
    "Nela": "500200100"
}
ksiazka["Marek"] = "400300100"
print(ksiazka)
del ksiazka["Nela"]
print(ksiazka)
imie = input("kogo szukasz? ")
numer = ksiazka.get(imie, "brak numeru")
print(numer)