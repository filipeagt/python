print('='*25)
print('{:^25}'.format('10 Termos de uma PA'))
print('='*25)
num = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
i = 0
while i < 10:
    print('{} =>'.format(num), end=' ')
    num += razao
    i += 1
print('FIM!')
