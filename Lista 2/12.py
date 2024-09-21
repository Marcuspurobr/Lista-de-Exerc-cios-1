'''
12. Analisador de Palindromo Avançado:
Desenvolva um programa que identifique palíndromos em frases completas. O
programa deve:
 1- Aceitar uma frase como entrada
 2- Ignorar espaços, pontuação e diferenças entre maiúsculas e minúsculas
 3- Determinar se a frase é um palíndromo
 4- Mostrar a frase invertida para comparação
 
Obs: Use funções para limpar e inverter o texto, e loops para processar os caracteres.
'''
import string

# Só coloca o que é letra e minúscula
def limpar(str):
    limpa = ''
    for ch in str:
        if ch.lower() in string.ascii_lowercase:
            limpa += ch.lower()
    return limpa


"""
Pega os termos da frase original, e vai criando uma segunda frase chamada 'invertida'
e vai colocando os termos de traz pra frente, ou seja, começa no final, para no 0, e vai andando
de -1 casa até -1 casa (assim ela vai pegando os de trás)
"""
def inverter(str):
    invertida = ''
    for i in range(len(str),0,-1):
        invertida += str[i-1]
    return invertida

print('Escolha uma frase para que eu analise se é um palíndromo')
frase = input('')
print('')

"""
 Frase separada é pra eu poder depois fazer a parte complicada dessa questao
que é devolver a frase invertida, colocando a mesma quantidade de letras em cada
palavra, só que invertida
"""
frase_separada = frase.split()

# Aqui eu fiz isso só para comparar as frases
frase = limpar(frase)
frase_invertida_limpa = inverter(frase)

"""
# Só comparar, lembrando que cada variável vai ficar nesse formato:
ex= frase = ola tudo bem
frase = olatudobem
frase_invertida_limpa = mebodutalo
"""
if inverter(frase) == frase:
    print('A frase é um palíndromo')
else:
    print('A frase não é um palíndromo')

"""
 Agora pra poder devolver a frase certinha invertida, é complicado
"""
frase_invertida = ''
i = 0

"""
Como eu separei a frase em palavras separadas na variavel frase_separada
 E para cada letra que eu olhar, tenho que ver se ela não é um ponto (1)
 Se não for, pego uma letra na mesma posição [i], só que na frase invertida limpa,
que estão todas as letras invertidas (2)
Depois de pegar a letra, vai pra próxima (3)
 Toda vez que eu terminar de verificar cada palavra, eu coloco um espaço (4)

"""

# Olhando as palavras
for palavras in frase_separada:

    # Olhando letra de cada palavra
    for y in range(len(palavras)):

        #(1)
        if palavras[y] not in string.punctuation:

            #(2)
            frase_invertida += frase_invertida_limpa[i]

            #(3)
            i +=1
    
    #(4)
    frase_invertida += ' '

# Só tirei um espaço que ficou no final da frase
frase_invertida = frase_invertida.strip()
print('A frase invertida ficou:')
print(frase_invertida)