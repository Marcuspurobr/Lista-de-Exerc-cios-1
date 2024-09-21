'''
10. Simulador de Banco:
Desenvolva um programa que simule operações bancárias básicas. O programa deve:
 1- Permitir criar contas com saldo inicial
 2- Realizar depósitos e saques
 3- Transferir dinheiro entre contas
 4- Verificar saldo
 5- Gerar um extrato simples das transações

Obs: Use funções para cada operação bancária e loops para manter o programa em
execução até que o usuário escolha sair.
'''

# Função para deposito, pega o valor do salto e soma
def deposito(conta,valor):
    return (conta+valor)



"""Função para saque, primeiro vê se tem dinheiro na conta:
se nao tiver, retorna (-1), aí depois la em baixo do código eu ponho que
 se der (-1), vai imprimir 'Nao tem dinheiro' 
se tiver dinheiro, retorna o valor do saldo e subtrai do saque"""

def saque(conta,valor):
    if conta<valor:
        return (-1)
    return (conta-valor)

# Duas listas, uma pra saldo das contas e outra pra salvar os extratos
contas = []
extrato = []


while True:


    """ Igual nos ultimos exercicios, é uma listinha por usuário escolher
     o que ele quer fazer """

    print('')
    print('O que deseja fazer?(Responda com um número)\n')
    print('1- Criar uma conta bancaria\n2- Realizar um saque\n3- Realizar um depósito')
    print('4- Transferir o dinheiro para outra conta\n5- Gerar o extrato de uma conta \n6- Verificar saldo')
    acao = int(input(''))
    print('')

    # Caso queira criar uma conta
    if acao == 1:

        # Valor do saldo inicial
        print('Insira o valor inicial da sua nova conta bancária:')
        reais = int(input(''))

        # Coloca o saldo na lista de contas
        contas.append(reais)
        # Cria um extrato pra essa conta
        extrato.append([])

    # Saque
    if acao == 2:
        print(contas)

        # Pergunta qual conta é
        print('Qual conta você gostaria de realizar o saque?')

        # Se for a conta número 1, tem que lembrar que o índice
        # dela será 0, pois a lista começa a contar do 0 pra frente
        indice_conta = int(input('')) - 1

        print('Insira o valor do saque que deseja realizar:')
        reais = int(input(''))

        # O saque atualizado vai ser o resultado da função
        novo_saldo = saque(contas[indice_conta],reais)

        """ Lembra la tras que eu disse que se a função retornar -1,
        é porque não tem dinheiro? Vou usar aqui"""

        if novo_saldo == -1:
            print('Você não possui essa quantidade de dinheiro')
        
        # Aí caso tenha dinheiro, atualiza o saldo e coloca no extrato a operação
        else:
            contas[indice_conta] = novo_saldo
            extrato[indice_conta].append(f'-{reais}')

    # Mesma coisa que o saque, só que agora é o depósito
    if acao == 3:

        print(contas)

        print('Qual conta você gostaria de realizar o deposito?')
        indice_conta = int(input('')) - 1

        print('Insira o valor do deposito que deseja realizar:')
        reais = int(input(''))

        novo_saldo = deposito(contas[indice_conta],reais)

        contas[indice_conta] = novo_saldo
        extrato[indice_conta].append(f'+{reais}')

    # Transferencia
    if acao == 4:

        print(contas)

        # Escolhe a conta para realizar a retirada
        print('Qual conta você gostaria de retirar o dinheiro')
        indice_conta1 = int(input('')) - 1
        print('')

        # Escolhe a conta para realizar a entrada
        print('Qual conta você gostaria de adicionar o dinheiro')
        indice_conta2 = int(input('')) - 1

        # Valor
        print('Insira o valor da transferência que deseja realizar:')
        reais = int(input(''))

        # Valor de cada saldo novo, do saque e do deposito
        novo_saldo1 = saque(contas[indice_conta1],reais)
        novo_saldo2 = deposito(contas[indice_conta2],reais)
        
        # Lembrando que tem que ver se a conta do saque tem o dinheiro
        if novo_saldo1 == -1:
            print(f'Você não possui essa quantidade de dinheiro na conta {indice_conta1+1}')
        
        # Caso tenha, atualiza as contas
        else:
            contas[indice_conta2] = novo_saldo2
            extrato[indice_conta2].append(f'+{reais}')
            contas[indice_conta1] = novo_saldo1
            extrato[indice_conta1].append(f'-{reais}')

    # Ver o Extrato
    if acao == 5:
        print(contas)

        print('Qual conta você gostaria de visualizar o extrato')
        indice_conta = int(input('')) - 1

        # Só printar a lista de extratos
        print(extrato[indice_conta])

    # Ver o saldo
    if acao == 6:
        print(contas)
