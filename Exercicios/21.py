print('Aluno: XXXXXXXXXXXXXXXXXXXXXXXXXXXXX\nNro Matrícula: XXXXXXXXXXX\n-------------------------------------\nPrograma referente ao exercício 21\n-------------------------------------',)
height = float(input('Insira sua altura: '))
weight = float(input('Insira seu peso(sem mentir viu?): '))
imc = (weight)/(height**2)
if imc < 17:
    print('Você é uma pessoa magra (vamos comer mais um pouquinho?)')
elif imc > 25:
    print('Você está em sobrepeso (está na hora de fazer uma academiazinha)')
else:
    print('Você está com o peso normal')
print('Vale lembrar que esse índice não leva em conta se o peso está relacionado com músculos ou gordura, então não se preocupe tanto com ele ;)')
print('-------------------------------------')