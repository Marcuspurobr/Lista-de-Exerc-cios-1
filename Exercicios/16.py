print('Aluno: XXXXXXXXXXXXXXXXXXXXXXXXXXXXX\nNro Matrícula: XXXXXXXXXXX\n-------------------------------------\nPrograma referente ao exercício 16\n-------------------------------------',)
n1 = int(input('Entre com o 1° número: '))
n2 = int(input('Entre com o 2° número: '))
n3 = int(input('Entre com o 3° número: '))
n4 = int(input('Entre com o 4° número: '))
n5 = int(input('Entre com o 5° número: '))
l = [n1,n2,n3,n4,n5]
ln = []
for _ in range(5):
    menor = l[0]
    i = 0
    for d in l:
        if d < menor:
            menor = d
            i = l.index(menor)
            print(i)
    l.remove(l[i])
    print(l)
    ln.append(menor)
    print(ln)
print('Os número em ordem crescente são: ', ln)
print('-------------------------------------')
