num = input('Digite um número entre 0 e 9999: ')
num = num.zfill(4)
print('Analizando o número {}.'.format(num))
print('Unidade: {}'.format(num[3]))
print('Dezena:  {}'.format(num[2]))
print('Centena: {}'.format(num[1]))
print('Milhar:  {}'.format(num[0]))