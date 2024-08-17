from datetime import date
atual = date.today().year
menores = 0
maiores = 0
for pessoa in range(1, 8):
    nascimento = int(input('Ano de nascimento da {}ª pessoa: '.format(pessoa)))
    idade =  atual - nascimento
    print('Idade: {}'.format(idade))
    if idade >= 21:
        maiores += 1
    else:
        menores += 1
print('{} pessoas são maiores de idade e {} são menores de idade.'.format(maiores, menores))
