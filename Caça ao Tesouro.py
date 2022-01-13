# Leitura da matriz

campo = []
for i in range(8):
  campo.append(input().split())

# Leitura e processamento dos sensores

num_sensores = int(input())
alcance = int(input())

for i in range(num_sensores):
  linha, coluna = [int(i) for i in input().split()]

# Impressão da saída
import math

#campo lista com as numeração da matriz
campo = []
for i in range(8):
  campo.append(input().split())


num_sensores = int(input())
alcance = int(input())
sensores = []
#range retorna uma série numérica no intervalo enviado como argumento. A série retornada é um objeto iterável tipo range e os elementos contidos serão gerados sob demanda
for i in range(num_sensores):
  linha_sensor, coluna_sensor = [int(i) for i in input().split()]
  # linha_sensor -= 1
  # coluna_sensor -= 1
  #adiciona as coordenadas do sensor à lista de sensores
  sensores.append([linha_sensor, coluna_sensor])

# Cria lista de baús
baus = []
for linha_campo in range(8): # Vai do 0 ao 7
  for coluna_campo in range(8):
    if campo[linha_campo][coluna_campo] == 'x':
      baus.append([linha_campo, coluna_campo])


# Cria lista de zonas mortas
zonas_mortas = []
for linha_campo in range(8): # Vai do 0 ao 7
  for coluna_campo in range(8):
    if campo[linha_campo][coluna_campo] == 'o':
      zonas_mortas.append([linha_campo, coluna_campo])

      
# Adiciona zona morta extra nos casos onde existe uma zona morta logo acima do sensor e outra logo ao lado
for sensor in sensores:
  for zona_morta in zonas_mortas:
    aux_sensor = [sensor[0] - 1, sensor[1]]
    # Se há uma zona morta colada em cima do sensor
    if zona_morta == aux_sensor:
      aux_sensor = [sensor[0], sensor[1] - 1]
      # Se há também uma zona morta colada na esquerda do sensor
      if aux_sensor in zonas_mortas:
        aux_sensor = [sensor[0] - 1, sensor[1] - 1]
        # Adiciona uma zona morta na esquerda acima colada ao sensor
        zonas_mortas.append(aux_sensor)
      else:
        aux_sensor = [sensor[0], sensor[1] + 1]
        if aux_sensor in zonas_mortas:
          aux_sensor = [sensor[0] - 1, sensor[1] + 1]
          # Adiciona uma zona morta na direita acima colada ao sensor
          zonas_mortas.append(aux_sensor)
    # Se há uma zona morta colada abaixo do sensor
    else:
      aux_sensor = [sensor[0] + 1, sensor[1]]
      if zona_morta == aux_sensor:
        aux_sensor = [sensor[0], sensor[1] - 1]
        #Se há também uma zona morta colada na esquerda do sensor
        if aux_sensor in zonas_mortas:
          # Adiciona uma zona morta na esquerda abaixo colada ao sensor
          aux_sensor = [sensor[0] + 1, sensor[1] - 1]
          zonas_mortas.append(aux_sensor)
        else: 
          aux_sensor = [sensor[0], sensor[1]]
          if aux_sensor in zonas_mortas:
            aux_sensor = [sensor[0] + 1, sensor[1] + 1]
            # Adiciona uma zona morta na direita abaixo colada ao sensor
            zonas_mortas.append(aux_sensor)


zonas_verdes = []
# Para cada sensor, cria sua zona verde e remove as zonas obstruídas pelas zonas mortas
for i, sensor in enumerate(sensores):
  zonas_verdes.append([])
  # Adiciona na zona verde do sensor as áreas visíveis por ele (sem contar as obstruções das zonas mortas)
  for linha_campo in range(8): # Vai do 0 ao 7
    for coluna_campo in range(8):
      # achar um ponto expecifico e medir suas distancias
      # if linha_campo == 5 and coluna_campo == 5:
      #   print("texto pudim", math.fabs(linha_campo - sensor[0]), math.fabs(coluna_campo - sensor[1]))
      # Se o ponto está no alcance do sensor, adiciona o ponto à zona verde desse sensor
      if math.fabs(linha_campo - sensor[0]) <= alcance and math.fabs(coluna_campo - sensor[1]) <= alcance:
        zonas_verdes[i].append([linha_campo, coluna_campo])

  # print("zonas_verdes", zonas_verdes)
  # Remove da zona verde do sensor as áreas obstruídas pelas zonas mortas
  # Busca as zonas mortas contidas na zona verde desse sensor
  for zona_morta in zonas_mortas:
    # Verifica se está dentro da zona verde
    for index_zona_verde, zona_verde in reversed(list(enumerate(zonas_verdes[i]))):
      # Verifica se essa zona morta está dentro da zona verde desse sensor (sensor índice i)
      if zona_morta[0] == zona_verde[0] and zona_morta[1] == zona_verde[1]:
        # Remove da zona verde do sensor as áreas obstruídas pelas zonas mortas
        diferenca_linha = sensor[0] - zona_morta[0]
        diferenca_coluna = sensor[1] - zona_morta[1]
        
        # Remove todos os pontos da zona verde desse sensor (sensor índice i) obstruídos pela zona morta
        if (diferenca_linha > 0 and zona_verde[0] <= zona_morta[0]) or (diferenca_linha < 0 and zona_verde[0] >= zona_morta[0]) or (diferenca_linha == 0 and zona_verde[0] == zona_morta[0]):
          if (diferenca_coluna > 0 and zona_verde[1] <= zona_morta[1]) or (diferenca_coluna < 0 and zona_verde[1] >= zona_morta[1]) or (diferenca_coluna == 0 and zona_verde[1] == zona_morta[1]):
            del zonas_verdes[i][index_zona_verde]


# Após acabar de preencher a lista de zonas verdes de todos os sensores, unimos todas as zonas verdes numa lista só
zona_verde_final = []
for zona_verde in zonas_verdes:
  # for ponto in zona_verde: # Igual ao extend
  #   if ponto not in zona_verde_final:
  #     zona_verde_final.append(ponto)
  zona_verde_final.extend(ponto for ponto in zona_verde if ponto not in zona_verde_final)

contagem_baus_encontrados = 0
# Depois, verificamos se há baús nessa zona verde unificada
for bau in baus:
  if bau in zona_verde_final:
    contagem_baus_encontrados += 1

# Imprime a quantidade de tesouros encontrados
if contagem_baus_encontrados > 0:
  print(str(contagem_baus_encontrados) + " bau(s) encontrado(s).")
else:
  print("Nenhum bau encontrado.")