print('Aluno: XXXXXXXXXXXXXXXXXXXXXXXXXXXXX\nNro Matrícula: XXXXXXXXXXX\n-------------------------------------\nPrograma referente ao exercício 20\n-------------------------------------',)
num = int(input('Insira um número: '))
menor = num
while num >= 0:
    if num < menor:
        menor = num
    num = int(input('Insira outro número: '))
print('O menor número de todos esses, é:', menor)
print('-------------------------------------')