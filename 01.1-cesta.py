import os
print(os.getcwd())
print(__file__)

cesta = os.path.dirname(__file__)
print(cesta)

cesta_k_souboru = os.path.join(cesta, "soubory/predmety.txt")
with open(cesta_k_souboru, encoding="utf-8") as soubor:
    text = soubor.read()
    print(text)