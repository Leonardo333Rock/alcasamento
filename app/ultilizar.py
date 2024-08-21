import random
import os


codigos = [1000,2000,3000,4000,5000,6000,7000,8800]

def Sortear(codigo):
    numero_aleatorio = random.randint(1000, 9999)
    for n in codigo:
        if numero_aleatorio == n:
            numero_aleatorio = random.randint(1000, 9999)
            Sortear(codigo)

    return  int(numero_aleatorio)

print(Sortear(codigos))