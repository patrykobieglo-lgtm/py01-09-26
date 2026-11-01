lista1 = [1, 1]
lista2 = [1, 1]
lista3 = lista1

print("lista1 == lista2:", lista1 == lista2)
print("lista1 is lista2:", lista1 is lista2)

print("lista1 == lista3:", lista1 == lista3)
print("lista1 is lista3:", lista1 is lista3)

print("lista2 == lista3:", lista2 == lista3)
print("lista2 is lista3:", lista2 is lista3)

lista3.append(3)

print(lista1)
