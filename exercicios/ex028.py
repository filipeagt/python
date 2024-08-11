from random import randint
from time import sleep
aleatorio = randint(0, 5)
linha = '-=-'*20
print(linha)
print('Vou pensar em um número entre 0 e 5, tente adivinhar... ')
print(linha)
num = int(input('Em que número eu pensei? '))
print('PROCESSANDO...')
sleep(2)
print('Acertou Mizeravi!' if num == aleatorio else 'ERROU!')
print('Pensei no número {}.'.format(aleatorio))