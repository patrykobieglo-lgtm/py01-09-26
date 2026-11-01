slowo = input("podaj słowo: ")
odwrocone = slowo[::-1]
print("od tylu:", odwrocone)
print(slowo.lower(), odwrocone.lower())
if slowo.lower() == odwrocone.lower():
    print("to jest palindrom!")
else:
    print("to nie jest palindrom.") 
      
