
wiek = int(input("Podaj wiek psa w latach: "))

if wiek < 0:
    print("Niepoprawny wiek psa.")
elif wiek == 0:
    print("Pies ma 0 ludzkich lat.")
elif wiek == 1:
    print("Pies ma 15 ludzkich lat.")
elif wiek == 2:
    print("Pies ma 24 ludzkie lata.")
else:
    ludzkie_lata = 24 + (wiek - 2) * 5
    print(f"Pies ma {ludzkie_lata} ludzkich lat.")
