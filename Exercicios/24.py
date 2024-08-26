print('Aluno: XXXXXXXXXXXXXXXXXXXXXXXXXXXXX\nNro Matrícula: XXXXXXXXXXX\n-------------------------------------\nPrograma referente ao exercício 23\n-------------------------------------',)
n = float(input('Insira um número: '))
i = 0
while n >= 10:
    n /= 10
    i += 1
while n < 1:
    n *= 10
    i -= 1
n_formatado = "{:.3f}".format(n)
print(f'O número em notação científica é: {n_formatado} * 10^({i})')
print('-------------------------------------')
