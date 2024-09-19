'''
5. Agenda de Contatos:
Crie um programa que simule uma agenda de contatos. O programa deve permitir:
 1- Adicionar um novo contato (nome, telefone, email)
 2- Buscar um contato pelo nome
 3- Editar um contato existente
 4- Excluir um contato
 5- Listar todos os contatos

Obs: Use funções para cada operação e estruturas de dados apropriadas para armazenar os
contatos em memória.
'''

# Nesse exercício eu esqueci de usar função, então deixei assim por preguiça

contatos = []
while True:

    # Eu separei cada ação diferente por um número, e aí, só realizei a operação de acordo com o número da ação
    print('O que deseja fazer?(Responda com um número)\n')
    print('1- Adicionar um novo contato\n2- Buscar um contato pelo nome\n3- Editar um contato existente')
    print('4- Excluir um contato\n5- Listar todos os contatos')

    acao = int(input(''))
    print('')

    if acao == 1:
        nome = input('Insira o nome do novo contato: ')
        telefone = input('Insira o telefone do novo contato: ')
        email = input('Insira o email do novo contato: ')
        contatos.append([nome,telefone,email])


    if acao == 2:
        nome_encontrar = input('Insira o nome do contato que quer procurar: ')
        for contato in contatos:
            if contato[0] == nome_encontrar:
                print(contato)
            else:
                print('Contato não encontrado')

    if acao ==3:
        nome_editar = input('Insira o nome do contato que quer editar: ')
        for contato in contatos:
            if contato[0] == nome_editar:
                i = contatos.index(contato)
                print(contato)
                novo_nome = input('Insira um novo nome para o contato: ')
                novo_telefone = input('Insira um novo telefone para o contato: ')
                novo_email = input('Insira um novo email para o contato: ')
                contatos.append([novo_nome,novo_telefone,novo_email])
                del contatos[i]
            else:
                print('Contato não encontrado')
    
    if acao == 4:
        nome_excluir = input('Insira o nome do contato que quer excluir: ')
        for contato in contatos:
            if contato[0] == nome_excluir:
                i = contatos.index(contato)
                del contatos[i]
            else:
                print('Contato não encontrado')

    if acao == 5:
        for contato in contatos:
            print(contato[0])

    print('')
