x = 10
stare_id = id(x)

x = x + 1

nowe_id = id(x)

print(stare_id == nowe_id)