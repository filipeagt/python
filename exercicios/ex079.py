numeros = []
while True:
    num = int(input('Digite um número: '))
    opcao = ' '
    if num in numeros:
        print('Valor duplicado. Não vou adicionar...')
    else:
        numeros.append(num)
        print('Valor adicionado com sucesso...')
    while opcao not in 'SN':
        opcao = input('Quer continuar? [S/N] ').upper().strip()[0]
    if opcao == 'N':
        break
print('-='*30)
print(f'Os valores únicos digitados em ordem crescente foram: {sorted(numeros)}')
