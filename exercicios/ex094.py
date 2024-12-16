listaPessoas = []
listaMulheres = []
listaMaisVelhos = []
mediaIdade = 0
while True:
    pessoa = {}    
    pessoa['nome'] = input('Nome: ').strip()
    while True:
        sexo = input('Sexo [F/M]: ').strip().upper()[0]
        if sexo in 'FM':
            pessoa['sexo'] = sexo
            break
        print('ERRO! Por favor, digite apenas M ou F.')
    pessoa['idade'] = int(input('Idade: '))
    listaPessoas.append(pessoa)
    while True:
        opcao = input('Deseja continuar? [S/N] ').strip().upper()[0]
        if opcao in 'SN':
            break
        print('ERRO! Responda apena S ou N.')
    if opcao == 'N':
        break
print('-=' * 30)
print(f'- O grupo tem {len(listaPessoas)} pessoas cadastradas.')
for p in listaPessoas:
    mediaIdade += p['idade']
    if p['sexo'] == 'F':
        listaMulheres.append(p)
mediaIdade /= len(listaPessoas)
print(f'- A média de idade é de {mediaIdade} anos.')
print(f'- As mulheres cadastradas foram: ',end='')
for m in listaMulheres:
    print(f'{m["nome"]}', end=' ')
for p in listaPessoas:
    if p['idade'] > mediaIdade:
        listaMaisVelhos.append(p)
print(f'\n- Lista de pessoas acima da média de idade:')
for p in listaMaisVelhos:
    for k, v in p.items():
        print(f'    {k} = {v};', end=' ')
    print()
print('<< ENCERRADO >>')
