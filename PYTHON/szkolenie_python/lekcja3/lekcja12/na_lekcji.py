
class SklepError(Exception):
    """Podstawowy wyjątek sklepu."""
    pass


class BrakTowaruError(SklepError):
    """Brak wystarczającej ilości towaru."""
    def __init__(self, nazwa, dostepne, zamowione):
        self.nazwa = nazwa
        self.dostepne = dostepne
        self.zamowione = zamowione
        super().__init__(
            f"Brak towaru: {nazwa} "
            f"(zamówiono {zamowione}, dostępne {dostepne}). "
            f"Kupić {dostepne}?"
        )


class NiepoprawnaIloscError(SklepError, ValueError):
    """Niepoprawna ilość produktu."""
    def __init__(self, ilosc):
        self.ilosc = ilosc
        super().__init__(
            f"ilość musi być dodatnia, podano {ilosc}"
        )


def kup(magazyn, nazwa, ilosc):
    if ilosc <= 0:
        raise NiepoprawnaIloscError(ilosc)

    try:
        dostepne = magazyn[nazwa]
    except KeyError as e:
        raise SklepError(
            f"nieznany produkt: {nazwa}"
        ) from e

    if ilosc > dostepne:
        raise BrakTowaruError(nazwa, dostepne, ilosc)

    magazyn[nazwa] -= ilosc
    return magazyn[nazwa]


magazyn = {"kawa": 3, "herbata": 10}

zakupy = [
    ("kawa", 5),
    ("herbata", 0),
    ("kakao", 1),
    ("herbata", 2),
]

for nazwa, ilosc in zakupy:
    try:
        pozostalo = kup(magazyn, nazwa, ilosc)
        print(f"Kupiono: {nazwa} ×{ilosc}, zostało {pozostalo}")

    except BrakTowaruError as e:
        print(e)

    except ValueError as e:
        print(f"Błąd sklepu: {e}")

    except SklepError as e:
        print(f"Błąd sklepu: {e}")
