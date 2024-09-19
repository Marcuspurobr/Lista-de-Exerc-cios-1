'''
1. AnaLisador de Texto:
Crie um programa que analise um texto fornecido pelo usuário. O programa deve:
 1- Solicitar ao usuário que digite um texto
 2- Contar o número total de palavras
 3- Identificar e contar palavras únicas
 4- Encontrar a palavra mais frequente e sua contagem
 5- Calcular o comprimento médio das palavras

Obs: Use funções para modularizar o código e estruturas de repetição para processar o
texto.
'''

# Função para fazer uma lista das palavras únicas (3)
def palavrasunicas(l):
    palavras_unicas = []
    for palavra in l:
        if l.count(palavra) ==1:
            palavras_unicas.append(palavra)
    return palavras_unicas


# Função para encontrar a palavra mais frequente e sua contagem(4)
def palavrafrequente(l):
    mais_frequente = l[0]
    quantidade = 0
    for i1 in range(len(l)):
        n=0
        for i2 in range(len(l)):
            if l[i1] == l[i2] and i1!=i2:
                n+=1
        if n>quantidade:
            quantidade = n
            mais_frequente = l[i1]
    return (mais_frequente,quantidade+1)


# Solicitar ao usuário que digite um texto (1)
texto = input('Insira um texto para ser analisado: ')
palavras = texto.split()
print('')


# Contar o número total de palavras (2)
quantidade_palavras = len(palavras)
print (f'No texto que você digitou há {quantidade_palavras} palavra(s)')
print('')


# Usando a função para identificar e contar palavras únicas (3)
unicas = palavrasunicas(palavras)
quantidade_unica = len(unicas)
print(f'As palavras únicas são: {unicas}, e possui {quantidade_unica} palavra(s) única(s).')
print('')


# Usando a função para encontrar a palavra mais frequente e sua contagem(4)
frequente = palavrafrequente(palavras)
print(f'A palavra mais frequente e sua quantidade é {frequente}')
print('')


#Calcular o comprimento médio das palavras (5)
somatorio = 0
for ch in palavras:
    somatorio += len(ch)
media = somatorio/len(palavras)
print(f'O comprimento médio das palavras é {media}')
