import random
import math
import matplotlib.pyplot as plt
from collections import Counter

def sqrt(x):
    return math.sqrt(x)

def log(x):
    return math.log(x)

def SPUTINIK(m, s):
    p0 = 0.322232431088 
    q0 = 0.099348462606
    p1 = 1.0
    q1 = 0.588581570495
    p2 = 0.342242088547 
    q2 = 0.531103462366
    p3 = 0.204231210245e-1 
    q3 = 0.103537752850
    p4 = 0.453642210148e-4 
    q4 = 0.385607006340e-2
    u = float(random.random())

    if u < 0.5:
        t = sqrt(-2.0*log(u))
    else:
        t = sqrt(-2*log(1-u))

    p = p0 + t * (p1 + t * (p2 + t * (p3 + t * p4)))
    q = q0 + t * (q1 + t * (q2 + t * (q3 + t * q4)))

    if u < 0.5:
        z = (p / q) - t
    else:
        z = t - (p / q)
        
    return (m + s * z)

def ADAMUS(alpha, scale):
    a = 1 / sqrt(2 * alpha-1)
    b = alpha - log(4)
    r1 = float(random.random())
    r2 = float(random.random())
    v = r1 / (1 - r1)
    x = alpha * math.pow(v, a)
    while( x > b + ((alpha * a+1) * log(v) - log(r1 * r1 * r2))):
    
        r1 = float(random.random())
        r2 = float(random.random())
        v = r1 / (1 - r1)
        x = alpha * math.pow(v, a)
    return (x / (alpha*scale))

qtd = 10000

valores_sputinik = []
valores_adamus = []
sputinik_arredondado = []
adamus_arredondado = []
sputinik_frequencia = []
adamus_frequencia = []

for i in range(qtd):
    valores_sputinik.append(SPUTINIK(0, 1))
    valores_adamus.append(ADAMUS(1, 1))

for i in range(qtd):
    sputinik_arredondado.append(round(valores_sputinik[i], 2))
    adamus_arredondado.append(round(valores_adamus[i], 2))
    result1 = [item for items, c in Counter(sputinik_arredondado).most_common() for item in [items] * c]
    result2 = [item for items, c in Counter(adamus_arredondado).most_common() for item in [items] * c]

for i in result1:
    x = result1.count(i)
    linha = (i, x)
    sputinik_frequencia.append(linha)
    while i in result1:
        result1.remove(i)

for i in result2:
    x = result2.count(i)
    linha = (i, x)
    adamus_frequencia.append(linha)
    while i in result2:
        result2.remove(i)

print("SPUTINIK:\n\nValor\tFrequencia")

for i in range(len(sputinik_frequencia)):
    print(f"{sputinik_frequencia[i][0]}:\t{sputinik_frequencia[i][1]}")

print("ADAMUS:\n\nValor\tFrequencia")

for i in range(len(adamus_frequencia)):
    print(f"{adamus_frequencia[i][0]}:\t{adamus_frequencia[i][1]}")

plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.hist(valores_sputinik, bins=250, density=True, alpha=0.6, color='g')
plt.title('SPUTINIK')
plt.xlabel('Valor')
plt.ylabel('Frequencia')

plt.subplot(1, 2, 2)
plt.hist(valores_adamus, bins=250, density=True, alpha=0.6, color='r')
plt.title('ADAMUS')
plt.xlabel('Valor')
plt.ylabel('Frequencia')

plt.tight_layout()
plt.show()