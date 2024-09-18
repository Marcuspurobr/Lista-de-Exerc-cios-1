print('Aluno: XXXXXXXXXXXXXXXXXXXXXXXXXXXXX\nNro Matrícula: XXXXXXXXXXX\n-------------------------------------\nPrograma referente ao exercício 22\n-------------------------------------',)
renda = int(input('Insira o quanto você recebe para que o governo possa pegar seu dinheiro de você: '))
if renda <= 3000:
    print('Sorte sua! O imposto devido é de 0 reais')
elif renda <= 5000:
        imposto = (renda-3000)*0.1
        print('O imposto devido é de', imposto, 'reais')
else:
      imposto = (renda-5000)*0.15 + 200
      print('O seu imposto devido é de', imposto, 'reais')
print('-------------------------------------')
