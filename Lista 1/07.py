print('Aluno: XXXXXXXXXXXXXXXXXXXXXXXXXXXXX\nNro Matrícula: XXXXXXXXXXX\n-------------------------------------\nPrograma referente ao exercício 7\n-------------------------------------',)
s = 0
i = 1
for _ in range(100):
    n = int(input(f'Entre com o {i}° número: '))
    s += n
    i += 1
print('O resultado é:', s)
print('-------------------------------------')
