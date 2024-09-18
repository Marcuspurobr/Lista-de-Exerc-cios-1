print('Aluno: XXXXXXXXXXXXXXXXXXXXXXXXXXXXX\nNro Matrícula: XXXXXXXXXXX\n-------------------------------------\nPrograma referente ao exercício 18\n-------------------------------------',)
name1 = input('Qual o nome do(a) primeiro(a) aluno(a)? ')
grade1 = float(input('E qual foi a sua nota? '))
name2 = input('Qual o nome do(a) segundo(a) aluno(a)?' )
grade2 = float(input('E qual foi a sua nota? '))
if grade1 == grade2:
    print('Ambos tiraram a mesma nota.')
elif grade1 > grade2:
    print(f'{name1} tirou a maior nota.')
else:
    print(f'{name2} tirou a maior nota.')
print('-------------------------------------')