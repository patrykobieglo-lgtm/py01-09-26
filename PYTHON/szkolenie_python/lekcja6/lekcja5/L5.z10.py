
imiona = ["Anna", "Jan", "Piotr", "Kasia"]

szukane = input("Podaj imię do wyszukania: ")

for pozycja, imie in enumerate(imiona, start=1):
    if imie == szukane:
        print(f"Znaleziono na pozycji {pozycja}.")
        break
else:
    print("Nie znaleziono imienia.")
