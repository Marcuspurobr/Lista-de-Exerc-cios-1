'''
6. Calculadora de Expressões:
Desenvolva uma calculadora que possa avaliar expressões matemáticas simples. O
programa deve:
 1- Aceitar uma expressão como string (por exemplo: "3 + 4 * 2")
 2- Avaliar a expressão respeitando a ordem das operações
 3- Exibir o resultado
 4- Permitir ao usuário inserir novas expressões ou sair

Obs: Use funções para separar a lógica de avaliação e um loop para manter a calculadora
em execução.
'''

'''
 As funções são basicamente a mesma, o que ela faz:
 1- Ela olha cada caracter da lista
 2- Procura o sinal da operação
 3- Pega os números antes e depois da operação usando o índice (i)
 4- Realiza a operação
 5- Deleta um dos números que usei na operação, deleta o sinal e pega o último número 
 usado e substitui pelo resultado da operação e retorna com a operação específica calculada
Exemplo: o usuário insere: 2 + 5 * 5 + 2
O programa transforma em uma lista usando o .split : [2+5*5+2]
depois da função produto vira: [2+25+2]
depois da função soma vira: [29]
'''


def produto(expressao):
    while '*' in expressao:
        for ch in expressao:
            if ch == '*':
                i = expressao.index(ch)
                produto = int(expressao[i-1]) * int(expressao[i+1])
                del expressao[i-1]
                del expressao[i-1]
                expressao[i-1] = produto
    return expressao

def divisao(expressao):
    while '/' in expressao:
        for ch in expressao:
            if ch == '/':
                i = expressao.index(ch)
                divisao = int(expressao[i-1]) / int(expressao[i+1])
                del expressao[i-1]
                del expressao[i-1]
                expressao[i-1] = divisao
    return expressao

def soma(expressao):
    while '+' in expressao:
        for ch in expressao:
            if ch == '+':
                i = expressao.index(ch)
                soma = int(expressao[i-1]) + int(expressao[i+1])
                del expressao[i-1]
                del expressao[i-1]
                expressao[i-1] = soma
    return expressao

def subtracao(expressao):
    while '-' in expressao:
        for ch in expressao:
            if ch == '-':
                i = expressao.index(ch)
                subtracao = int(expressao[i-1]) - int(expressao[i+1])
                del expressao[i-1]
                del expressao[i-1]
                expressao[i-1] = subtracao
    return expressao

def resposta(expressao):
    x = subtracao(soma(divisao(produto(expressao))))
    return x

while True:

    calcular = input('Insira sua expressão: ')
    conta = calcular.strip().split()
    print(f'Deu {str(resposta(conta)).replace('[','').replace(']','')}')
    go_again = input('Deseja realizar mais uma conta? ')
    if go_again.lower() == 'nao':
        break