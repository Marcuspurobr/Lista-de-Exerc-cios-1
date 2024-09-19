'''
2. Jogo de Adivinhação:
Desenvolva um jogo onde o computador escolhe um número aleatório e o usuário 
tenta adivinhar. O programa deve:
 1- Gerar um número aleatório entre 1 e 100
 2- Pedir ao usuário para adivinhar o número
 3- Informar se o palpite está alto, baixo ou correto
 4- Limitar o número de tentativas a 10
 5- Perguntar se o usuário quer jogar novamente ao final
 
Obs: Use funções para organizar o código e loops para controlar as tentativas e repetições
do jogo.
'''

import random

# Função pra definir se o número chutado é maior(retorna 1), menor (retorna 2) ou igual (retorna 0) (3)
def proximidade(x,y):
    if x>y:
        return(2)
    if x<y:
        return(1)
    return(0)

# Gerando o número aleatório (1)
random_num = random.randint(1,100)
tentativa = 0

# Primeiro while pra deixar o jogo ligado, só vai acabar quando a pessoa não quiser jogar mais(5)
while True:

    # O jogo em si, acaba na tentativa número 10 (4)
    while True:

        # Pedindo o palpite do jogador (1)
        palpite = int(input('Coloque sua tentativa: '))
        print('')

        # Analisando o palpite (3)
        if proximidade(palpite,random_num) == 2:
            print('Chute um valor mais baixo\n')
        elif proximidade(palpite,random_num) == 1:
            print('Chute um valor mais alto\n')
        # Caso acerte, acabou o jogo (4)
        else:
            print('ACERTOUUU :) \n')
            break

        # Caso tenha errado, aumenta a tentativa, e se ja foram as 10 tentativas, acaba (4)
        tentativa +=1
        if tentativa == 10:
            print('Você perdeu :(\n')
            break

    jogar_denovo = input('Gostaria de jogar novamente?(sim ou nao) ')

    if jogar_denovo.lower() == 'nao':
        break
    #Caso o usuário queira jogar de novo, é importante zerar as tentativas e escolher um novo número(5)
    tentativa = 0
    random_num = random.randint(1,100)