def acha_celula_mais_restrita(board):
    # Encontre a próxima célula vazia no tabuleiro com MRV (Most Restricted Variable)
    min_tamanho_dominio = float('inf')
    cel_mais_restrita = None

    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                # Calcula o tamanho do domínio (número de valores possíveis) para a célula
                tamanho_dominio = len(get_valores_possiveis(board, row, col))
                if tamanho_dominio < min_tamanho_dominio:
                    min_tamanho_dominio = tamanho_dominio
                    cel_mais_restrita = (row, col)

    return cel_mais_restrita

def get_valores_possiveis(board, row, col):
    # Obtenha os valores possíveis para preencher a célula (row, col)
    valores = set(range(1, 10))

    for i in range(9):
        # Remova valores da mesma linha e coluna
        valores.discard(board[row][i])
        valores.discard(board[i][col])

    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            # Remova valores do bloco 3x3
            valores.discard(board[i][j])

    return list(valores)

def soma_restricoes_futuras(board, row, col, num):
    # Conta o numero de restricoes futuras se 'num' for atribuido a celula
    board[row][col] = num  # Atribua temporariamente 'num' a celula

    # Calcule o número total de restricões futuras
    total_restricoes = 0
    for i in range(9):
        if board[row][i] == 0:
            total_restricoes += len(get_valores_possiveis(board, row, i)) - 1
        if board[i][col] == 0:
            total_restricoes += len(get_valores_possiveis(board, i, col)) - 1

    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if board[i][j] == 0:
                total_restricoes += len(get_valores_possiveis(board, i, j)) - 1

    board[row][col] = 0  # Reverta a atribuicao temporaria

    return total_restricoes

def resolve(board, usa_gula=True):
    celula_vazia = acha_celula_mais_restrita(board)

    if not celula_vazia:
        return True  # O tabuleiro esta completamente preenchido

    row, col = celula_vazia

    if usa_gula:
        valores_possiveis = get_valores_possiveis(board, row, col)
        # Ordena os valores possiveis com base no numero de restricoes futuras
        valores_possiveis.sort(key=lambda num: soma_restricoes_futuras(board, row, col, num))

    else:
        valores_possiveis = get_valores_possiveis(board, row, col)

    for num in valores_possiveis:
        board[row][col] = num

        if resolve(board, usa_gula):
            return True

        board[row][col] = 0  # Reverta a atribuicao se a solucao nao for encontrada

    return False  # Retorna False se nao houver solucao

# Funcao para imprimir o tabuleiro
def print_board(board):
    for row in board:
        print(" ".join(map(str, row)))

# Problema 1
board1 = [
    [0, 0, 9, 0, 0, 0, 5, 0, 0],
    [0, 8, 0, 0, 0, 0, 0, 6, 0],
    [7, 0, 0, 8, 0, 4, 0, 0, 1],
    [0, 0, 4, 0, 2, 0, 3, 0, 0],
    [0, 0, 0, 5, 9, 8, 0, 0, 0],
    [0, 0, 2, 0, 6, 0, 9, 0, 0],
    [3, 0, 0, 6, 0, 9, 0, 0, 5],
    [0, 6, 0, 0, 0, 0, 0, 2, 0],
    [0, 0, 5, 0, 0, 0, 4, 0, 0]
]

print("\nProblema 1:\n")
if resolve(board1, usa_gula=True):
    print_board(board1)
else:
    print("\nNao ha solucao para o problema 1.")

# Problema 2
board2 = [
    [0, 0, 0, 0, 2, 0, 3, 4, 0],
    [2, 9, 0, 0, 0, 0, 0, 5, 0],
    [5, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 6, 0, 8, 9, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 8],
    [0, 0, 6, 5, 0, 4, 0, 0, 0],
    [0, 0, 0, 0, 0, 2, 0, 0, 6],
    [0, 2, 0, 0, 0, 0, 0, 8, 9],
    [0, 5, 7, 0, 8, 0, 0, 0, 0]
]

print("\nProblema 2:\n")
if resolve(board2, usa_gula=True):
    print_board(board2)
else:
    print("\nNao ha solucao para o problema 2")