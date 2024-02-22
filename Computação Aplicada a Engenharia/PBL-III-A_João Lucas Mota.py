import pandas

dffilmes = pandas.read_csv('Filmes.csv',sep=',')
print(dffilmes)

pais = input('Digite um pais (Primeira letra maiúscula): ')
qtde = len(dffilmes)
filmes = 0
visual = 0
lucro = 0

for i in range(qtde):
    linha = dffilmes.iloc[i]
    if pais == linha['Pais']:
        filmes = filmes + 1
        visual = visual + linha['Visualizacoes']
        lucro = lucro + (linha['Visualizacoes']*linha['Valor Unitario'])
        
if filmes == 0:
    print('Não há filmes disponíveis para este país.')
else:    
    print('Número de filmes disponíveis no(a)', pais, 'é: ',filmes)
    print('Total de visualizações: ',visual)
    print('Valor total arrecadado: ',round(lucro, 2))

dffilmes["Valor Total"] = round(dffilmes['Visualizacoes']*dffilmes['Valor Unitario'], 2)

x = input('Imprimir tabela com os valores totais? (S/N) \n')

if x == 'S':
    print(dffilmes)

dffilmes.to_csv('FilmesTotalizado.csv',sep=',')