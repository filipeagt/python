print('='*30)
print(f'{"Caixa eletrônico":^30}')
print('='*30)
valor = int(input('Qual o valor a ser sacado? R$'))
n50 = valor // 50
n20 = valor % 50 // 20
n10 = valor % 50 % 20 // 10
n1  = valor % 50 % 20 % 10
print('='*30)
print(f'Saque realizado: ')
if n50 > 0:
    print(f'{n50} cédula(s) de R$50')
if n20 > 0:
    print(f'{n20} cédula(s) de R$20')
if n10 > 0:
    print(f'{n10} cédula(s) de R$10')
if n1 > 0:
    print(f'{n1} cédula(s) de R$1')
print('='*30)
print('Volte sempre! Tenha um bom dia!')
