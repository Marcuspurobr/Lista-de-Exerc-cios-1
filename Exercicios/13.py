import math
print('Aluno: XXXXXXXXXXXXXXXXXXXXXXXXXXXXX\nNro Matrícula: XXXXXXXXXXX\n-------------------------------------\nPrograma referente ao exercício 13\n-------------------------------------',)
a = int(input('Insira a 1ª dimensão do triângulo: '))
b = int(input('Insira a 2ª dimensão do triângulo: '))
c = int(input('Insira a 3ª dimensão do triângulo: '))
pt = a+b+c
p = pt/2
at = math.sqrt(p*(p-a)*(p-b)*(p-c))
print('O perímetro é:', pt)
print('A área é:', at)
print('-------------------------------------')