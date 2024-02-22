# Joao Lucas Mota Nogueira da Costa

import random
import math
import os
import matplotlib.pyplot as plt
import matplotlib.patches as pat

def geraPares(N):
    coordX = []
    coordY = []
    for i in range(N):
        x = ((random.randint(0,10000))/10000)
        y = ((random.randint(0,10000))/10000)
        coordX.append(x)
        coordY.append(y)
    return coordX, coordY

def checaDistancia(x, y):
    distanciaX = x - 0.5
    distanciaY = y - 0.5
    distancia = math.sqrt(distanciaX**2 + distanciaY**2)
    
    if distancia < 0.5:
        return 1
    else:
        return 0

dentro = 0
inX = []
inY = []
outX = []
outY = []

os.system('cls')

N = int(input("Numero de iteracoes: "))

crdX, crdY = geraPares(N)

for i in range(len(crdX)):
    if checaDistancia(crdX[i], crdY[i]):
        inX.append(crdX[i])
        inY.append(crdY[i])
        dentro += 1
    else:
        outX.append(crdX[i])
        outY.append(crdY[i])

pi = 4*(dentro/N)

plt.figure(figsize = [6.5, 6.5])
plt.title(f'Aproximacao de Pi: {pi}        Erro: {round((100*(abs(pi-math.pi)/math.pi)), 2)}%')
plt.subplot().add_artist(pat.Circle((0.5, 0.5), 0.5, fill = False, lw = 2))
plt.scatter(inX, inY, s = 0.5, c = 'green')
plt.scatter(outX, outY, s = 0.5, c = 'red')
plt.show()