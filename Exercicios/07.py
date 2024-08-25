print('Aluno: XXXXXXXXXXXXXXXXXXXXXXXXXXXXX\nNro Matrícula: XXXXXXXXXXX\n-------------------------------------\nPrograma referente ao exercício 7\n-------------------------------------',)
s = int(input('Entre com o 1° número: '))
i = 2
for _ in range(99):
    n = int(input(f'Entre com o {i}° número: '))
    s += n
    i += 1
print('O resultado é:', s)
print('-------------------------------------')
