'''
8. Analisador de Frequência de Letras:
Desenvolva um programa que analise a frequência de letras em um texto. O programa
deve:
 1- Solicitar ao usuário que digite um texto
 2- Contar a ocorrência de cada letra (ignorando maiúsculas/minúsculas)
 3- Exibir um gráfico de barras simples usando caracteres ASCII para representar as
frequências
 4- Ordenar as letras da mais frequente para a menos frequente

Obs: Use funções para separar a lógica de contagem e exibição, e loops para processar o
texto.
'''


# Função para colocar (sem repetição) quais letras possuem na frase
def LetrasPresentes(str):
    lista_letras = []
    for letra in str:
        if letra not in lista_letras:
            lista_letras.append(letra)
    return lista_letras

# Função para fazer a contagem de cada letra
def QuantidadeLetra (str,letra):
    qtd = 0
    for ch in str:
        if ch == letra:
            qtd +=1
    return qtd
'''
 É a função que faz o gráfico:
Linha1 = a barra incial que todo gráfico tem que ter na vertical, + o tamanho da barra, que é a 
quantidade de vezes que a letra aparece
Linha 2 = coloquei a letra, pra simbolizar no grafico qual é, a barra vertical,
+ o tamanho das barras e no final o número da quantidade de vezes
'''
def GraficoBarras(letra,quantidade):
    linha1 = (' |') + ('_') * quantidade
    linha2 = (f'{letra}|') + ('_') * quantidade + ('|') + (f'{quantidade}')
    return(linha1,linha2)

# Pegar o texto e tirar os espaços e letras maiúsculas
print('Digite um texto para que eu faça a analise de frequência de cada letra: ')
texto1 = input()
texto = texto1.replace(' ','').lower()

# Criar 2 listas, uma pras letras (sem repetir) e outra pra quantidade
letras = LetrasPresentes(texto)
quantidade = []

for letra in letras:
    quantidade.append(QuantidadeLetra(texto,letra))
'''
 Separei elas em ordem crescente, como fiz isso:
criei uma lista nova pra essa nova ordem
fui adicionando as letras e sua quantidade na nova lista, e removendo da lista antiga


obs: a lista das letras e das quantidades, apesar de estarem separadas
elas estavão meio que "alinhadas", pois a letra na posição 0 da lista 'letras'
tinha sua quantidade na posição 0 da lista 'quantidade'
então eu peguei a posição (x) do número maior da lista 'quantidade',
e adicionei na lista nova essa mesma quantidade e a letra na mesma posição (x)
da lista 'letras'
exemplo: 
letras = [a, t,h]
quantidade = [2,1,1]
o maior numero está na posição 0, isso porque o 'a' apareceu 2 vezes no texto,
então vai adicionar na lista "ordem_crescente" [a,2]
e no final a lista vai ficar assim: 
ordem_crescente = [[a,2],[t,1],[h,1]]
'''

ordem_crescente= []
while len(letras)>0:
    m = 0
    for numero in quantidade:
        if numero > m:
            m = numero
            i = quantidade.index(numero)
    
    ordem_crescente.append([quantidade[i],letras[i]])
    del quantidade[i]
    del letras[i]


# Aí para cada letra nessa lista, imprimia o grafico de barras dela
for letra in ordem_crescente:
    for linha in GraficoBarras(letra[1],letra[0]):
        print(linha)


# E no final imprimia mais uma barra para ser a barra horizontal do grafico
print((' |')+('_') * (2*ordem_crescente[0][0]) + ('_____'))
