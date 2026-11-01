def wielokrotne_powitanie(imie: str, ilosc: int) -> None:
    for i in range(1, ilosc + 1):
        print(f"{i}. Cześć, {imie}!")

print(wielokrotne_powitanie("Ala", 2))
