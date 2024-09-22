'''
15. Simulador de Loteria:
Crie um programa que simule um jogo de loteria. O programa deve:
 1- Permitir ao usuário escolher 6 números entre 1 e 60
 2- Gerar 6 números aleatórios como resultado do sorteio
 3- Comparar os números do usuário com o resultado e informar quantos acertos houve
 4- Simular múltiplos sorteios e calcular a probabilidade de ganhar baseada nos
resultados

Obs: Use funções para gerar números, comparar resultados e calcular probabilidades, e
loops para simular múltiplos sorteios.
'''
import random

# Função para fazer um resultado de um sorteio
def resultado():

    # Vou escrever o resultado em uma lista
    resultado = []

    # São 6 numeros, entao vai executar 6 vezes
    for _ in range(6):

        # Adiciona um número aleatório de 0 a 60
        resultado.append(random.randint(0,60))
    return resultado

# Função para ver quantos acertos tiveram
def acertou(escolha, resultado):
    acertos = 0

    # Para cada número, se tiver presente no resultado, acerto soma 1
    for numero in escolha:
        if numero in resultado:
            acertos+=1
    return acertos

# Formula de probabilidade, para retornar em porcentagem
def probabilidade(acertos,total):
    return(acertos*100/total)


escolha = []

# Pedir para escolher os números
print('Escolha 6 números de 0 a 60')

# Executa 6 vezes, pois são 6 números
for n in range(6):

    # Escreve os 6 números
    numero = int(input(f'Escolha o número {n+1}: '))

    # Se inseriu um número no intervalo errado, manda o usuário escrever de novo
    while numero > 60 or numero < 0:
        print('')
        print('Entre 0 a 60, por favor insira novamente: ')
        numero = int(input(''))
    
    # Depois de deixar o número no intervalo, adiciona na lista
    escolha.append(numero)

# Simula um sorteio
resultado1 = resultado()
acertos = acertou(escolha,resultado1)

# Mostra os resultados
print(f'A sua escolha foi {escolha}')
print(f'E o resultado do sorteio foi {resultado1}')
print(f'E você teve {acertos} acertos') 

# Simulação de múltiplos sorteios
# 1- Pergunta quantos serão
print('Quantos sorteios você deseja realizar?')
sorteios = int(input(''))

# Quantidade de vezes que ganhou 
ganhou = 0

# Vai executar 'x' vezes, e o x é o valor que o usuário escolheu em cima
for _ in range(sorteios):

    # Considerei que um sorteio ganho, é aquele que teve pelo menos 1 número certo
    # Porque se fossem todos, seria impossível praticamente
    if acertou(escolha,resultado()) >= 1:
        ganhou += 1

print(f'A chance de ganhar é de {probabilidade(ganhou,sorteios)}%')
