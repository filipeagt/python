from math import sqrt, trunc
num = int(input('Digite um número:'))
raiz = sqrt(num)
print('A raiz de {} é igual a {:.2f}'.format(num, trunc(raiz)))