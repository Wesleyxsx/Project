import random
import time
import os


# MOSTRAR TÍTULO
def titulo():
    print('\n#################################\n')
    print('\tEsqueleto chao')
    print('\n#################################\n')

#GERADOR DE 'X' E 'O' DO MAPA
def gerador_linha():
    bloco_gerado = random.choices(esqueleto, weights = [10, 1], k = 1)
    return bloco_gerado

#gerador linha do mapa
def gerador_coluna_mapa(coluna:int, linha:int):
    
    global linha_mapa,mapa
    while True:
        if coluna < pos_coluna:
            coluna += 1
            bloco = gerador_linha()
            linha_mapa.extend(bloco)
        elif coluna == pos_coluna:
            mapa.append(linha_mapa)
            coluna = 0
            if linha < pos_linha:
                linha += 1
                linha_mapa = []
            elif linha == pos_linha:
                break

#contador do while de colunas
coluna = 0

#linha do while de colunas
linha = 1

#Matriz mapa
mapa = []

#linha mapa
linha_mapa = []

#esqueleto do mapa
esqueleto = ['o' , 'x']

titulo()
input('\nDigite ENTER para iniciar o gerador...')

#entrada de linhas
pos_coluna = int(input('\nNúmero de colunas da Matriz do mapa\n'))
pos_linha = int(input('\nNúmero de linhas da Matriz do mapa\n'))

gerador_coluna_mapa(coluna, linha)


for x in range(pos_linha):
    for y in range(pos_coluna):
        print (mapa[x][y], end= " ")
    print("")
