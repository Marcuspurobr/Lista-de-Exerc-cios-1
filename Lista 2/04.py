'''
4. Gerador de Senhas:
Desenvolva um programa que gere senhas aleatórias com base em critérios
especificados pelo usuário. O programa deve:
 1- Pedir ao usuário o comprimento desejado da senha
 2- Perguntar se deve incluir letras maiúsculas, minúsculas, números e/ou caracteres
especiais
 3- Gerar e exibir uma senha que atenda aos critérios
 4- Oferecer a opção de gerar outra senha

Obs: Use funções para gerar diferentes tipos de caracteres e um loop para construir a senha.
'''

import random
import string

# Funções para pegar caracteres para a senha:

def GerarMaiuscula():
    return random.choice(letras_maiuscula)

def GerarMinuscula():
    return random.choice(letras_minuscula)

def GerarNumero():
    return str((random.randint(1,9)))

def GerarCaracter():
    return random.choice(caracteres)

# Cada uma dessas variáveis tem todos os elementos de cada especificidade
# Para isso usei a biblioteca string
letras_minuscula = string.ascii_lowercase
letras_maiuscula = string.ascii_uppercase
caracteres = string.punctuation

while True:
    comprimento = int(input('Qual será o comprimento da senha? '))
    tamanho_atual = 0
    
    print('Responda as perguntas com sim ou nao:')

    maiuscula = input('Deseja incluir letras maiúsculas? ')
    minuscula = input('Deseja incluir letras minusculas? ')
    numero = input('Deseja incluir letras números? ')
    caracter = input('Deseja incluir letras caracteres? ')

    condicoes = []
    if maiuscula.lower() == 'sim':
        condicoes.append(0)
    if minuscula.lower() == 'sim':
        condicoes.append(1)
    if numero.lower() == 'sim':
        condicoes.append(2)
    if caracter.lower() == 'sim':
        condicoes.append(3)        
    

    senha = ''
    while tamanho_atual < comprimento:
        i = random.choice(condicoes)
        if i == 0:
            senha += GerarMaiuscula()
        elif i == 1:
            senha += GerarMinuscula()
        elif i == 2:
            senha += GerarNumero()
        else:
            senha += GerarCaracter()
        tamanho_atual +=1
    print(f'Sua senha é {senha}')
    
    go_again = input('Deseja formar uma nova senha? (sim ou nao) ')
    if go_again == 'nao':
        break

