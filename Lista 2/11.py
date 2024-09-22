'''
11. Codificador/Decodificador de Cifra de César:
Crie um programa que codifique e decodifique mensagens usando a Cifra de César. O
programa deve:
 1- Pedir ao usuário se deseja codificar ou decodificar uma mensagem
 2- Solicitar a mensagem e o valor do deslocamento
 3- Exibir o resultado da operação
 4- Oferecer a opção de processar outra mensagem

Obs: Use funções para codificar e decodificar, e loops para processar cada caractere da
mensagem.
'''

import string

listaletras = string.ascii_lowercase


def codificar(l,n):
    codificado = ''
    for ch in l:
        if ch in listaletras:
            i = listaletras.index(ch)
            i += n
            if i >= 26:
                i -= 26
            print(i)
            codificado += listaletras[i]
        else:
            codificado += ch
    return codificado


def decodificar(l,n):
    decodificado = ''
    for ch in l:
        if ch in listaletras:
            i = listaletras.index(ch)
            i -= n
            decodificado += listaletras[i]
        else:
            decodificado += ch
    return decodificado

while True:
    print(('Desejas codificar(1) ou decodificar(2) uma mensagem?'))
    acao = int(input(''))

    if acao == 1:

        print('Insira a mensagem para codificar:')
        mensagem = input('').lower()
        print('Insira o valor do deslocamento:')
        deslocamento = int(input(''))
        print(codificar(mensagem,deslocamento))



    if acao == 2:
        print('Insira a mensagem para decodificar:')
        mensagem = input('').lower()
        print('Insira o valor do deslocamento:')
        deslocamento = int(input(''))
        print(decodificar(mensagem,deslocamento))



    go_again = input('Deseja usar o programa de novo? ')
    if go_again.lower() == 'nao':
        break

