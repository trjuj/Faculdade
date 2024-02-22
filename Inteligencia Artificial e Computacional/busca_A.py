import numpy as np

inicial1 = np.array([0,0,9,0,0,0,5,0,0,
                     0,8,0,0,0,0,0,6,0,
                     7,0,0,8,0,4,0,0,1,
                     0,0,4,0,2,0,3,0,0,
                     0,0,0,5,9,8,0,0,0,
                     0,0,2,0,6,0,9,0,0,
                     3,0,0,6,0,9,0,0,5,
                     0,6,0,0,0,0,0,2,0,
                     0,0,5,0,0,0,4,0,0]).reshape([9, 9])

inicial2 = np.array([0,0,0,0,2,0,3,4,0,
                     2,9,0,0,0,0,0,5,0,
                     5,0,0,1,0,0,0,0,0,
                     0,0,0,6,0,8,9,0,0,
                     1,0,0,0,0,0,0,0,8,
                     0,0,6,5,0,4,0,0,0,
                     0,0,0,0,0,2,0,0,6,
                     0,2,0,0,0,0,0,8,9,
                     0,5,7,0,8,0,0,0,0]).reshape([9, 9])

def checaEstado(mat):
    for i in mat:
        if 0 in mat:
            return None
    return 1

def buscaPossibilidades(mat, row, col):
    result = []
    vet = [1,2,3,4,5,6,7,8,9]

    linha = mat[row]

    coluna = []
    for i in range(9):
        coluna.append(mat[i][col])

    setor = []
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            setor.append(mat[i][j])

    for i in vet:
        if i not in linha:
            if i not in coluna:
                if i not in setor:
                    result.append(i)

    return result

def buscaVazias(mat):
    result = []
    for i in range(9):
        for j in range(9):
            if mat[i][j] == 0:
                result.append((i, j))
    return result

def heuristica(mat):
    result = [] # lista que apresenta o valor a ser colocado assim como suas coordenadas
    possibilidades = []
    vazias = buscaVazias(mat)
    for i in vazias:
        possibilidades.append(buscaPossibilidades(mat, i[0], i[1]))
        