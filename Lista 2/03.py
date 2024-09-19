'''
3. Conversor de Unidades:
Crie um programa que converta entre diferentes unidades de medida. O programa
deve:
 1- Oferecer um menu com opções de conversão (por exemplo: km para milhas, Celsius
para Fahrenheit, kg para libras)
 2- Pedir ao usuário para escolher uma opção e inserir o valor a ser convertido
 3- Exibir o resultado da conversão
 4- Perguntar se o usuário deseja fazer outra conversão

Obs: Use funções para cada tipo de conversão e um loop para manter o programa rodando
até que o usuário escolha sair.
'''

#Nessas funções o primeiro if serve pra fazer a primeira conversão, o segundo return é pra voltar a inversa
def CelsiusFahrenheit(n,t):
    if t == 2:
        return (n*(9/5))+32
    return (n-32)*5/9

def KmMilhas(n,t):
    if t==1:
        return(n/0.621371)
    return (n*1.60934)

def KgLibras(n,t):
    if t==3:
        return(n*2.205)
    return (n*0,4536)


while True:

    # Pedindo para que coloque qual operação fazer, e pedindo o número para realizar a conversão
    print('Qual conversão você deseja fazer?(Escolha um número)\n1- Km -> milhas\n2- Celsius -> Fahrenheit\n3- Kg para libras/\n4- Milhas -> km\n5- FahrenheiT -> Celsius\n6- Libras -> kg')
    tipo = int(input(''))
    numero = int(input('Insira o número que gostaria de fazer a conversão: '))

    # Verificando qual operação ele quer fazer, e devolvendo o valor já convertido das funções
    if tipo == 2:
        print(f'Sua conversão deu {CelsiusFahrenheit(numero,tipo)} Fahrenheits')
    elif tipo ==5:
        print(f'Sua conversão deu {CelsiusFahrenheit(numero,tipo)} Celsius')
    elif tipo == 1:
        print(f'Sua conversão deu {KmMilhas(numero,tipo)} milhas')
    elif tipo == 4:
        print(f'Sua conversão deu {KmMilhas(numero,tipo)} Km')
    elif tipo == 3:
        print(f'Sua conversão deu {KmMilhas(numero,tipo)} libras')
    elif tipo == 6:
        print(f"Sua conversão deu {KmMilhas(numero,tipo)} kg's")
    
    
    # Caso a pessoa nao queira fazer mais conversões, interrompe o while e acaba o programa

    go_again = input('Deseja fazer mais uma conversão? (sim ou nao) ')

    if go_again.lower() == 'nao':
        break