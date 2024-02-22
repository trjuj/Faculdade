#PBL IV-A João Lucas Mota Nogueira da Costa - Engenharia Boyle
import pandas as pd

dados = pd.read_csv('DadosClimaticos2018Londrina.csv',sep=';')

k = 1
while k == 1: # Variável que determina o final do programa
    Op = int(input('Opção 1: Lista das médias de temperatura de cada mês do ano. \nOpção 2: Lista das médias de umidade relativa de cada mês do ano. \nOpção 3: Lista dos meses com temperatura média acima do valor escolhida. \nOpção 4: Lista dos meses com umidade relativa abaixo do valor escolhido. \nOpção 5: Finalizar o programa. \nDigite aqui a opção desejada: '))
    if Op == 1:
        def MediasTemp(tabela): # Função da primeira opção
            TempMensal = []
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
                    TempMensal.append(media)
            return TempMensal
        T = MediasTemp(dados)
        print('Médias das temperaturas de cada mês: ',T)

    elif Op == 2:
        def MediasUmid(tabela): # Função da segunda opção
            UmidMensal = []
            soma = 0
            qntd = 0
            mesatual = 1
            for i in range(len(tabela)):
                linha = tabela.iloc[i]
                data = linha['Data']
                umid = float(linha['Umidade'])
                data_completa = data.split('/')
                mes = int(data_completa[1])
                
                while mesatual == mes:
                    soma = soma + umid
                    qntd = qntd + 1
                    mesatual = mesatual + 1
                    media = round(float(soma/qntd),2)
                    UmidMensal.append(media)
            return UmidMensal
        U = MediasUmid(dados)
        print('Médias das umidades relativas de cada mês: ',U)
    
    elif Op == 3:
        def TempAcima(tabela,lista): # Função da terceira opção
            Meses = []
            x = float(input('Digite a temperatura média: '))
            if x < T[0]:
                Meses.append('Janeiro')
            if x < T[1]:
                Meses.append('Fevereiro')
            if x < T[2]:
                Meses.append('Março')
            if x < T[3]:
                Meses.append('Abril')
            if x < T[4]:
                Meses.append('Maio')
            if x < T[5]:
                Meses.append('Junho')
            if x < T[6]:
                Meses.append('Julho')
            if x < T[7]:
                Meses.append('Agosto')
            if x < T[8]:
                Meses.append('Setembro')
            if x < T[9]:
                Meses.append('Outubro')
            if x < T[10]:
                Meses.append('Novembro')
            if x < T[11]:
                Meses.append('Dezembro')
            return Meses

        C = TempAcima(dados,T)
        print('Os meses com a temperatura média acima do valor selecionado são: ',C)
        
    elif Op == 4:
        def UmidAbaixo(tabela,lista): # Função da quarta opção
            Meses = []
            x = float(input('Digite a umidade média: '))
            if x > U[0]:
                Meses.append('Janeiro')
            if x > U[1]:
                Meses.append('Fevereiro')
            if x > U[2]:
                Meses.append('Março')
            if x > U[3]:
                Meses.append('Abril')
            if x > U[4]:
                Meses.append('Maio')
            if x > U[5]:
                Meses.append('Junho')
            if x > U[6]:
                Meses.append('Julho')
            if x > U[7]:
                Meses.append('Agosto')
            if x > U[8]:
                Meses.append('Setembro')
            if x > U[9]:
                Meses.append('Outubro')
            if x > U[10]:
                Meses.append('Novembro')
            if x > U[11]:
                Meses.append('Dezembro')
            return Meses
        
        S = UmidAbaixo(dados,U)
        print('Os meses com a umidade relativa abaixo do valor selecionado são: ',S)
        
    elif Op == 5: # Opção de finalização do programa
        print('Finalizando o programa...')
        k = k + 1
        
    elif Op != [1,2,3,4,5]: # Erro caso o número inserido seja diferente das opções disponíveis
        print('ERROR 404: NOT FOUND')