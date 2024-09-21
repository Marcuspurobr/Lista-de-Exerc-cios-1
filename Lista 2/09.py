'''
9. Gerenciador de Tarefas:
Crie um programa de gerenciamento de tarefas. O programa deve permitir:
 1- Adicionar novas tarefas com descrição, prioridade e data de vencimento
 2- Listar todas as tarefas, ordenadas por prioridade ou data
 3- Marcar tarefas como concluídas
 4- Remover tarefas
 5- Editar detalhes de uma tarefa existente

Obs: Use funções para cada operação e estruturas de dados apropriadas para armazenar as
tarefas em memória.
'''


# Não me pergunte, eu também não sei... eu demorei muito... e se cair na prova eu não faço dnv

tarefas_prioridade = []
tarefas_vencimento = []

def ListaTarefas(l):
    linhas = []
    for listas in l:
        linhas.append(Tarefas(listas))
    return linhas

def Tarefas(l):
    imagem = '| '
    for termo in l:
        imagem += termo + '   '
    imagem = imagem.strip()+' |'
    return(imagem)

while True:

    print('O que deseja fazer?(Responda com um número)\n')
    print('1- Adicionar nova tarefa\n2- Remover uma tarefa\n3- Editar uma tarefa existente')
    print('4- Listar todos as tarefas por data\n5- Listar todos as tarefas por prioridade\n6- Marcar tarefa como concluida')

    acao = int(input(''))
    print('')

    if acao == 1:
        descrição = input('Insira uma descrição para a tarefa: ')
        prioridade = input('Insira uma prioridade para a tarefa: ')
        data = input('Insira uma data para a tarefa: ')
        tarefas_vencimento.append([data,prioridade,descrição])
        tarefas_prioridade.append([prioridade,data,descrição])


    if acao == 2:
        for linhas in ListaTarefas(tarefas_prioridade):
            print(linhas)
        print(('Escolha o número da tarefa para remover'))
        print('1 para o primeiro etc.')
        i = int(input(''))
        tarefas_vencimento.remove(tarefas_prioridade[i-1])
        del tarefas_prioridade[i-1]

    if acao ==3:
        for linhas in ListaTarefas(tarefas_prioridade):
            print(linhas)
        print(('Escolha o número da tarefa para editar'))
        print('1 para o primeiro etc.')
        i = int(input(''))
        print('')
        print(Tarefas(tarefas_prioridade[i-1]))
        nova_descrição = input('Insira uma nova descrição para a tarefa: ')
        nova_prioridade = input('Insira uma nova prioridade para a tarefa: ')
        nova_data = input('Insira uma nova data para a tarefa: ')
        tarefas_vencimento.append([nova_data,nova_prioridade,nova_descrição])
        tarefas_prioridade.append([nova_prioridade,nova_data,nova_descrição])
        tarefas_vencimento.remove(tarefas_prioridade[i-1])
        del tarefas_prioridade[i-1]

    
    if acao == 4:
        for linhas in ListaTarefas(tarefas_vencimento):
            print(linhas)

    if acao == 5:
        for linhas in ListaTarefas(tarefas_prioridade):
            print(linhas)

    if acao == 6:
        for linhas in ListaTarefas(tarefas_prioridade):
            print(linhas)
        print(('Escolha o número da tarefa para marcar como concluída'))
        print('1 para o primeiro etc.')
        i = int(input(''))
        tarefas_vencimento[i-1].append('Concluída')
        tarefas_prioridade[i-1].append('Concluída')

    tarefas_prioridade_organizado = []
    tarefas_vencimento_organizado = []
    
    while len(tarefas_prioridade) > 0:
        M = 0
        for i in range(len(tarefas_prioridade)):
            if int(tarefas_prioridade[i][0]) > M :
                i_maior = i
                M = int(tarefas_prioridade[i][0])
        tarefas_prioridade_organizado.append(tarefas_prioridade[i_maior])
        del tarefas_prioridade[i_maior]
    
    tarefas_prioridade = tarefas_prioridade_organizado

    while len(tarefas_vencimento) > 0:
        m = '32/100'
        for i in range(len(tarefas_vencimento)):
            if int(tarefas_vencimento[i][0].split('/')[1]) < int(m.split('/')[1]):
                i_menor = i
                m = tarefas_vencimento[i][0]
            elif int(tarefas_vencimento[i][0].split('/')[1]) == int(m.split('/')[1]):
                if int(tarefas_vencimento[i][0].split('/')[0]) < int(m.split('/')[0]):
                    i_menor = i
                    m = tarefas_vencimento[i][0]
        tarefas_vencimento_organizado.append(tarefas_vencimento[i_menor])
        del tarefas_vencimento[i_menor]

    tarefas_vencimento = tarefas_vencimento_organizado
        
    print('')
