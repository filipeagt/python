num = int(input('Digite um número: '))
divisivel = 0
for x in range(1, num+1):
    if num % x == 0:
        print('\033[33m{}\033[m'.format(x),end=' ')
        divisivel += 1
    else:
        print('\033[31m{}\033[m'.format(x), end=' ')
print('\nO número {} foi divisível {} vezes.'.format(num, divisivel))
if divisivel == 2:
    print('E por isso ele é PRIMO!'.format(num))
else:
    print('E por isso ele NÃO é primo!'.format(num))
