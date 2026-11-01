nazwa1, cena1, ilosc1 = "Zeszyt", 4.99, 1
nazwa2, cena2, ilosc2 = "Segregator", 7.49, 1
nazwa3, cena3, ilosc3 = "Długopis", 3.29, 2
suma = cena1 * ilosc1 + cena2 * ilosc2 + cena3 * ilosc3
print("Surowa suma:", suma)
suma_zaokroglona = round(suma, 2)
vat = suma * 23 / 123
print("PARAGON")
print(nazwa1, cena1, "zł x", ilosc1)
print(nazwa2, cena2, "zł x", ilosc2)
print(nazwa3, cena3, "zł x", ilosc3)
print("Suma:", suma_zaokroglona, "zł")
print("------------------")
print("VAT:", round(vat, 2), "zł")

#ponizej po poprawce

nazwa1, cena1, ilosc1 = "Zeszyt", 4.99, 1
nazwa2, cena2, ilosc2 = "Segregator", 7.49, 1
nazwa3, cena3, ilosc3 = "Długopis", 3.29, 2
suma = cena1 * ilosc1 + cena2 * ilosc2 + cena3 * ilosc3
print("Surowa suma:", suma)
suma_zaokroglona = round(suma, 2)
vat = suma * 23 / 123
print("\nPARAGON")
print(f"{'Produkt':<15} {'Ilość':>5} {'Wartość':>10}")
print("-" * 32)
print(f"{nazwa1:<15} {ilosc1:>5} {cena1 * ilosc1:>10.2f}")
print(f"{nazwa2:<15} {ilosc2:>5} {cena2 * ilosc2:>10.2f}")
print(f"{nazwa3:<15} {ilosc3:>5} {cena3 * ilosc3:>10.2f}")
print("-" * 32)
print(f"{'RAZEM':<15} {'':>5} {suma_zaokroglona:>10.2f}")
print(f"{'w tym VAT 23%':<15} {'':>5} {vat:>10.2f}")