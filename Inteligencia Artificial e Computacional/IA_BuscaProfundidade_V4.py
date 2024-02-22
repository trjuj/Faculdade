#Joao Lucas Mota Nogueira da Costa
#Joao Luis Chiarelotto Crema

import os
import copy
import random

mat = []

def menu():
    while True:
        os.system('cls')
        print("---------- MENU JUJ ----------\n")
        print("1 - Teste de Movimento")
        print("2 - Movimento")
        print("3 - Mostrar matriz")
        print("4 - Testar matriz")
        print("5 - Tenta resolver")
        print("0 - Sair\n")
        op = input("Op: ")

        if op == '1':
            os.system('cls')
            print("----- TESTE DE MOVIMENTO -----")
            mostra_mat(mat)
            val = input("\nValor: ")
            res = teste_mov(mat, val)
            if res == 1:
                print("Movimento possível para cima")
            elif res == 2:
                print("Movimento possível para baixo")
            elif res == 3:
                print("Movimento possível para esquerda")
            elif res == 4:
                print("Movimento possível para direita")
            elif res == 0:
                print("Nenhum movimento possível")
            input("Enter para prosseguir...")
        elif op == '2':
            os.system('cls')
            print("----- MOVIMENTO -----")
            mostra_mat(mat)
            val = input("\nValor: ")
            movimento(mat, val)
            os.system('cls')
            print("Movimento realizado\n")
            mostra_mat(mat)
            input("\nEnter para prosseguir...")
        elif op == '3':
            os.system('cls')
            mostra_mat(mat)
            input("\nEnter para prosseguir...")
        elif op == '4':
            os.system('cls')
            if testa_matriz(mat):
                print("Matriz correspondente")
            else:
                print("Matriz incorreta")
            input("\nEnter para prosseguir...")
        elif op == '5':
            os.system('cls')
            resolve()
        elif op == '0':
            break
        else:
            os.system('cls')
            print("Opção errada!")
            input("\nEnter para prosseguir...")
        os.system('cls')

def inicio():
    while True:
        os.system('cls')
        print("----- MATRIZ -----\n")
        print("1 - Matriz aleatória")
        print("2 - Matriz manual")
        print("0 - Sair\n")
        op = input("Op: ")

        if op == '1':
            os.system('cls')
            matriz_random()
            break
        elif op == '2':
            os.system('cls')
            cria_matriz()
            break
        elif op == '0':
            exit()
        else:
            os.system('cls')
            print("Escolha uma das opções.")
            input("\nEnter para prosseguir...")
    menu()

def cria_matriz():
    vet = ['1','2','3','4','5','6','7','8','-']
    for i in range(3):
        linha = []
        for j in range(3):
            print(f"\nEscolhas possíveis: {vet}")
            x = input(f"\nEscolha o número [{i}][{j}]: ")
            while x not in vet:
                print("Número inválido. Escolha novamente.")
                x = input(f"\nEscolha o número [{i}][{j}]: ")
            linha.append(x)
            vet.remove(str(x))
            os.system('cls')
        mat.append(linha)

def matriz_random():
    vet = ['1','2','3','4','5','6','7','8','-']
    for i in range(3):
        linha = []
        for j in range(3):
            x = random.choice(vet)
            linha.append(x)
            vet.remove(x)
        mat.append(linha)
    if matriz_solucionavel(mat):
        mostra_mat(mat)
        input("\nEnter para prosseguir...")
    else:
        for i in range(3):
            mat.pop()
        matriz_random()

def matriz_solucionavel(matriz):
    elementos = [elemento for linha in matriz for elemento in linha if elemento != '-']
    inversoes = 0

    for i in range(len(elementos)):
        for j in range(i + 1, len(elementos)):
            if elementos[i] > elementos[j]:
                inversoes += 1

    # Verifica se o número de inversões é par ou ímpar
    return inversoes % 2 == 0

def busca_index(matriz, val):
    for i in range(len(matriz)):
        if val in matriz[i]:
            return (i, matriz[i].index(val))

def busca_movs(matriz):
    movs = []
    pos = busca_index(matriz, '-')
    x = pos[0]
    y = pos[1]
    if x != 0:
        movs.append(matriz[x-1][y])
    if x != 2:
        movs.append(matriz[x+1][y])
    if y != 0:
        movs.append(matriz[x][y-1])
    if y != 2:
        movs.append(matriz[x][y+1])
    return movs

def mostra_mat(matriz):
    print("Matriz gerada:")
    for i in range(3):
        for j in range(3):
            print(matriz[i][j], end=' ')
        print()

def teste_mov(matriz, val):
    pos = busca_index(matriz, val)
    x = pos[0]
    y = pos[1]
    if matriz[x][y] == '-':
        return 0
    if x != 0 and matriz[x-1][y] == '-':
        return 1  # cima
    if x != 2 and matriz[x+1][y] == '-':
        return 2  # baixo
    if y != 0 and matriz[x][y-1] == '-':
        return 3  # esquerda
    if y != 2 and matriz[x][y+1] == '-':
        return 4  # direita

def movimento(matriz, val):
    tst = teste_mov(matriz, val)
    pos = busca_index(matriz, val)
    x = pos[0]
    y = pos[1]
    if tst == 1:
        matriz[x-1][y], matriz[x][y] = matriz[x][y], matriz[x-1][y]
    elif tst == 2:
        matriz[x+1][y], matriz[x][y] = matriz[x][y], matriz[x+1][y]
    elif tst == 3:
        matriz[x][y-1], matriz[x][y] = matriz[x][y], matriz[x][y-1]
    elif tst == 4:
        matriz[x][y+1], matriz[x][y] = matriz[x][y], matriz[x][y+1]

def testa_matriz(matriz):
    fim = [['-','1','2'],['3','4','5'],['6','7','8']]
    return matriz == fim

def resolve():
    # Converte a matriz para uma tupla de tuplas para facilitar o controle do estado
    estado_inicial = tuple(tuple(row) for row in mat)

    # Define o estado objetivo
    estado_objetivo = (('-', '1', '2'), ('3', '4', '5'), ('6', '7', '8'))

    # Inicializa a pilha de estados para a busca em profundidade
    pilha = [(estado_inicial, [])]

    # Inicializa um conjunto para rastrear estados visitados
    visitados = set()

    max_profundidade = 1000  # Defina uma profundidade máxima para a busca

    while pilha:
        estado_atual, caminho = pilha.pop()
        visitados.add(estado_atual)

        if len(caminho) > max_profundidade:
            continue  # Ignora estados além da profundidade máxima

        # Se o estado atual for igual ao estado objetivo, encontramos uma solução
        if estado_atual == estado_objetivo:
            print("----- RESOLUÇÃO -----")
            mostra_mat(list(estado_atual))
            print("\nSolução encontrada em", len(caminho), "passos.")
            input("Pressione Enter para prosseguir...")
            return

        # Encontra a posição do espaço vazio ('-')
        pos_vazio = busca_index(list(estado_atual), '-')
        linha_vazio, coluna_vazio = pos_vazio[0], pos_vazio[1]

        # Possíveis movimentos
        movimentos = [
            ('cima', linha_vazio - 1, coluna_vazio),
            ('baixo', linha_vazio + 1, coluna_vazio),
            ('esquerda', linha_vazio, coluna_vazio - 1),
            ('direita', linha_vazio, coluna_vazio + 1)
        ]

        for movimento, linha, coluna in movimentos:
            if 0 <= linha < 3 and 0 <= coluna < 3:
                # Cria um novo estado após o movimento
                novo_estado = tuple(tuple(row) for row in estado_atual)
                novo_estado = troca_elementos(novo_estado, (linha_vazio, coluna_vazio), (linha, coluna))

                if novo_estado not in visitados:
                    novo_caminho = caminho + [movimento]
                    pilha.append((novo_estado, novo_caminho))

    # Se chegamos aqui, não foi encontrada uma solução
    print("Não foi encontrada uma solução dentro da profundidade máxima.")
    input("Pressione Enter para prosseguir...")

def troca_elementos(matriz, pos1, pos2):
    matriz_lista = list(list(row) for row in matriz)
    matriz_lista[pos1[0]][pos1[1]], matriz_lista[pos2[0]][pos2[1]] = matriz_lista[pos2[0]][pos2[1]], matriz_lista[pos1[0]][pos1[1]]
    return tuple(tuple(row) for row in matriz_lista)

#---------------------------------------------------------------------------------------------------------

inicio()