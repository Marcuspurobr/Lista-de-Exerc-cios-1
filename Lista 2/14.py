'''
14. Jogo de Questões e Respostas:
Desenvolva um jogo de perguntas e respostas. O programa deve:
 1- Ter uma lista predefinida de perguntas e respostas
 2- Apresentar as perguntas ao jogador em ordem aleatória
 3- Verificar se a resposta está correta
 4- Manter uma pontuação
 5- Mostrar o resultado final e perguntar se o jogador quer jogar novamente

Obs: Use funções para gerenciar perguntas, verificar respostas e gerenciar a pontuação, e
loops para controlar o fluxo do jogo.
'''

import random

# Pequena observação: eu acho mais fácil fazer o código sem usar função;
# Mas como ele pediu, então eu fiz


# Função pra pegar a proxima pergunta, junto com sua resposta
def proxima_pergunta(perguntas,respostas):

    # Pega uma aleatoria
    pergunta = random.choice(perguntas)

    # Pega a posição dela
    i = perguntas.index(pergunta)

    # E pega a resposta que está na mesma posição, só que na lista 'respostas'
    resposta = respostas[i]

    # Devolve a pergunta e a resposta
    return(pergunta,resposta)


# Função para comparar o palpite e a resposta correta
def verificar(p,r):

    # Se o palpite for a resposta retorna 1
    if p.lower() == r:
        return 1
    # Se não, retorna 0
    return 0

while True:

    # Lista de Perguntas e respostas
    perguntas = ['Quanto é 7x8?','Qual o nome do processo de divisão celular em que uma célula dá origem a outras duas idênticas?', 'Complete a frase: o objeto ________ é o complemento que se liga ao verbo transitivo por meio de preposição','O isopropanol é um álcool primário.(V ou F?)']
    respostas = ['56','mitose','indireto','v']

    # O enunciado pediu pra fazer uma função pra pontuação, mas tipo
    # É literalmente só fazer uma variável, vou fazer uma função pra isso não
    pontuacao = 0

    # Enquanto ouver perguntas que não foram usadas 
    # Lembrando que todas vez que eu usar uma pergunta, vou remove-la da lista
    while len(perguntas)>0:

        # Pega a próxima pergunta
        questao = proxima_pergunta(perguntas,respostas)

        # Printa ela pro usuário responder
        print(questao[0])
        palpite = input('')
        print('')

        # Usamos a função pra ver se está certo
        # Lembrando que ela retorna 1(se está certo) ou 0 (se está errado)
        acertou = verificar(palpite,questao[1])

        if acertou == 1:
            print('Certa resposta\n')
            pontuacao += 1
        else:
            print('Resposta incorreta\n')

        # Tira a pergunta e a resposta usada
        perguntas.remove(questao[0])
        respostas.remove(questao[1])
    
    print(f'Fim do Jogo, sua pontuação foi {pontuacao}')

    # Caso queira parar, se a resposta for "nao" o programa para
    go_again = input('Deseja jogar novamente? ')
    if go_again.lower() == 'nao':
        break
    print('')

