import matplotlib.pyplot as plt
import pandas as pd

dados = pd.read_csv('si_env-2019.csv',encoding='ISO-8859-1',sep=';')

#-----------------------------------------------------------------------------------------------
# Entrada de dados

data_inicial = int(input('Em qual mês o grafico deve começar?: '))
data_final = int(input('Em qual mês o grafico deve terminar?: '))
a = data_inicial - 1
b = data_final
if data_inicial >= b:
    print('Intervalo de tempo inválido.')
elif data_inicial >= 13 or data_final >= 13 or data_inicial <= 0 or data_final <= 0:
    print('Digite um número entre 1 e 12 equivalente ao mês desejado')
else:

#-----------------------------------------------------------------------------------------------
# Funções
    
    def vitimas(tabela):
        vit01 = 0
        vit02 = 0
        vit03 = 0
        vit04 = 0
        vit05 = 0
        vit06 = 0
        vit07 = 0
        vit08 = 0
        vit09 = 0
        vit10 = 0
        vit11 = 0
        vit12 = 0
        vit_por_mes = []
        
        for i in range(len(tabela)):
            linha = dados.iloc[i]
            data = linha['data_boletim']
            data_completa = data.split('/')
            mes = int(data_completa[1])
            
            if mes == 1:
                if linha[' desc_severidade'] == ('NAO FATAL      '):
                    vit01 = vit01 + 1
            if mes == 2:
                if linha[' desc_severidade'] == ('NAO FATAL      '):
                    vit02 = vit02 + 1
            if mes == 3:
                if linha[' desc_severidade'] == ('NAO FATAL      '):
                    vit03 = vit03 + 1
            if mes == 4:
                if linha[' desc_severidade'] == ('NAO FATAL      '):
                    vit04 = vit04 + 1
            if mes == 5:
                if linha[' desc_severidade'] == ('NAO FATAL      '):
                    vit05 = vit05 + 1
            if mes == 6:
                if linha[' desc_severidade'] == ('NAO FATAL      '):
                    vit06 = vit06 + 1
            if mes == 7:
                if linha[' desc_severidade'] == ('NAO FATAL      '):
                    vit07 = vit07 + 1
            if mes == 8:
                if linha[' desc_severidade'] == ('NAO FATAL      '):
                    vit08 = vit08 + 1
            if mes == 9:
                if linha[' desc_severidade'] == ('NAO FATAL      '):
                    vit09 = vit09 + 1
            if mes == 10:
                if linha[' desc_severidade'] == ('NAO FATAL      '):
                    vit10 = vit10 + 1
            if mes == 11:
                if linha[' desc_severidade'] == ('NAO FATAL      '):
                    vit11 = vit11 + 1
            if mes == 12:
                if linha[' desc_severidade'] == ('NAO FATAL      '):
                    vit12 = vit12 + 1
                    
        vit_por_mes.append(vit01)
        vit_por_mes.append(vit02)
        vit_por_mes.append(vit03)
        vit_por_mes.append(vit04)
        vit_por_mes.append(vit05)
        vit_por_mes.append(vit06)
        vit_por_mes.append(vit07)
        vit_por_mes.append(vit08)
        vit_por_mes.append(vit09)
        vit_por_mes.append(vit10)
        vit_por_mes.append(vit11)
        vit_por_mes.append(vit12)
        
        return vit_por_mes
    funcao1 = vitimas(dados)
    
    def alcool(tabela):
        alc01 = 0
        alc02 = 0
        alc03 = 0
        alc04 = 0
        alc05 = 0
        alc06 = 0
        alc07 = 0
        alc08 = 0
        alc09 = 0
        alc10 = 0
        alc11 = 0
        alc12 = 0
        alc_por_mes = []
        
        for i in range(len(tabela)):
            linha = dados.iloc[i]
            data = linha['data_boletim']
            data_completa = data.split('/')
            mes = int(data_completa[1])
            
            if mes == 1:
                if linha[' Embreagues'] == ('SIM'):
                    alc01 = alc01 + 1
            if mes == 2:
                if linha[' Embreagues'] == ('SIM'):
                    alc02 = alc02 + 1
            if mes == 3:
                if linha[' Embreagues'] == ('SIM'):
                    alc03 = alc03 + 1
            if mes == 4:
                if linha[' Embreagues'] == ('SIM'):
                    alc04 = alc04 + 1
            if mes == 5:
                if linha[' Embreagues'] == ('SIM'):
                    alc05 = alc05 + 1
            if mes == 6:
                if linha[' Embreagues'] == ('SIM'):
                    alc06 = alc06 + 1
            if mes == 7:
                if linha[' Embreagues'] == ('SIM'):
                    alc07 = alc07 + 1
            if mes == 8:
                if linha[' Embreagues'] == ('SIM'):
                    alc08 = alc08 + 1
            if mes == 9:
                if linha[' Embreagues'] == ('SIM'):
                    alc09 = alc09 + 1
            if mes == 10:
                if linha[' Embreagues'] == ('SIM'):
                    alc10 = alc10 + 1
            if mes == 11:
                if linha[' Embreagues'] == ('SIM'):
                    alc11 = alc11 + 1
            if mes == 12:
                if linha[' Embreagues'] == ('SIM'):
                    alc12 = alc12 + 1
        
        alc_por_mes.append(alc01)
        alc_por_mes.append(alc02)
        alc_por_mes.append(alc03)
        alc_por_mes.append(alc04)
        alc_por_mes.append(alc05)
        alc_por_mes.append(alc06)
        alc_por_mes.append(alc07)
        alc_por_mes.append(alc08)
        alc_por_mes.append(alc09)
        alc_por_mes.append(alc10)
        alc_por_mes.append(alc11)
        alc_por_mes.append(alc12)
        
        return alc_por_mes
    funcao2 = alcool(dados)
    
    def cinto(tabela):
        cin01 = 0
        cin02 = 0
        cin03 = 0
        cin04 = 0
        cin05 = 0
        cin06 = 0
        cin07 = 0
        cin08 = 0
        cin09 = 0
        cin10 = 0
        cin11 = 0
        cin12 = 0
        cin_por_mes = []
            
        for i in range(len(tabela)):
            linha = dados.iloc[i]
            data = linha['data_boletim']
            data_completa = data.split('/')
            mes = int(data_completa[1])
            if mes == 1:
                if linha[' cinto_seguranca'] == ('NÃO'):
                    cin01 = cin01 + 1
            if mes == 2:
                if linha[' cinto_seguranca'] == ('NÃO'):
                    cin02 = cin02 + 1
            if mes == 3:
                if linha[' cinto_seguranca'] == ('NÃO'):
                    cin03 = cin03 + 1
            if mes == 4:
                if linha[' cinto_seguranca'] == ('NÃO'):
                        cin04 = cin04 + 1
            if mes == 5:
                if linha[' cinto_seguranca'] == ('NÃO'):
                    cin05 = cin05 + 1
            if mes == 6:
                if linha[' cinto_seguranca'] == ('NÃO'):
                    cin06 = cin06 + 1
            if mes == 7:
                if linha[' cinto_seguranca'] == ('NÃO'):
                    cin07 = cin07 + 1
            if mes == 8:
                if linha[' cinto_seguranca'] == ('NÃO'):
                    cin08 = cin08 + 1
            if mes == 9:
                if linha[' cinto_seguranca'] == ('NÃO'):
                    cin09 = cin09 + 1
            if mes == 10:
                if linha[' cinto_seguranca'] == ('NÃO'):
                    cin10 = cin10 + 1
            if mes == 11:
                if linha[' cinto_seguranca'] == ('NÃO'):
                    cin11 = cin11 + 1
            if mes == 12:
                if linha[' cinto_seguranca'] == ('NÃO'):
                    cin12 = cin12 + 1
        
        cin_por_mes.append(cin01)
        cin_por_mes.append(cin02)
        cin_por_mes.append(cin03)
        cin_por_mes.append(cin04)
        cin_por_mes.append(cin05)
        cin_por_mes.append(cin06)
        cin_por_mes.append(cin07)
        cin_por_mes.append(cin08)
        cin_por_mes.append(cin09)
        cin_por_mes.append(cin10)
        cin_por_mes.append(cin11)
        cin_por_mes.append(cin12)
        return cin_por_mes
    funcao3 = cinto(dados)
    
#-----------------------------------------------------------------------------------------------
# Gráfico
    
    fig = plt.figure(figsize=(12,12))
    meses = ['Janeiro','Fevereiro','Março','Abril','Maio','Junho','Julho','Agosto','Setembro','Outubro','Novembro','Dezembro']
    plt.plot(meses[a:b], funcao1[a:b], color = 'red', label = 'Feridos')
    plt.plot(meses[a:b], funcao2[a:b], color = 'blue', label = 'Embriagados')
    plt.plot(meses[a:b], funcao3[a:b], color = 'green', label = 'Sem cinto')
    plt.grid(True)
    plt.ylim(0,1600)
    plt.legend()
    plt.title('Acontecimentos de feridos, motoristas embriagados e não uso de cinto de segurança')
    plt.ylabel('Número de Acontecimentos')