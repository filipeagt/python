from random import randint
tupla = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print(f'Número sorteados: ', end='')
for num in tupla:
    print(num, end=' ')
print(f'\nO menor valor na tupla é {min(tupla)} e o maior é {max(tupla)}.')
