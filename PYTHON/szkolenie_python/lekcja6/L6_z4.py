def oblicz_srednia(*oceny):
    if not oceny:
        return 0

    srednia = sum(oceny) / len(oceny)
    return round(srednia, 2)
                 
print(oblicz_srednia(5, 4, 3, 5))
print(oblicz_srednia())
