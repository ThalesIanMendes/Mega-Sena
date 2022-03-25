import time
import random

def linha(tam):
    return '*' * tam

def cabeçalho(txt):
    print(linha(42))
    print(txt.center(42))
    print(linha(42))

cabeçalho('MegaSena')
LD = True
while LD:
    lista = []
    for i in range(6):
        sorteio = random.randint(1,60)
        lista.append(sorteio)
        lista.sort()
        time.sleep(0.2)

    if (lista[0] != lista[1] != lista[2] != lista[3] != lista[4] != lista[5] ):
        print("Sorteando...")
        time.sleep(1)
        print(lista)

        with open("Arquivo.txt", "a") as arquivo:
            arquivo.write("Nomeros: ")
            for item in lista:
                arquivo.write("%s - " % item)
        with open("Arquivo.txt", "a") as arquivo:
            arquivo.write("\n")
        LD = False



