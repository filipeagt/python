num = int(input('Digite um número: '))
paridade = 'PAR' if num%2 == 0 else 'ÍMPAR'
print('O número {} é {}!'.format(num, paridade))