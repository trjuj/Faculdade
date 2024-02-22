import pandas as pd
import matplotlib.pyplot as plt

dados = pd.read_csv('si_env-2019.csv', encoding='ISO-8859-1', sep=';')

cor_ops = int(input('Opções de cor: \nOpção 1: Vermelho \nOpção 2: Verde \nOpção 3: Azul \nDigite a opção referente a cor desejada para os gráficos de barras: '))

# Função

def boletim_acidentes(tabela):
    qnt1 = 0
    qnt2 = 0
    qnt3 = 0
    qnt4 = 0
    qnt5 = 0
    qnt6 = 0
    qnt7 = 0
    qnt8 = 0
    qnt9 = 0
    qnt10 = 0
    qnt11 = 0
    qnt12 = 0
    acidentes_por_mes = []
    for i in range(len(tabela)):
        linha = tabela.iloc[i]
        data = linha['data_boletim']
        data_completa = data.split('/')
        mes = int(data_completa[1])
        if mes == 1:
            qnt1 = qnt1 + 1
        if mes == 2:
            qnt2 = qnt2 + 1
        if mes == 3:
            qnt3 = qnt3 + 1
        if mes == 4:
            qnt4 = qnt4 + 1
        if mes == 5:
            qnt5 = qnt5 + 1
        if mes == 6:
            qnt6 = qnt6 + 1
        if mes == 7:
            qnt7 = qnt7 + 1
        if mes == 8:
            qnt8 = qnt8 + 1
        if mes == 9:
            qnt9 = qnt9 + 1
        if mes == 10:
            qnt10 = qnt10 + 1
        if mes == 11:
            qnt11 = qnt11 + 1
        if mes == 12:
            qnt12 = qnt12 + 1
            
    acidentes_por_mes.append(qnt1)
    acidentes_por_mes.append(qnt2)
    acidentes_por_mes.append(qnt3)
    acidentes_por_mes.append(qnt4)
    acidentes_por_mes.append(qnt5)
    acidentes_por_mes.append(qnt6)
    acidentes_por_mes.append(qnt7)
    acidentes_por_mes.append(qnt8)
    acidentes_por_mes.append(qnt9)
    acidentes_por_mes.append(qnt10)
    acidentes_por_mes.append(qnt11)
    acidentes_por_mes.append(qnt12)
    return acidentes_por_mes
funcao = boletim_acidentes(dados)

# Gráfico

fig = plt.figure(figsize=(7,7))
meses = ['Jan','Fev','Mar','Abr','Mai','Jun','Jul','Ago','Set','Out','Nov','Dez']
ax = fig.add_axes([0,0,1,1])
width = 0.64
if cor_ops == 1:
    ax.bar(meses,funcao,color='red')
elif cor_ops == 2:
    ax.bar(meses,funcao,color='green')
elif cor_ops == 3:
    ax.bar(meses,funcao,color='blue')
plt.title('Número de acidentes por mês no ano de 2019')
plt.ylabel('Número de Acidentes')
plt.show()
