from random import choice
lista = []
for x in range(4):
    lista.append(input('{}° aluno: '.format(x+1)))

for x in range(4):
    sorteado = choice(lista)
    print('{}° sorteado: {}'.format(x+1, sorteado))
    lista.remove(sorteado)