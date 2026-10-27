import os

cesta_souboru = os.path.join(os.path.dirname(__file__), "soubory/predmety.txt")

try:
    with open(cesta_souboru, encoding="utf-8") as soubor:
        batoh = [radek.strip() for radek in soubor]
except FileNotFoundError:
    batoh = []

print("Tvůj batoh:", ", ".join(batoh))

novy_predmet = input("Co chceš přidat? ").strip().lower()
if novy_predmet != "":
    batoh.append(novy_predmet)

zahodit = input("Co chceš zahodit? ").strip().lower()
if zahodit in batoh:
    batoh.remove(zahodit)
else:
    print("Tento předmět v batohu nemáš.")

with open(cesta_souboru, mode="w", encoding="utf-8") as soubor:
    for predmet in batoh:
        soubor.write(f"{predmet}\n")