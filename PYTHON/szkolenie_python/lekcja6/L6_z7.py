def stworz_profil(imie: str, **dane_dodatkowe) -> dict:
    profil = {"imie": imie}

    # update dodaje dane dodatkowe
    profil.update(dane_dodatkowe)

    return profil


profil = stworz_profil(
    "Patryk",
    wiek=43,
    miasto="Lublin",
    zawod="menedżer"
)

print(profil)