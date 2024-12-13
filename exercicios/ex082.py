numeros = list()
pares = []
impares = []
while True:
    numeros.append(int(input(f'Digite o {len(numeros)+1} º valor: ')))
    opcao = ' '
    while opcao not in 'SN':
        opcao = input('Deseja continuar? [S/N] ').upper().strip()[0]
    if opcao == 'N':
        break
for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)
print('-='*30)
print(f'Números digitados: {numeros}')
print(f'números pares: {pares}')
print(f'Números ímpares: {impares}')
