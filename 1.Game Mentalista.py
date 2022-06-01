import random
import time
import os

# MOSTRAR TÍTULO
def titulo():
    print('\n#################################\n')
    print('\tO MENTALISTA')
    print('\n#################################')

# GERANDOR DE NUMEROS ALETÓRIOS
def gerador_numerico():
    numero_gerado = random.randrange(1, 101)
    return numero_gerado

#FUNÇÃO PRINCIPAL
def mentalista(numero, tentativa):
    while True:
        try:
            chute = int(input('\nChute o numero que estou pensando entre 1 e 100. \nResposta: '))
            if chute > 100 or chute < 1:
                time.sleep(1)
                print('\n Apenas um numero entre 1 e 100, tente de novo')
            elif chute > numero:
                time.sleep(1)
                print(f'\nO numero que pensei é menor que {chute}, tente de novo')
                tentativa += 1
                time.sleep(1)
            elif chute < numero:
                time.sleep(1)
                print(f'\nO numero que pensei é maior que {chute}, tente de novo')
                tentativa += 1
                time.sleep(1)
            elif chute == numero:
                time.sleep(1)
                tentativa += 1
                print(f'\nPARABÉNS, você acertou com {tentativa} tentativas')
                time.sleep(1)
                opcao = str(input('Quer jogar mais uma vez? (s/n): '))
                #lower vai dimirnuir, o strip vai seprar as letras e [0] vai dar a posição q quero tirar no caso a primeira
                if opcao.lower().strip()[0] == 's': #or opcao.lower() == 'sim': deixando de necessitar essa parte
                    print('\nReiniciando o jogo...')
                    time.sleep(3)
                    numero = gerador_numerico()
                    tentativa = 0
                    os.system('cls')
                    titulo()
                    continue
                    print(opcao)
                elif opcao.lower().strip()[0] == 'n': #or opcao.lower() == 'nao' or opcao.lower() == 'não': deixando de precissar novamente
                    time.sleep(1)
                    print('\nOk, obrigado por jogar!')
                break

        except ValueError:
            print('\n Digite um numero inteiro!')
            time.sleep(1)
            



titulo()
input('Digite ENTER para iniciar o game...')
numero = gerador_numerico()
tentativa = 0
mentalista(numero, tentativa)
