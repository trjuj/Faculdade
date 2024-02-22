import pandas
dfcotacao = pandas.read_csv('cotacao.csv',sep=';')
print(dfcotacao['valor'])