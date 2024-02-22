import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

dados = pd.read_csv('si_env-2019 2.0.csv',encoding='ISO-8859-1',sep=';')


def media_idade_mes(dataframe): #funçao para calculo da media de idades por mes 
    dados['Mes'] = pd.DatetimeIndex(dados['data_boletim'], dayfirst=True).month #separando o mes e criando uma nova coluna 
    dados.to_csv('novo.csv',sep = ';', index = False) #novo arquivo com a coluna mes 
    return pd.DataFrame(dataframe.groupby('Mes')['idades'].mean()).reset_index()  #calculo da media das idades por mês 
#print(media_idade_mes(dados))


def vitimas(dados): #funçao para calculo da quantidade de acidentes nao fatal por mes
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
    
    for i in range(len(dados)):
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

def alcool(dados): #funçao para quantidade de vitimas com alcool no sangue por mes 
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
    
    for i in range(len(dados)):
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

def cinto(dados): #funçao para calcular a quantidade de vitimas sem cinto de segurança 
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
        
    for i in range(len(dados)):
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


def tipo_de_veiculo(dados): #funçao que calcula a quantidade de determinado veiculo
    qtdeMOTO = 0
    qtdeAUTO = 0
    qtdeMOTONE = 0
    qtdeBICI = 0
    qtdeONIBUS = 0
    qtdeCAMINHONETE = 0
    qtdeCAMINHAO = 0
    qtdeNAO = 0
    qtdeCAMIONETA = 0
    qtdeCAMINHAOTRATOR = 0
    qtdeMICRO = 0
    qtdeTRATOR = 0
    qtdeCARROCA = 0
    qtdeKOMBI = 0
    qtdeBONDE = 0
    qtdeESPECIAL = 0
    qtdeCARRODEMAO = 0
    qtdeREBOQUE = 0
    qtdeTRICICLO = 0
    qtdePATINETE = 0
    qtdeCHARRETE = 0
    qtdeTAXI = 0
    qtdeCICLOMOTOR = 0
    qtdeTRACAO = 0
    tipos=[]
    for i in range (len(dados)):   
       linha = dados.iloc[i]
       especie = linha['especie_veiculo']
    
       if especie == 'MOTOCICLETA':
            qtdeMOTO = qtdeMOTO + 1

       if especie == 'AUTOMOVEL':
            qtdeAUTO = qtdeAUTO + 1
    
       if especie == 'MOTONETA':
            qtdeMOTONE = qtdeMOTONE + 1
    
       if especie == 'BICICLETA':
            qtdeBICI = qtdeBICI + 1
        
       if especie == 'ONIBUS':
            qtdeONIBUS = qtdeONIBUS + 1
        
       if especie == 'CAMINHONETE':
             qtdeCAMINHONETE = qtdeCAMINHONETE + 1
         
       if especie == 'CAMINHAO':
             qtdeCAMINHAO = qtdeCAMINHAO + 1
        
       if especie == 'NAOINFORMADO':
             qtdeNAO = qtdeNAO + 1
        
       if especie == 'CAMIONETA':
             qtdeCAMIONETA = qtdeCAMIONETA + 1
    
       if especie == 'CAMINHAO-TRATOR':
             qtdeCAMINHAOTRATOR = qtdeCAMINHAOTRATOR + 1
        
       if especie == 'MICROONIBUS':
             qtdeMICRO = qtdeMICRO + 1
        
       if especie == 'TRATORDERODAS':
             qtdeTRATOR = qtdeTRATOR + 1
        
       if especie == 'CARROCA':
             qtdeCARROCA = qtdeCARROCA + 1
        
       if especie == 'KOMBI':
             qtdeKOMBI = qtdeKOMBI + 1
         
       if especie == 'BONDE':
             qtdeBONDE = qtdeBONDE + 1
        
       if especie == 'ESPECIAL':
             qtdeESPECIAL = qtdeESPECIAL + 1
        
       if especie == 'CARRODEMAO':
             qtdeCARRODEMAO = qtdeCARRODEMAO + 1
        
       if especie == 'REBOQUEESEMI-REBOQUE':
             qtdeREBOQUE = qtdeREBOQUE + 1
        
       if especie == 'TRICICLO':
             qtdeTRICICLO = qtdeTRICICLO + 1
        
       if especie == 'PATINETE':
             qtdePATINETE = qtdePATINETE + 1
         
       if especie == 'CHARRETE':
             qtdeCHARRETE = qtdeCHARRETE + 1
        
       if especie == 'TAXI':
             qtdeTAXI = qtdeTAXI + 1
        
       if especie == 'CICLOMOTOR':
             qtdeCICLOMOTOR = qtdeCICLOMOTOR + 1
        
       if especie == 'TRACAO':
             qtdeTRACAO = qtdeTRACAO + 1
    tipos.append(qtdeMOTO)
    tipos.append(qtdeAUTO)
    tipos.append(qtdeMOTONE)
    tipos.append(qtdeBICI)
    tipos.append(qtdeONIBUS)
    tipos.append(qtdeCAMINHONETE)
    tipos.append(qtdeCAMINHAO)
    tipos.append(qtdeNAO)
    tipos.append(qtdeCAMIONETA)
    tipos.append(qtdeCAMINHAOTRATOR)
    tipos.append(qtdeMICRO)
    tipos.append(qtdeTRATOR)
    tipos.append(qtdeCARROCA)
    tipos.append(qtdeKOMBI)
    tipos.append(qtdeBONDE)
    tipos.append(qtdeESPECIAL)
    tipos.append(qtdeCARRODEMAO)
    tipos.append(qtdeREBOQUE)
    tipos.append(qtdeTRICICLO)
    tipos.append(qtdePATINETE)
    tipos.append(qtdeCHARRETE)
    tipos.append(qtdeTAXI)
    tipos.append(qtdeCICLOMOTOR)
    tipos.append(qtdeTRACAO)
    return tipos
        
        
        
def boletim_acidentes(dados): #funçao que calcla a quantidade de acidentes por mes 
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
    for i in range(len(dados)):
        linha = dados.iloc[i]
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
        

while True:
    print('..........................................................')
    print('0 - Finalizar o programa')
    print('1 - Idade média mensal das pessoas que sofreram acidentes (grafico de linha)')
    print('2 - Acontecimentos de feridos, motoristas embriagados e não uso de cinto de segurança (grafico de linha)')
    print('3 - Número de casos por espécies de carro em 2019 (histograma)')
    print('4 - Número de acidentes por mês em 2019 (histograma)')
    print('.........................................................')

    y = int(input('Digite uma opção entre 0 e 4: '))

    if y == 0:
      print('Tenha um bom dia!')
      break
    elif y == 1:
      mes_escolhido_inicial = int(input('Em qual mes o grafico ira começar?: '))
      mes_escolhido_final = int(input('Em qual mes o grafico ira terminar?: '))
      tabela = media_idade_mes(dados).iloc[mes_escolhido_inicial-1:mes_escolhido_final]
      plt.plot(tabela['Mes'], tabela['idades'], marker='o', color='c')
      plt.ylim(33) 
      plt.xticks(np.arange(mes_escolhido_inicial,mes_escolhido_final +1, 1.0))
      plt.title("Idade média mensal das pessoas que sofreram acidentes")
      plt.xlabel('Mês') 
      plt.ylabel('idade Média') 
      plt.grid()
      plt.show() 
    elif y == 2:
      data_inicial = int(input('Em qual mês o grafico deve começar?: '))
      data_final = int(input('Em qual mês o grafico deve terminar?: '))
      a = data_inicial - 1
      b = data_final
      if data_inicial >= b:
          print('Intervalo de tempo inválido.')
      else:
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
          plt.show() 
    elif y == 3:
      cor = input('Qual a cor (b,g,r,c,m,y,k) do histograma?')
      fig = plt.figure(figsize=(22,8))
      ax = fig.add_axes([0,0,1,1])
      especies = ['Motocicleta', 'Automovel', 'Motoneta', 'Bicicleta', 'Onibus', 'Caminhonete', 'Caminhao', 'Nao Informado', 'Camioneta', 'Caminhao-Trator', 'Microonibus', 'Trator', 'Carroça', 'Kombi', 'Bonde', 'Especial', 'Carro de mao', 'Reboque', 'Triciclo', 'Patinete', 'Charrete', 'Taxi', 'Ciclomotor', 'Traçao',]
      ax.bar(especies,tipo_de_veiculo(dados),width=0.64,color=cor)
      plt.ylabel('Número de casos')
      plt.title('Número de casos por espécies de carro em 2019')
      plt.show()
    elif y == 4:
      cor = input('Qual a cor (b,g,r,c,m,y,k) do histograma?')
      fig = plt.figure(figsize=(5,5))
      meses = ['Jan','Fev','Mar','Abr','Mai','Jun','Jul','Ago','Set','Out','Nov','Dez']
      plt.title('Número de acidentes por mês no ano de 2019')
      ax = fig.add_axes([0,0,1,1])
      ax.bar(meses,funcao,width=0.64,color=cor)
      plt.ylabel('Número de Acidentes')
      plt.title('Número de acidentes por mês em 2019')
      plt.show()
    else:
        print('Numero invalido!')