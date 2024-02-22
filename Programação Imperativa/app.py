print('Digite o número de itens na lista: ')
q = int(input())
a = []

while len(a) < q:
    print('Digite um núemro inteiro ',len(a),'/',q,': ')
    x = int(input())
    a.append(x)

media = sum(a)/q

abaixo = 0
acima = 0
igual = 0

for i in range(q):
    if a[i] < media:
        abaixo += 1
    if a[i] > media:
        acima += 1
    if a[i] == media:
        igual += 1

print('\nA média aritmética é: ',float(media))
print('O total de números abaixo da média é: ',abaixo)
print('O total de números iguais a média é: ',igual)
print('O total de números acima da média é: ',acima)
