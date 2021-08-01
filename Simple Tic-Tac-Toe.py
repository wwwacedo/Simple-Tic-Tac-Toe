def verifica_vencedor(celulas_do_jogo):  # user_input é uma String
    combinacao_vencedora = [[0, 1, 2], [3, 4, 5], [6, 7, 8],  # horizontal
                            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # vertical
                            [0, 4, 8], [2, 4, 6]]  # diagonal
    vencedor = []
    for x in range(8):
        if celulas_do_jogo[combinacao_vencedora[x][0]][2] == \
                celulas_do_jogo[combinacao_vencedora[x][1]][2] == \
                celulas_do_jogo[combinacao_vencedora[x][2]][2]:
            if celulas_do_jogo[combinacao_vencedora[x][0]][2] in 'OX' and \
                    celulas_do_jogo[combinacao_vencedora[x][0]][2] not in vencedor:
                vencedor.append(celulas_do_jogo[combinacao_vencedora[x][0]][2])
    return vencedor


def conta_caracteres(celulas_do_jogo):
    os, xs, _s = 0, 0, 0
    for celula in celulas_do_jogo:
        if celula[2] == 'O':
            os += 1
        elif celula[2] == 'X':
            xs += 1
        else:
            _s += 1
    return [os, xs, _s]


def status_do_jogo(celulas_do_jogo):
    status = ''
    vencedor = verifica_vencedor(celulas_do_jogo)  # vencedor recebe o retorno da função verifica_vencedor
    caracteres = conta_caracteres(celulas_do_jogo)  # caracteres recebe o retorno da função conta_caracteres
    if len(vencedor) == 0 and caracteres[2] == 0:
        status = 'Draw'
    elif len(vencedor) == 1:
        status = f'{vencedor[0]} wins'
    elif len(vencedor) > 1:
        status = 'Impossible'
    elif caracteres[0] > caracteres[1] and caracteres[0] - caracteres[1] > 1 or caracteres[1] > caracteres[0] and \
            caracteres[1] - caracteres[0] > 1:
        status = 'Impossible'
    elif len(vencedor) == 0 and caracteres[2] != 0:
        status = 'Game not finished'
    return status


def desenha_grid(celulas):
    print(f'''---------
| {celulas[0][2]} {celulas[1][2]} {celulas[2][2]} | 
| {celulas[3][2]} {celulas[4][2]} {celulas[5][2]} |
| {celulas[6][2]} {celulas[7][2]} {celulas[8][2]} | 
---------''')


def jogada():
    return input('Enter the coordinates: ')


def verificador(movimento, numeros):
    movimento = movimento.split()
    achou = [1 for p in movimento if p in numeros]
    if achou != [1, 1]:
        return False
    return True


def verifica_jogada(celulas_do_jogo):
    todos_os_numeros = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    numeros_possiveis = ['1', '2', '3']
    while True:
        j = jogada()
        if len(j.split()) < 2:
            print('You should enter numbers!')
            continue
        elif len(j.split()) == 2 and not verificador(j, todos_os_numeros):
            print('You should enter numbers!')
            continue
        else:
            linha, coluna = j.split()
            coordenadas = [int(linha), int(coluna), '_']
            if not verificador(j, numeros_possiveis):
                print('Coordinates should be from 1 to 3!')
                continue
            elif coordenadas not in celulas_do_jogo:
                print('This cell is occupied! Choose another one!')
                continue
            else:
                return coordenadas


def encontra_posicao_da_celula(celulas_do_jogo, coordenadas):
    i = 0
    c = coordenadas
    for celula in celulas_do_jogo:
        if celula == c:
            break
        else:
            i += 1
            continue
    return i


def atualiza_celulas_do_jogo(celulas_do_jogo, coordenadas, contador_de_jogadas):
    i = encontra_posicao_da_celula(celulas_do_jogo, coordenadas)
    if contador_de_jogadas % 2 == 0:
        celulas_do_jogo.remove([coordenadas[0], coordenadas[1], '_'])
        celulas_do_jogo.insert(i, [coordenadas[0], coordenadas[1], 'X'])
    else:
        celulas_do_jogo.remove([coordenadas[0], coordenadas[1], '_'])
        celulas_do_jogo.insert(i, [coordenadas[0], coordenadas[1], 'O'])
    return celulas_do_jogo


def main():
    contador_de_jogadas = 0
    celulas_do_jogo = [[i, j, '_'] for i in range(1, 4) for j in range(1, 4)]
    while True:
        desenha_grid(celulas_do_jogo)
        status = status_do_jogo(celulas_do_jogo)
        if status != 'Game not finished':
            print(status)
            break
        coordenadas = verifica_jogada(celulas_do_jogo)
        celulas_do_jogo = atualiza_celulas_do_jogo(celulas_do_jogo, coordenadas, contador_de_jogadas)
        contador_de_jogadas += 1


main()

