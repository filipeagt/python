print('='*25)
print('{:^25}'.format('10 Termos de uma PA'))
print('='*25)
num = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
qtd = 10
somatorio = 0
while qtd != 0:
    for x in range(qtd):
        print('{} =>'.format(num), end=' ')
        num += razao
        somatorio += 1
    qtd = int(input('PAUSA\nVocê quer mostrar mais quantos termos? '))
print('A progressão foi finalizada com {} termos mostrados.'.format(somatorio))
