import heapq
import numpy as np

def validador(board, row, col, num):
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False

    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if board[i][j] == num:
                return False

    return True

def acha_celula_vazia(board):
    vazias = []
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                vazias.append((i, j))
    if vazias:
        return vazias
    else:
        return None

def heuristica(board, empty_cell):
    if empty_cell:
        row, col = empty_cell
        possibilidades = 0
        for num in range(1, 10):
            if validador(board, row, col, num):
                possibilidades += 1
        return possibilidades
    return 0

def ordem(x):
    return x[0]

def melhor_celula(board):
    melhores = []
    vazias = acha_celula_vazia(board)
    if vazias:
        for k in vazias:
            possiblidades = heuristica(board, k)
            melhores.append((possiblidades, k[0], k[1]))
        melhores.sort(key=ordem)
        return melhores[0][1], melhores[0][2]
    else:
        return None

def resolve_a_estrela(board):
    heap = [(heuristica(board, melhor_celula(board)), board)]
    while heap:
        _, current_board = heapq.heappop(heap)
        empty_cell = melhor_celula(current_board)
        if not empty_cell:
            return current_board
        row, col = empty_cell
        for num in range(1, 10):
            if validador(current_board, row, col, num):
                new_board = [row[:] for row in current_board]
                new_board[row][col] = num
                heapq.heappush(heap, (heuristica(new_board, empty_cell), new_board))
    return None

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

print("Problema 1:\n")
for row in board1:
    print(row)

solution1 = resolve_a_estrela(board1)

if solution1:
    print("\nSolucao 1:\n")
    for row in solution1:
        print (row)
else:
    print("\nNão há solução para o Problema 1.")

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
for row in board2:
    print(row)

solution2 = resolve_a_estrela(board2)

if solution2:
    print("\nSolucao 2\n")
    for row in solution2:
        print (row)
else:
    print("\nNão há solução para o Problema 2.\n")