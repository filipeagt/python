from random import shuffle
lista = []
for x in range(4):
    lista.append(input('{}° aluno: '.format(x+1)))
shuffle(lista)
print('A ordem de apresentação será:\n{}'.format(lista))