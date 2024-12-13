numeros = list()
while True:
    numeros.append(int(input(f'Digite o {len(numeros)+1}º número: ')))
    while True:
        opcao = input('Deseja continuar? [S/N] ').strip().upper()[0]
        if opcao in 'SN':
            break
        else:
            print('Opção inválida!',end=' ')
    if opcao == 'N':
        break
print('-='*30)
print(f'Os número digitados foram {numeros}')
print(f'Foram digitados {len(numeros)} números.')
print(f'Lista de valores em ordem decrescente {sorted(numeros, reverse=True)}')
if 5 in numeros:
    print(f'O valor 5 aparece na(s) posição(ões) ', end='')
    for chave, valor in enumerate(numeros):
        if valor == 5:
            print(f'{chave}', end=' ')
    print('da lista.')
else:
    print(f'O valor 5 não aparece na lista.')
