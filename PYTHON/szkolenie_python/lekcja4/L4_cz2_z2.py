punkt = (10, 20, 30)
x, y, z = punkt
print(y)
#punkt[0] = 15
#TypeError: 'tuple' object does not support item assignment
nowy_punkt = (15,) + punkt[1:]
print(nowy_punkt)
