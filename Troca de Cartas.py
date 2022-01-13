input_num_linhas_repetidas = int(input())
cartas_repetidas = []

for quantidade_linhas in range(input_num_linhas_repetidas):
    inserido = input().upper().split()
    dict_carta = {'nome': str(inserido[0]), 'quantidade': int(inserido[1])}
    cartas_repetidas.append(dict_carta)

input_num_linhas_adquirir = int(input())
cartas_adquirir = []

for quantidade_linhas in range(input_num_linhas_adquirir):
    inserido = input().upper().split()
    dict_carta = {'nome': str(inserido[0]), 'quantidade': int(inserido[1])}
    cartas_adquirir.append(dict_carta)

propostas = []
while 1 == 1:
    inserido = str(input().upper())
    if inserido == '---':
        break
    inserido = inserido.split()
    dict_troca_carta = {'nome_carta_recebida': inserido[0], 'nome_carta_dada': inserido[1]}
    propostas.append(dict_troca_carta)

troca_realizada = False

for proposta in propostas:
    for carta_repetida in cartas_repetidas:
        if ((proposta['nome_carta_dada'] == carta_repetida['nome']) and (carta_repetida['quantidade'] > 0)):
            carta_repetida['quantidade'] -= 1
            index = next(
                (i for i, carta in enumerate(cartas_adquirir) if carta['nome'] == proposta['nome_carta_recebida']),
                None)
            if index == None:
                index = next(
                    (i for i, carta in enumerate(cartas_repetidas) if carta['nome'] == proposta['nome_carta_recebida']),
                    None)
                if index == None:
                    cartas_repetidas.append({'nome': proposta['nome_carta_recebida'], 'quantidade': 1})
                else:
                    cartas_repetidas[index]['quantidade'] += 1
            elif cartas_adquirir[index]['quantidade'] > 0:
                cartas_adquirir[index]['quantidade'] -= 1
            else:
                index = next(
                    (i for i, carta in enumerate(cartas_repetidas) if carta['nome'] == proposta['nome_carta_recebida']),
                    None)
                if index == None:
                    cartas_repetidas.append({'nome': proposta['nome_carta_recebida'], 'quantidade': 1})
                else:
                    cartas_repetidas[index]['quantidade'] += 1
            print('TROCA REALIZADA!')
            troca_realizada = True
            break
    if troca_realizada == False:
        print('TROCA NAO REALIZADA!')
    else:
        troca_realizada = False

index_cartas_desejadas = next((k for k, carta in enumerate(cartas_adquirir) if carta['quantidade'] != 0), None)
if index_cartas_desejadas == None:
    print('JOAO CONSEGUIU AS CARTAS DESEJADAS!')
else:
    print('JOAO NAO CONSEGUIU AS CARTAS DESEJADAS!')
