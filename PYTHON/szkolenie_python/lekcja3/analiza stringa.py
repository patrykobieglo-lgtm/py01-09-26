slowo = input("Podaj słowo: ")
odwrocone = slowo[::-1]
print(f"Od tyłu: {odwrocone}")
if slowo.lower() == odwrocone.lower():
   print("To jest palindrom.")
else:
    print("To nie jest palindrom.")
