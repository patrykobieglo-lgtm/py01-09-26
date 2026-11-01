
from pathlib import Path

sciezka = Path("dane") / "raporty" / "raport.txt"

print(sciezka.name, sciezka.stem, sciezka.suffix)
print(sciezka.parent)

sciezka.parent.mkdir(parents=True, exist_ok=True)

sciezka.write_text("To jest raport.", encoding="utf-8")

print(sciezka.read_text(encoding="utf-8"))
print(sciezka.exists())

for element in Path("dane").iterdir():
    print(element.name, element.is_dir())

for plik in Path("dane").glob("**/*.txt"):
    print(plik)
