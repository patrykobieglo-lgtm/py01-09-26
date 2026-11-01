def analiza_listy(liczby: list[int]) -> tuple[int, int, int]:
    najmniejsza = min(liczby)
    najwieksza = max(liczby)
    suma = sum(liczby)

    # Nie używamy nazw min, max i sum jako zmiennych,
    # ponieważ są to nazwy wbudowanych funkcji Pythona.

    return najmniejsza, najwieksza, suma


najmniejsza, najwieksza, suma = analiza_listy([4, 9, 1, 7])

print(f"Min: {najmniejsza}, max: {najwieksza}, suma: {suma}")