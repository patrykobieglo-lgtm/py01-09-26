def pierogi():
    print("pierogi: start")
    farsz()
    print("pierogi: koniec")


def farsz():
    print("farsz: start")
    cebulka()
    print("farsz: koniec")


def cebulka():
    print("cebulka: start")
    print("cebulka: koniec")


# Przewidywana kolejność:
# pierogi: start
# farsz: start
# cebulka: start
# cebulka: koniec
# farsz: koniec
# pierogi: koniec

# Przy "farsz: koniec" na stosie są:
# pierogi
# farsz

pierogi()