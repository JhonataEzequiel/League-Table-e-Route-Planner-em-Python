import numpy as np


def busca (g, r, e, y, map_matrix, visitados, rota = False):

    """
        A função busca usará recursão para procurar por rotas diferentes. Quando encontrar uma, a variável rota vai ser True, caso contrário será False.
        O algorítimo de busca é feito com backtracking, e ele percorrer todos os caminhos possíveis nas quatro direções que é possível caminhar.

        Significado das variáveis:

        g = linha atual
        r = coluna atual
        e = linha alvo
        y = linha alvo
        visitados = lista contendo todos os elementos que foram visitados pela função, para evitar entrar em loop
    """

    if rota:
        return True
    if(g>=0 and g<len(map_matrix) and r >=0 and r < len(map_matrix[0])):
        visitados[g][r] = 1

        if(g == e and r == y):
            rota = True

        else:

            if(g+1 < len(map_matrix) and map_matrix[g+1][r] and visitados[g+1][r] != 1 ):
                rota = busca(g+1, r, e, y, map_matrix, visitados, rota)
            if (g - 1 >= 0  and map_matrix[g - 1][r] and visitados[g - 1][r] != 1):
                rota = busca(g - 1, r, e, y, map_matrix, visitados, rota)
            if (r + 1 < len(map_matrix[0]) and map_matrix[g][r + 1] and visitados[g][r + 1] != 1):
                rota = busca(g, r + 1, e, y, map_matrix, visitados, rota)
            if (r - 1 >= 0 and map_matrix[g][r - 1] and visitados[g][r - 1] != 1):
                rota = busca(g, r - 1, e, y, map_matrix, visitados, rota)

    return rota


def route_exists(from_row, from_column, to_row, to_column, map_matrix):
    """
        toda a lógica da route_exists é basicamente feita na busca
    """
    visitados = np.zeros((len(map_matrix), len(map_matrix[0])))
    rota = busca(from_row, from_column, to_row, to_column, map_matrix, visitados)
    return rota