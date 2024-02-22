import pandas

dfcarros = pandas.read_csv('EstoqueCarros.csv',sep=';')
print(dfcarros)

marca = input('Digite uma marca de carro: ')

total = 0

qtde = len(dfcarros)

for i in range(qtde):
    linha = dfcarros.iloc[i]
    if marca == linha['Marca']:
        total = total + linha['Quantidade']

print('Total de carros da marca', marca,': ',total)