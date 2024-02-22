# PBL IV B João Lucas Mota Nogueira da Costa - Engenharia Boyle

import pandas as pd
import matplotlib.pyplot as plt

dados = pd.read_csv('DadosClimaticos2018Londrina.csv',sep=';')

def Medias(tabela):
    MediaMensal = []
    soma = 0
    qntd = 0
    mesatual = 1
    for i in range(len(tabela)):
        linha = tabela.iloc[i]
        data = linha['Data']
        temp = int(float(linha['Temperatura']))
        data_completa = data.split('/')
        mes = int(data_completa[1])
        
        while mesatual == mes:
            soma = soma + temp
            qntd = qntd + 1
            mesatual = mesatual + 1
            media = round(float(soma/qntd),2)
            MediaMensal.append(media)
    print('Gráfico das médias mensais de temperatura')
    return MediaMensal
    
MediaFinal = Medias(dados)

fig1 = plt.figure(figsize=(12,12))
plt.plot(['Janeiro','Fevereiro','Março','Abril','Maio','Junho','Julho','Agosto','Setembro','Outubro','Novembro','Dezembro'],MediaFinal)
plt.title('João Lucas Mota Nogueira da Costa')
plt.xlabel('Meses', fontsize='x-large')
plt.ylabel('Média de Temperatura', fontsize='x-large')
plt.ylim(20,30)
plt.show()

#--------------------------------------------------------------------------------------------------------------------------------------

m = int(input('Digite o mês desejado (Janeiro = 1, Fevereiro = 2 ...) : '))

if m in range(1,13):

    def Umidade (mes_escolhido,tabela):
        Umidades = []
        for i in range(len(tabela)):
            linha = tabela.iloc[i]
            data = linha['Data']
            umid = linha['Umidade']
            data_completa = data.split('/')
            mes = int(data_completa[1])
            
            if mes_escolhido == mes:
                Umidades.append(umid)
        print('\nHistograma das ocorrências da umidade do ar no mês selecionado')
        return Umidades
    
    UmidadesFinal = Umidade(m,dados)
    
    plt.hist(UmidadesFinal, bins = 100)
    plt.show()
else:
    print('Número inválido')