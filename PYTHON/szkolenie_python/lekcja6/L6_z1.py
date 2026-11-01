def opis_ksiazki(tytul, autor, rok_wydania=2024):
    return f'Ksiazka "{tytul}" napisana przez {autor}, wydana w roku {rok_wydania}'

print(opis_ksiazki("Lalka", "Bolesław Prus", 1890))

print(opis_ksiazki(autor="Bolesław Prus", tytul="Lalka", rok_wydania=1890))

print(opis_ksiazki("Lalka", "Bolesław Prus"))
