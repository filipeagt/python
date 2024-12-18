from random import randint
from time import sleep


def sorteia(lista):
    print('Sorteando 5 valores da lista: ', end='')
    for x in range(5):
        lista.append(randint(1, 10))
        sleep(0.5)
        print(f'{lista[x]}', end=' ', flush=True)
    print('PRONTO!')


def somaPar(lista):
    s = 0    
    for valor in lista:
        if valor % 2 == 0:
            s += valor
    print(f'Somando os valores pares de {lista}, temos {s}.')

    
numeros = []
sorteia(numeros)
somaPar(numeros)