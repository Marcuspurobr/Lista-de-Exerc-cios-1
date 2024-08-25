print('Aluno: XXXXXXXXXXXXXXXXXXXXXXXXXXXXX\nNro Matrícula: XXXXXXXXXXX\n-------------------------------------\nPrograma referente ao exercício 9\n-------------------------------------',)
s = int(input('Entre com o 1° número: '))
i = 2
while s < 100:
    n = int(input(f'Entre com o {i}° número: '))
    s += n
    i += 1
print('A soma final é:', s)
print('-------------------------------------')
