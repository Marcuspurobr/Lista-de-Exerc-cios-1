print('Aluno: XXXXXXXXXXXXXXXXXXXXXXXXXXXXX\nNro Matrícula: XXXXXXXXXXX\n-------------------------------------\nPrograma referente ao exercício 19\n-------------------------------------',)
s = float(input('Insira a 1ª nota: '))
i = 2
while i <= 2:
    nota = float(input(f'Insira a {i}ª nota: '))
    s += nota
    i += 1
media = s/2
print('A média aritmética dessas 20 notas é:', media)
print('-------------------------------------')