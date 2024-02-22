# João Lucas Mota Nogueira da Costa

import matplotlib.pyplot as plt
import numpy as np

def funcao(n):
    a = 3
    b = 5
    m = 31
    if (n == 0):
        valoresY.append(2)
    else:
        x = (a*valoresY[len(valoresY)-1]+b)%m
        valoresY.append(x)

def detecta(vetor):
    cont = 1
    init = 2
    for i in range(1,len(vetor)):
        if vetor[i] == init:
            print(f"Fim da sequencia {cont}: {i}")
            cont = cont+1

valoresY = []
valoresX = []

for i in range(0,101):
    valoresX.append(i+1)

for i in range (0, 101):
    funcao(i)

print(valoresY)
print('\n')

detecta(valoresY)

xpoints = np.array(valoresX)
ypoints = np.array(valoresY)

plt.plot(xpoints, ypoints)
plt.show()