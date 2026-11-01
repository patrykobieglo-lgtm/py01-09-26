
cena = 100
student = input("Czy jesteś studentem? (tak/nie): ")
wiek = int(input("Podaj wiek: "))

cena_koncowa = cena * 0.5 if student == "tak" or wiek < 18 else cena

print(f"Cena biletu: {cena_koncowa:.2f} zł")