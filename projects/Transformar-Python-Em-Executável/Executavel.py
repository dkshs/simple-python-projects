# NOTA! Necessário a biblioteca 'pyinstaller' para gerar o executável.

# Esse código eu recomendo criar um ambiente virtual para resultados melhores.
# ------ Só rodar no terminal `pip install pyinstaller` ----
# ---- Leia o README.md desta pasta para mais informações ----

import time

time.sleep(1)
print("hello world")
time.sleep(1)
y = "Y"
while y == "Y":
    x = input('Digite seu nome: ')
    print(f"Olá {x}")
    y = input("Again? Y/n: ")
    if y == "" or y == "Y" or y == "y":
        y = "Y"
    elif y == "n" or y == "N":
        time.sleep(0.5)
        print("Tchau!")
        time.sleep(1)
        break
