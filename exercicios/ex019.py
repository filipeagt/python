from random import choice

lista = list()
for x in range(4):
    lista.append(input('{}º aluno: '.format(x+1)))

sorteado = choice(lista)
print('O aluno sorteado foi {}'.format(sorteado))