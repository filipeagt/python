num = int(input('Digite um número para calcular seu fatorial: '))
fat = 1
print('Calculando {}! = {} '.format(num, num), end='')
while num > 1:
    fat *= num
    num -= 1
    print('x {} '.format(num), end='')
print('= {}'.format(fat))
