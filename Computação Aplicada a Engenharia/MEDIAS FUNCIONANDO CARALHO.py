import pandas as pd

dados = pd.read_csv('DadosClimaticos2018Londrina.csv',sep=';')

def Medias(tabela):
    MediaMensal = []
    soma = 0
    qntd = 0
    mesatual = 1
    for i in range(len(tabela)):
        linha = tabela.iloc[i]
        data = linha['Data']
        temp = float(linha['Temperatura'])
        data_completa = data.split('/')
        mes = int(data_completa[1])
        
        while mesatual == mes:
            soma = soma + temp
            qntd = qntd + 1
            mesatual = mesatual + 1
            media = round(float(soma/qntd),2)
            MediaMensal.append(media)
    return MediaMensal
    
MediaFinal = Medias(dados)
print(MediaFinal)