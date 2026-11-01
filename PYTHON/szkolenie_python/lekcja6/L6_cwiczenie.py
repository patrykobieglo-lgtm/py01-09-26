def pokaz_cene_po_rabacie(nazwa, cena):
    print(f"{nazwa}: {cena * 0.85:.2f} zł")

pokaz_cene_po_rabacie("Laptop", 3200) # Laptop: 2720.00 zł
pokaz_cene_po_rabacie("Myszka", 120) # Myszka: 102.00 zł
pokaz_cene_po_rabacie("Monitor", 900) # Monitor: 765.00 z
pokaz_cene_po_rabacie("kupa", 100)
#rozłoenie ratami
def rozloz_na_raty(kwota, liczba_rat):
    if liczba_rat <= 0:
        return None #wczesny return: reszta się nie wykona
    rata = round(kwota / liczba_rat, 2)
    ostatnia = round(kwota - rata * (liczba_rat - 1), 2)#wyrównuje grosze
    return rata, ostatnia