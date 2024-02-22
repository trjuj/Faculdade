import pandas

dfpopulacao = pandas.read_csv('PopulacaoAmericaSul.csv',sep=';')
print(dfpopulacao)

qtde = len(dfpopulacao)

total = 0

for i in range(qtde):
    linha = dfpopulacao.iloc[i]
    print(linha['Pais'])
    total = total + linha['Populacao']
    
print('A população total da América do Sul: ',total, 'habitantes.')