import sqlite3
conn = sqlite3.connect("kurs.db")
c = conn.cursor()
# UPDATE: SET – nowe wartości, WHERE – które wiersze zmienić
c.execute("UPDATE miasta SET populacja = ? WHERE nazwa = ?", (540000, "Poznań"))
print("Zmienione wiersze:", c.rowcount) # Zmienione wiersze: 1
c.execute("UPDATE miasta SET populacja = ? WHERE nazwa = ?", (250000, "Gdynia"))
if c.rowcount == 0:
print("Nie ma miasta Gdynia – nic nie zmieniono.")
# DELETE: dodajemy wiersz testowy bez populacji i od razu go usuwamy
c.execute("INSERT INTO miasta (nazwa) VALUES (?)", ("Miasto testowe",))
c.execute("DELETE FROM miasta WHERE populacja IS NULL")
print("Usunięte wiersze:", c.rowcount) # Usunięte wiersze: 1
conn.commit()
c.execute("SELECT nazwa, populacja FROM miasta WHERE nazwa = ?", ("Poznań",))
print(c.fetchone()) # ('Poznań', 540000)
conn.close()