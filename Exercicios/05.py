print('Aluno: XXXXXXXXXXXXXXXXXXXXXXXXXXXXX\nNro Matrícula: XXXXXXXXXXX\n-------------------------------------\nPrograma referente ao exercício 5\n-------------------------------------',)
n1 = int(input('Entre com o 1° número: '))
n2 = int(input('Entre com o 2° número: '))
n3 = int(input('Entre com o 3° número: '))
if n1 >= n2 and n1 >= n3:
    print('O maior número é:', n1)
elif n2>=n3:
    print('O maior número é:', n2)
else:
    print('O maior número é:', n3)
print('-------------------------------------')
