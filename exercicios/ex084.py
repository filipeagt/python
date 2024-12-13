galera = []
pessoa = []
maiorPeso = menorPeso = 0
indicesMaiorPeso = []
indicesMenorPeso = []
while True:
    pessoa.append(input('Nome: '))
    pessoa.append(float(input('Peso: ')))
    galera.append(pessoa[:])
    pessoa.clear()
    opcao = input('Deseja continuar? [S/N] ').upper().strip()[0]
    if opcao == 'N':
        break
print('-='*30)
print(galera)
print(f'Foram cadastradas {len(galera)} pessoas.')
for indice, valor in enumerate(galera):
    if indice == 0:
        maiorPeso = menorPeso = valor[1]
    else:
        if valor[1] > maiorPeso:
            maiorPeso = valor[1]
        if valor[1] < menorPeso:
            menorPeso = valor[1]
print(f'O maior peso foi de {maiorPeso}kg. Peso de', end=' ')
for p in galera:
    if p[1] == maiorPeso:
        print(f'[{p[0]}]', end=' ')
print()
print(f'O menor peso foi de {menorPeso}kg. Peso de', end=' ')
for p in galera:
    if p[1] == menorPeso:
        print(f'[{p[0]}]', end=' ')
print()
