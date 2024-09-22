'''
13. Gerador de Relatório de Vendas:
Crie um programa que gere relatórios de vendas com base em dados inseridos pelo
usuário. O programa deve:
 1- Permitir ao usuário inserir dados de vendas (produto, quantidade, preço)
 2- Calcular o total de vendas por produto e geral
 3- Identificar o produto mais vendido e o de maior faturamento
 4- Gerar um relatório formatado com estas informações

Obs: Use funções para processar os dados e gerar o relatório, e loops para coletar e analisar
os dados inseridos.
'''
"""
 Essa função verifica cada venda dos dados de venda e pega o maior e o indice dele, pra retornar só o nome
 lembrando que as informações ficam guardadas assim na lista:
 ex: l = [['abacaxi', 2, 250],['banana', 10, 50]]
 Então para um produto, o índice 0 é o nome, o índice 1 é a quantidade e o índice 2 é o preço
"""
def maior_venda(l):
    M = 0
    i = 0
    for venda in l:
        if venda[1] > M:
            M = venda[1]
            i = l.index(venda)
    return l[i][0]


# Mesa coisa que o de cima, a diferença que a fatura é igual a (quantidade*preço)
def maior_fatura(l):
    M = 0
    i = 0
    for fatura in l:
        reais = fatura[1]*fatura[2]
        if reais > M:
            M = reais
            i = l.index(fatura)
    return l[i][0]


# Fiz uma lista para guardar o total da fatura de cada produto
def total_por_produto(l):
    lista_total = []
    for produtos in l:
        lista_total.append(produtos[1]*produtos[2])
    return lista_total

# Somei totas as faturas e peguei o total de todas as faturas
def total_geral(l):
    total = 0
    for valores in l:
        total += valores
    return total


# Codigo para fazer o relatório
def relatorio(l):
    # Cada linha que vai imprimir vou colocar nessa lista
    linhas = []

    # Primeiro adiciono o produto com maior faturamento e maior venda
    linhas.append(f'O produto com o maior faturamento foi: {maior_fatura(l)}')
    linhas.append(f'O produto com a maior venda foi: {maior_venda(l)}')
    linhas.append('')

    # Deixo na variavel o total faturado de cada produto e a soma de todas faturas
    vendas = total_por_produto(l)
    venda_total = total_geral(vendas)

    # Adiciona uma linha para cada produto e o total de sua fatura
    for produto in l:
        i = l.index(produto)
        linhas.append(f'O produto {produto[0]} faturou um total de {vendas[i]} reais')

    # Adiciona a linha com o total
    linhas.append(f'O valor total faturado foi {venda_total}')

    return linhas

# Aqui vou armazenar os dados
dados_de_venda = []

continuar = ''
while continuar.lower() != 'nao':

    print('Insira o nome do produto:')
    produto = input('')
    print('')

    print('Insira a quantidade vendida do produto:')
    quantidade = int(input(''))
    print('')

    print('Insira o preço do produto:')
    preco = int(input(''))
    print('')

    dados_de_venda.append([produto,quantidade,preco])

    print('Deseja inserir mais um produto?(sim ou nao)')
    continuar = input('')
    print('')

for linhas in relatorio(dados_de_venda):
    print(linhas)