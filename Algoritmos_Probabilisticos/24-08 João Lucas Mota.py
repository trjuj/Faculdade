import random
import os

def jogaDado():
    results = []
    for i in range(4):
        results.append(random.randint(1,6))
    return results

def prob(N):
    eventos = 0
    cont = 0
    while cont <= N:
        results = jogaDado()
        if 6 not in results:
            cont += 1
        else:
            if results[0] != 6:
                if results[1] != 6:
                    if results[2] != 6:
                        if results[3] == 6:
                            eventos += 1
                        else:
                            cont += 1
                    else:
                        cont += 1
                else:
                    cont += 1
            else:
                cont += 1
    prob = float(eventos / N)

    return prob

os.system('cls')
N = int(input("Numero de iteracoes: "))
x = float(prob(N))
print (f"Probabilidade do evento acontecer: {x} ou {round(x*100, 6)}%")
