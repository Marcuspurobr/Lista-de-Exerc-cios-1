print('Aluno: XXXXXXXXXXXXXXXXXXXXXXXXXXXXX\nNro Matrícula: XXXXXXXXXXX\n-------------------------------------\nPrograma referente ao exercício 25\n-------------------------------------',)

import string

def hexadecimal(x):
    hexa = []

    while x > 16:

        if x % 16 < 10:
            hexa.append(x%16)
        
        else:
            i = x % 16 - 10
            hexa.append(string.ascii_uppercase[i])
        x = x//16
    
    if x < 10:
        hexa.append(x)
    else:
        i = x - 10
        hexa.append(string.ascii_uppercase[i])
    
    return hexa

n = int(input('Insira um número: '))
print(f'O número em hexadecimal é: {hexadecimal(n)}')
print('-------------------------------------')
