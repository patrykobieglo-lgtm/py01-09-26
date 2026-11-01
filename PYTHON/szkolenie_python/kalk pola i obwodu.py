# Pobranie długości i szerokości (z zamianą przecinka na kropkę)
dlugosc = float(input("Długość (m): ").replace(',', '.'))
szerokosc = float(input("Szerokość (m): ").replace(',', '.'))

# Obliczenie pola i obwodu
pole = dlugosc * szerokosc
obwod = 2 * dlugosc + 2 * szerokosc

# Wyświetlenie wyników
print(f"Pole: {pole} m²")
print(f"Obwód: {obwod} m")
