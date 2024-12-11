print('-'*20)
print('Cadastro de pessoas')
print('-'*20)
pessoas = []
maiorIdade = homens = mulheresMenos20 = 0
while True:
    nome = input('Nome: ').strip()
    idade = int(input('Idade: '))
    continuar = sexo = ' '
    while sexo not in 'MF':
        sexo = input('Sexo [M/F]: ').upper().strip()[0]
    pessoas.append({'nome': nome, 'idade': idade, 'sexo': sexo})    
    while continuar not in 'SN':
        continuar = input('Deseja cadastar mais pessoas [S/N]: ').upper().strip()[0]
    if continuar == 'N':
        break
for pessoa in pessoas:
    if pessoa['idade'] >= 18:
        maiorIdade += 1
    if pessoa['sexo'] == 'M':
        homens += 1
    elif pessoa['idade'] < 20:
        mulheresMenos20 += 1
print(f'Cadastro de {len(pessoas)} pessoa(s) realizado com sucesso!')
print(f'{maiorIdade} maior(es) de 18 anos.') 
print(f'{homens} ', 'homem.' if homens == 1 else 'homens.')
print(f'{mulheresMenos20} mulher(es) com menos de 20 anos.')
