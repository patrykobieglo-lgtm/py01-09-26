
dni = ["pon", "wt", "śr", "czw", "pt", "sob", "niedz"]
temperatury = [14.5, 17.0, 12.5, 19.5, 21.0, 16.5, 13.0]

# 1. Najniższa temperatura
minimum = min(temperatury)

# 2. Najwyższa temperatura
maksimum = max(temperatury)

# 3. Średnia temperatura
srednia = sum(temperatury) / len(temperatury)

# 4. Temperatury od najniższej do najwyższej
rosnaco = sorted(temperatury)

# 5. Trzy najwyższe temperatury
# reverse=True sortuje od najwyższej do najniższej
# [:3] wybiera trzy pierwsze elementy
trzy_najcieplejsze = sorted(temperatury, reverse=True)[:3]

# 6. Szukamy pozycji najwyższej temperatury
indeks = temperatury.index(maksimum)

# Na tej samej pozycji w liście dni znajduje się najcieplejszy dzień
najcieplej = dni[indeks]

# Wyświetlamy wyniki
print(f"Min: {minimum}, max: {maksimum}, średnia: {srednia:.1f}")
print("Rosnąco:", rosnaco)
print("Trzy najcieplejsze:", trzy_najcieplejsze)
print("Najcieplej:", najcieplej)
