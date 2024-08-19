print('='*25)
print('{:^25}'.format('10 Termos de uma PA'))
print('='*25)
num = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
for x in range(10):
    print('{} =>'.format(num), end=' ')
    num += razao
print('Acabou')
