def brutto_z_netto(netto: float, vat: float = 0.23) -> float:
    """Oblicza cenę brutto na podstawie ceny netto.

    Args:
        netto: Cena netto.
        vat: Stawka VAT zapisana jako liczba dziesiętna.

    Returns:
        Cena brutto zaokrąglona do dwóch miejsc po przecinku.
    """
    return round(netto * (1 + vat), 2)


def netto_z_brutto(brutto: float, vat: float = 0.23) -> float:
    """Oblicza cenę netto na podstawie ceny brutto.

    Args:
        brutto: Cena brutto.
        vat: Stawka VAT zapisana jako liczba dziesiętna.

    Returns:
        Cena netto zaokrąglona do dwóch miejsc po przecinku.
    """
    return round(brutto / (1 + vat), 2)


help(brutto_z_netto)


# mypy: Argument 1 to "brutto_z_netto" has incompatible type "str"; expected "float" [arg-type]
brutto_z_netto("100")