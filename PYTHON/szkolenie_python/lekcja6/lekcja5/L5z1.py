
wiek = int(input("Podaj wiek: "))

if wiek < 0:
    print("Niepoprawny wiek")
elif wiek <= 1:
    print("Niemowlę")
elif wiek <= 12:
    print("Dziecko")
elif wiek <= 17:
    print("Nastolatek")
elif wiek <= 64:
    print("Dorosły")
else:
    print("Senior")
