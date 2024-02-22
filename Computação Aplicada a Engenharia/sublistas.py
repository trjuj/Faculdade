import pandas as pd

dados = pd.read_csv('DadosClimaticos2018Londrina.csv',sep=';')

def Medias(tabela):
    MediaMensal = []
    soma = 0
    qntd = 0
    mesatual = 1
    for y in range(len(dados)):
        lin = dados.iloc[y]
        data_completa = lin['Data']
        mes = data_completa[3:5]
    
        while mesatual == mes:
            for i in range(len(tabela)):
                linha = tabela.iloc[i]
                temp = linha['Temperatura']
                qntd = qntd + 1
                soma = soma + temp
                MediaMensal.append(soma/qntd)
                mesatual = mesatual + 1
                soma = 0
                qntd = 0
        return MediaMensal

MediasFinal = Medias(dados)
print(MediasFinal)