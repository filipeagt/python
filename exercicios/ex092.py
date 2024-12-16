from datetime import date
anoAtual = date.today().year
ctps = {}
ctps['nome'] = input('Nome: ')
nascimento = int(input('Ano de nascimento: '))
ctps['idade'] = anoAtual - nascimento
ctps['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))
if ctps['ctps'] != 0:
    ctps['contratacao'] = int(input('Ano de contratação: '))
    ctps['salario'] = float(input('Salário: R$ '))
    ctps['aposentadoria'] = ctps['contratacao'] + 35 - nascimento
print('-=' * 30)
print(ctps)
for chave, valor in ctps.items():
    print(f'    - {chave} tem o valor {valor}')
