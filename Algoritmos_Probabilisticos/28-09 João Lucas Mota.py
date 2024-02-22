# Joao Lucas Mota Nogueira da Costa

import random
import matplotlib.pyplot as plt
import numpy as np

def geraResistecias(N):

    R = [100, 150, 200]
    pop = []
    for i in range(N):
        am = []
        for j in R:
            x = random.randint(round(j*0.95), round(j*1.05))
            am.append(x)
        pop.append((am[0], am[1], am[2]))

    return pop

def getEquivalente(R):

    Eq = R[0] + 1/((1/R[1])+(1/R[2]))

    return Eq

N = 250 # ITERACOES
EQs = []
pop = geraResistecias(N)
for i in pop:
    EQs.append(getEquivalente(i))

media = np.mean(EQs)
desvio = np.std(EQs)

print(f"Media = {round(media, 2)} ohms")
print(f"Desvio Padrao = {round(desvio, 2)} ohms")
print(f"Intervalo de confiança: {round(media-(1.96*desvio),4)} ohms a {round(media+(1.96*desvio),4)} ohms")

resp = """ 
A incerteza de resistência dos componentes pode gerar alguns impactos, como estabilidade, precisão e em certos casos
até mesmo o funcionamento do sistema como um todo caso não tenham sido levadas em conta as porcentagens de tolerância
dos componentes utilizados ao projetar o sistema.
"""

print(resp)