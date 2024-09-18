print('Aluno: XXXXXXXXXXXXXXXXXXXXXXXXXXXXX\nNro Matrícula: XXXXXXXXXXX\n-------------------------------------\nPrograma referente ao exercício 11\n-------------------------------------',)
n = int(input('Entre com o 1° número: '))
i = 2
s = 0
while n > 0:
    s += n
    n = int(input(f'Entre com o {i}° número: '))
    i += 1
print('A soma final é:', s)
print('-------------------------------------')