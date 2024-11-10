print('='*25)
print('{:^25}'.format('10 Termos de uma PA'))
print('='*25)
num = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
qtd = 10
while qtd != 0:
    for x in range(qtd):
        print('{} =>'.format(num), end=' ')
        num += razao
    qtd = int(input('Você quer mostrar mais quantos números? '))
