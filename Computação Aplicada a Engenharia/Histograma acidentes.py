import pandas as pd
import matplotlib.pyplot as plt

dados = pd.read_csv('si_env-2019.csv',encoding='ISO-8859-1',sep=';')

#------------------------------------------------------------------------------------
# Entrada de dados

cor_ops = int(input('Opções de cor: \nOpção 1: Vermelho \nOpção 2: Verde \nOpção 3: Azul \nDigite a opção referente a cor desejada para os gráficos de barras: '))
    
#------------------------------------------------------------------------------------
# Função

def acidentes(tabela):
    qnt01 = 0
    qnt02 = 0
    qnt03 = 0
    qnt04 = 0
    qnt05 = 0
    qnt06 = 0
    qnt07 = 0
    qnt08 = 0
    qnt09 = 0
    qnt10 = 0
    qnt11 = 0
    qnt12 = 0
    casos_por_mes = []
    for i in range(len(tabela)):
        linha = tabela.iloc[i]
        data = linha['data_boletim']
        data_completa = data.split('/')
        mes = int(data_completa[1])
        if mes == 1:
            qnt01 = qnt01 + 1
        if mes == 2:
            qnt02 = qnt02 + 1
        if mes == 3:
            qnt03 = qnt03 + 1
        if mes == 4:
            qnt04 = qnt04 + 1
        if mes == 5:
            qnt05 = qnt05 + 1
        if mes == 6:
            qnt06 = qnt06 + 1
        if mes == 7:
            qnt07 = qnt07 + 1
        if mes == 8:
            qnt08 = qnt08 + 1
        if mes == 9:
            qnt09 = qnt09 + 1
        if mes == 10:
            qnt10 = qnt10 + 1
        if mes == 11:
            qnt11 = qnt11 + 1
        if mes == 12:
            qnt12 = qnt12 + 1
            
    casos_por_mes.append(qnt01)
    casos_por_mes.append(qnt02)
    casos_por_mes.append(qnt03)
    casos_por_mes.append(qnt04)
    casos_por_mes.append(qnt05)
    casos_por_mes.append(qnt06)
    casos_por_mes.append(qnt07)
    casos_por_mes.append(qnt08)
    casos_por_mes.append(qnt09)
    casos_por_mes.append(qnt10)
    casos_por_mes.append(qnt11)
    casos_por_mes.append(qnt12)
    return casos_por_mes
funcao = acidentes(dados)

#------------------------------------------------------------------------------------
# Gráfico

fig = plt.figure(figsize=(12,12))
meses = ['Janeiro','Fevereiro','Março','Abril','Maio','Junho','Julho','Agosto','Setembro','Outubro','Novembro','Dezembro']
ax = fig.add_axes([0,0,1,1])
plt.title('Número de acidentes por mês ocorridos no ano de 2019')
plt.ylabel('Número de Acidentes')
width = 0.6
if cor_ops == 1:
    ax.bar(meses,funcao,color='red')
elif cor_ops == 2:
    ax.bar(meses,funcao,color='green')
elif cor_ops == 3:
    ax.bar(meses,funcao,color='blue')
plt.show()