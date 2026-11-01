# zmiana kwoty netto na brutto
def brutto_z_netto(netto: float, vat: float = 0.23) -> float:
    # Dodanie VAT i zaokrąglenie wyniku do 2 miejsc po przecinku
    return round(netto * (1 + vat), 2)


# zmiana brutto na netto
def netto_z_brutto(brutto: float, vat: float = 0.23) -> float:
    # Odjęcie VAT i zaokrąglamy wynik do 2 miejsc po przecinku
    return round(brutto / (1 + vat), 2)


# wyprintowanie funkcji
print(brutto_z_netto(100))
print(netto_z_brutto(123))
print(brutto_z_netto(100, vat=0.08))