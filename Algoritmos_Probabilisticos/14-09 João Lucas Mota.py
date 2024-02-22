import random
import math
import matplotlib.pyplot as plt

def funcao1(x):
    y = x**2
    return y

def funcao2(x):
    y = math.sqrt(1-(x**2))
    return y

def geraPares1(N):
    coordX = []
    coordY = []
    for i in range(N):
        x = ((random.randint(0,20000))/10000)
        y = ((random.randint(0,40000))/10000)
        coordX.append(x)
        coordY.append(y)
    return coordX, coordY

def geraPares2(N):
    coordX = []
    coordY = []
    for i in range(N):
        x = ((random.randint(0,10000))/10000)
        y = ((random.randint(0,10000))/10000)
        coordX.append(x)
        coordY.append(y)
    return coordX, coordY

def checaPosicao1(x, y):
    if y < funcao1(x):
        return 0
    else:
        return 1
    
def checaPosicao2(x, y):
    if y < funcao2(x):
        return 0
    else:
        return 1

N = int(input("Numero de iteracoes: "))

crdX1, crdY1 = geraPares1(N)
inX1 = []
outX1 = []
inY1 = []
outY1 = []

for i in range(N):
    if checaPosicao1(crdX1[i], crdY1[i]):
        outX1.append(crdX1[i])
        outY1.append(crdY1[i])
    else:
        inX1.append(crdX1[i])
        inY1.append(crdY1[i])

crdX2, crdY2 = geraPares2(N)
inX2 = []
outX2 = []
inY2 = []
outY2 = []

for i in range(N):
    if checaPosicao2(crdX2[i], crdY2[i]):
        outX2.append(crdX2[i])
        outY2.append(crdY2[i])
    else:
        inX2.append(crdX2[i])
        inY2.append(crdY2[i])

plt.figure(figsize=[13,6.5])

plt.subplot(1,2,1)
result1 = round(8*(len(inX1)/N), 4)
plt.title(f"Aproximacao da integral: {result1}   Erro: {round((100*(abs(result1-(8/3))/(8/3))), 2)}%")
plt.scatter(inX1, inY1, s = 1, c = 'green')
plt.scatter(outX1, outY1, s = 1, c = 'red')

plt.subplot(1,2,2)
result2 = round(len(inX2)/N, 4)
plt.title(f"Aproximacao da integral: {result2}   Erro: {round((100*(abs(result2-(math.pi/4))/(math.pi/4))), 2)}%")
plt.scatter(inX2, inY2, s = 1, c = 'green')
plt.scatter(outX2, outY2, s = 1, c = 'red')
plt.show()