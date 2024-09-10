num = int(input('Digite um número: '))
fat = 1
cont = 1
while num >= cont:
    fat *= cont
    cont += 1
print('O fatorial de {} é {}'.format(num, fat))
