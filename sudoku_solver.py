def gerarTabuleiro(lista):
    separador1 = "+-----------------------+"
    separador2 = "| "

    print(separador1)

    for x in range(0, 9):
        if x == 3 or x == 6:
            print(separador1)

        print(separador2, end="")

        for y in range(0, 9):
            if y == 3 or y == 6:
                print(separador2, end="")
            etc = str(lista[x][y]) + " "

            print(etc, end="")
        print(separador2)
    print(separador1)


def solucionar_tabuleiro(lista):
    contador_quadrante = 0
    valor_quadrante = []
    posicao_numero_vez = []
    possiveis_numeros = []

    for rei in range(0, 9):
        for numero_vez in range(1, 10):
            for x in range(0, 9):  # Pega a posição de todos os "num. da vez" contidos no tabuleiro
                for y in range(0, 9):
                    if lista[x][y] == numero_vez:
                        posicao_numero_vez.append([y, x])

            for i in range(0, 9):  # Loop de cada quadrante
                quadrante_aux = []
                quadrante = []
                numero_permitido_quadrante = 0
                numero_ja_foi = None

                quadrante = quadrante_disponivel(i + 1,
                                                 lista)  # Retorna uma lista com os números e a posição do quadrante

                for i in range(0, len(quadrante)):  # Retornando apenas os valores dos quadrantes
                    quadrante_aux.append(quadrante[i][2])

                if ('.' in quadrante_aux) and not (numero_vez in quadrante_aux):
                    for k in range(0, 9):  # Compara os 9 nums. do quadrante c/ números da vez
                        numero_permitido = 0  # Variável auxiliar para firmar que o mesmo número não vai estar na horizontal nem na vertical em todas as comparaçoes

                        for j in range(0, len(posicao_numero_vez)):  # Loop número da vez
                            if ((posicao_numero_vez[j][0] != quadrante[k][0]) and (
                                posicao_numero_vez[j][1] != quadrante[k][1])):
                                if quadrante[k][2] == '.':
                                    numero_permitido += 1
                            else:
                                break

                            if numero_permitido == len(
                                    posicao_numero_vez):  ## Só deixa passar se nenhum dos "números da vez" for da mesma posição que o número escolhido
                                possiveis_numeros.append(quadrante[k][0:2])

                    if (len(possiveis_numeros) == 1):
                        pos_x = possiveis_numeros[0][0]
                        pos_y = possiveis_numeros[0][1]
                        lista[pos_y][pos_x] = numero_vez

                    possiveis_numeros.clear()
                quadrante_aux.clear()
            posicao_numero_vez.clear()

    return lista


def quadrante_disponivel(posicao, lista):
	# Este método retorna os quadrantes do tabuleiro, de acordo
	# com a posicao do quadrante e a lista solicidada nos parâmetros,
	# o retorno da lista é na sintaxe [X, Y, VALOR_POSICAO].
	# Por enquanto deixei cetado manualmente todo esse método.
	
    valores_quadrante = []

    if (posicao == 1):
        valores_quadrante = [[0, 0, lista[0][0]], [0, 1, lista[1][0]], [0, 2, lista[2][0]],
                             [1, 0, lista[0][1]], [1, 1, lista[1][1]], [1, 2, lista[2][1]],
                             [2, 0, lista[0][2]], [2, 1, lista[1][2]], [2, 2, lista[2][2]]]
        return valores_quadrante

    elif (posicao == 2):
        valores_quadrante = [[0, 3, lista[3][0]], [0, 4, lista[4][0]], [0, 5, lista[5][0]],
                             [1, 3, lista[3][1]], [1, 4, lista[4][1]], [1, 5, lista[5][1]],
                             [2, 3, lista[3][2]], [2, 4, lista[4][2]], [2, 5, lista[5][2]]]
        return valores_quadrante

    elif (posicao == 3):
        valores_quadrante = [[0, 6, lista[6][0]], [0, 7, lista[7][0]], [0, 8, lista[8][0]],
                             [1, 6, lista[6][1]], [1, 7, lista[7][1]], [1, 8, lista[8][1]],
                             [2, 6, lista[6][2]], [2, 7, lista[7][2]], [2, 8, lista[8][2]]]
        return valores_quadrante

    elif (posicao == 4):
        valores_quadrante = [[3, 0, lista[0][3]], [3, 1, lista[1][3]], [3, 2, lista[2][3]],
                             [4, 0, lista[0][4]], [4, 1, lista[1][4]], [4, 2, lista[2][4]],
                             [5, 0, lista[0][5]], [5, 1, lista[1][5]], [5, 2, lista[2][5]]]
        return valores_quadrante

    elif (posicao == 5):
        valores_quadrante = [[3, 3, lista[3][3]], [3, 4, lista[4][3]], [3, 5, lista[5][3]],
                             [4, 3, lista[3][4]], [4, 4, lista[4][4]], [4, 5, lista[5][4]],
                             [5, 3, lista[3][5]], [5, 4, lista[4][5]], [5, 5, lista[5][5]]]
        return valores_quadrante

    elif (posicao == 6):
        valores_quadrante = [[3, 6, lista[6][3]], [3, 7, lista[7][3]], [3, 8, lista[8][3]],
                             [4, 6, lista[6][4]], [4, 7, lista[7][4]], [4, 8, lista[8][4]],
                             [5, 6, lista[6][5]], [5, 7, lista[7][5]], [5, 8, lista[8][5]]]
        return valores_quadrante

    elif (posicao == 7):
        valores_quadrante = [[6, 0, lista[0][6]], [6, 1, lista[1][6]], [6, 2, lista[2][6]],
                             [7, 0, lista[0][7]], [7, 1, lista[1][7]], [7, 2, lista[2][7]],
                             [8, 0, lista[0][8]], [8, 1, lista[1][8]], [8, 2, lista[2][8]]]
        return valores_quadrante

    elif (posicao == 8):
        valores_quadrante = [[6, 3, lista[3][6]], [6, 4, lista[4][6]], [6, 5, lista[5][6]],
                             [7, 3, lista[3][7]], [7, 4, lista[4][7]], [7, 5, lista[5][7]],
                             [8, 3, lista[3][8]], [8, 4, lista[4][8]], [8, 5, lista[5][8]]]
        return valores_quadrante

    elif (posicao == 9):
        valores_quadrante = [[6, 6, lista[6][6]], [6, 7, lista[7][6]], [6, 8, lista[8][6]],
                             [7, 6, lista[6][7]], [7, 7, lista[7][7]], [7, 8, lista[8][7]],
                             [8, 6, lista[6][8]], [8, 7, lista[7][8]], [8, 8, lista[8][8]]]
        return valores_quadrante


# numeros = [[5, 6, '.', 8, 4, 7, '.', '.', '.'], [3, '.', 9, '.', '.', '.', 6, '.', '.'], ['.', '.', 8, '.', '.', '.', '.', '.', '.'], ['.', 1, '.', '.', 8, '.', '.', 4, '.'], [7, 9, '.', 6, '.', 2, '.', 1, 8], ['.', 5, '.', '.', 3, '.', '.', 9, '.'], ['.', '.', '.', '.', '.', '.', 2, '.', '.'], ['.', '.', 6, '.', '.', '.', 8, '.', 7],  ['.', '.', '.', 3, 1, 6, '.', 5, 9]]

numeros = [[], [], [], [], [], [], [], [], []]

for i in range(0, 9):
    for j in range(0, 9):
        numeros[i].append(input('Digite o item: '))

gerarTabuleiro(solucionar_tabuleiro(numeros))