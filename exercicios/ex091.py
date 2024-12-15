from random import randint
from time import sleep
jogadas = {}
ordenadas = {}
values = []
print('Valores sorteados:')
for x in range(1, 5):
    num = randint(1, 6)
    jogadas[f'jogador{x}'] = num
    values.append(num)
    sleep(1)
    print(f'    O jogador{x} tirou {num}')
values.sort(reverse=True)
print('Ranking dos jogadores:')
for indice, valor in enumerate(values):
    for k, v, in jogadas.items():
        if valor == v and k not in ordenadas.keys():
            ordenadas[k] = v
            sleep(1)
            print(f'    {indice+1}º lugar: {k} com {v}')
