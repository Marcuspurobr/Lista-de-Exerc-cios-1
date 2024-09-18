print('Aluno: XXXXXXXXXXXXXXXXXXXXXXXXXXXXX\nNro Matrícula: XXXXXXXXXXX\n-------------------------------------\nPrograma referente ao exercício 8\n-------------------------------------',)
m = int(input('Entre com o 1° número: '))
i = 2
for _ in range(100):
    n = int(input(f'Entre com o {i}° número: '))
    if n > m:
        m = n 
    i += 1
print('O maior número é:', m)
print('-------------------------------------')
