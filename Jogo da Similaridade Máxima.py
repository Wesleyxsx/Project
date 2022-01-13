
tamanho_quadrado_maior = int(input())

quadrado_maior = []
for i in range(tamanho_quadrado_maior):
  quadrado_maior.append(input().split())

tamanho_quadrado_menor = int(input())

quadrado_menor = []
for i in range(tamanho_quadrado_menor):
  quadrado_menor.append(input().split())

similaridade_maxima = -1
max_similaridade_posicao_x = 0
max_similaridade_posicao_y = 0
for posicao_x in range(tamanho_quadrado_maior - tamanho_quadrado_menor + 1):
  for posicao_y in range(tamanho_quadrado_maior - tamanho_quadrado_menor + 1):
      contagem = 0
      for iterador_linha in range(tamanho_quadrado_menor):
          for iterador_coluna in range(tamanho_quadrado_menor):
              if (quadrado_maior[posicao_x + iterador_linha][posicao_y + iterador_coluna] == quadrado_menor[iterador_linha][iterador_coluna]):
                  similaridade = 100 * contagem / (tamanho_quadrado_menor ** 2)
                  contagem += 1
                  if similaridade > similaridade_maxima:
                      similaridade_maxima = similaridade
                      max_similaridade_posicao_x = posicao_x
                      max_similaridade_posicao_y = posicao_y

# Imprime a saída conforme pedido
print("Posição: ({0},{1})".format(max_similaridade_posicao_x, max_similaridade_posicao_y))
print("Similaridade máxima: {:.2f}%".format(similaridade_maxima))