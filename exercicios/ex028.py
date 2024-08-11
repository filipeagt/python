from random import randint
aleatorio = randint(0,5)
num = int(input('Pensei num número entre 0 e 5, tente adivinhar... '))
print('Acertou Mizeravi!' if num == aleatorio else 'ERROU!')