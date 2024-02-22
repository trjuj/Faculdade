from collections import deque

# Representação do estado do quebra-cabeça como uma lista de listas
# O número 0 representa o espaço vazio
estado_objetivo = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]

def expandir_estado(estado):
    # Encontra a posição do espaço vazio
    for i in range(3):
        for j in range(3):
            if estado[i][j] == 0:
                vazio_i, vazio_j = i, j
    
    sucessores = []
    
    # Movimentos possíveis: acima, abaixo, esquerda, direita
    movimentos = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    for movimento in movimentos:
        novo_i = vazio_i + movimento[0]
        novo_j = vazio_j + movimento[1]
        
        if 0 <= novo_i < 3 and 0 <= novo_j < 3:
            novo_estado = [linha.copy() for linha in estado]
            novo_estado[vazio_i][vazio_j], novo_estado[novo_i][novo_j] = novo_estado[novo_i][novo_j], novo_estado[vazio_i][vazio_j]
            sucessores.append(novo_estado)
    return sucessores

def busca_em_largura(estado_inicial):
    fila = deque([(estado_inicial, [])])
    visitados = set()
    
    while fila:
        estado_atual, acoes = fila.popleft()
        
        if estado_atual == estado_objetivo:
            return acoes
        
        visitados.add(tuple(tuple(row) for row in estado_atual))
        
        for prox_estado in expandir_estado(estado_atual):
            if tuple(tuple(row) for row in prox_estado) not in visitados:
                fila.append((prox_estado, acoes + [prox_estado]))
                visitados.add(tuple(tuple(row) for row in prox_estado))
    return None

def imprimir_estado(estado):
    for linha in estado:
        print(' '.join(map(str, linha)))

# Solicita ao usuário inserir o estado inicial como uma lista de listas
estado_inicial = []
print("Insira o estado inicial (uma linha de cada vez, usando espaços como separadores):")
for _ in range(3):
    linha = list(map(int, input().split()))
    estado_inicial.append(linha)

print("\nEstado Inicial:")
imprimir_estado(estado_inicial)

acoes_solucao = busca_em_largura(estado_inicial)

if acoes_solucao:
    print("\nSolução encontrada em", len(acoes_solucao), "passos:")
    for i, estado in enumerate(acoes_solucao):
        print("\nPasso", i+1)
        imprimir_estado(estado)
else:
    print("\nNão foi encontrada uma solução.")