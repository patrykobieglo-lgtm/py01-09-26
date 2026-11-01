
n = 4

for wiersz in range(1, n + 1):
    spacje = n - wiersz
    gwiazdki = 2 * wiersz - 1
    print(" " * spacje + "*" * gwiazdki)

print(" " * (n - 1) + "|")
