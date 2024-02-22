import math

x = float(input('Digite a distância percorrida desde o início da corrida: '))

f = 2*math.sin(x) + 30
g = 4*math.cos(x) + 30
d = f - g

print('Diferença de temperatura: ',d)

print('Diferença > 0 : ',d > 0)
