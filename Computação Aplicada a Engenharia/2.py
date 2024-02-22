import pandas

dfcotSH = pandas.read_csv('cotacaoSH.csv',sep=';',header=None,names=['currency','value'])

print(dfcotSH)

