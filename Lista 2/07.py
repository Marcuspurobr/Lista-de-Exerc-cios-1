'''
7. Jogo da Forca:
Crie um jogo da forca. O programa deve:
 1- Ter uma lista predefinida de palavras e escolher uma aleatoriamente
 2- Mostrar os espaços correspondentes a cada letra da palavra
 3- Pedir ao jogador para adivinhar uma letra por vez
 4- Atualizar a exibição da palavra com as letras corretas
 5- Limitar o número de tentativas incorretas
 6- Informar se o jogador ganhou ou perdeu ao final

Obs: Use funções para as diferentes partes do jogo e loops para controlar o fluxo do jogo.
'''
import random

'''
 Função que pega o tamanho da palavra, e gera uma lista com o '_' 
para cada letra que tiver
'''
def gerarjogo(palavra):
    tamanho = len(palavra)
    jogo = []
    for _ in range(len(palavra)):
        jogo.append('_')
    return jogo

'''
Essa função verifica os acertos, e devolve a lista com os '_'
e no lugar de algum '_', ele coloca a letra, caso esteja na posição certa
'''
def acertou(jogo,letra,palavra):
    i = 0
    for ch in palavra:
        if ch == letra:
            jogo[i] = letra
        i += 1
    return jogo


while True:

    lista_palavras = ['livro','caneta','garfo','panela','mesa','cama','microfone','martelo','bolsa','menina','garoto','pai','mae','homem','mulher','medica','estudante']
    palavra = random.choice(lista_palavras)
    jogo = gerarjogo(palavra)
    tentativa = 0

    while True:

        print(jogo)
        letra = input('Digita uma letra: ')


        if letra in palavra:
            jogo = acertou(jogo, letra, palavra)
            print('\nOpa, você acertou uma letra\n')
        else:
            print(f"Que pena, a letra '{letra}' não está na palavra\n")
        tentativa +=1

        # Caso todos os '_' forem substituídos, o usuario ganhou
        if '_' not in jogo:
            print(jogo)
            print('Parabéns, você ganhou!\n')
            break

        # Se acabou todas tentativas, o usuario perdeu
        if tentativa == len(jogo)*2+4:
            print('Acabaram as tentativas, você perdeu')
            print(f'A palavra era {palavra}')
            break

    go_again = input('Deseja jogar novamente? (sim ou nao) ')
    if go_again.lower() == 'nao':
        break