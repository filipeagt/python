matriz = [[], [], []]
somaPares = somaColuna3 = maiorLinha2 = 0
for linha in range(3):
    for coluna in range(3):
        matriz[linha].append(int(input(f'Digite o valor para [{linha}, {coluna}]: ')))
print('-='*30)
for linha, lista in enumerate(matriz):
    for coluna, item in enumerate(lista):
        if item % 2 == 0:
            somaPares += item
        if coluna == 2:
            somaColuna3 += item
        print(f'[{item:^5}]', end='')
    print()
print(f'Soma dos valores pares: {somaPares}')
print(f'Soma dos valores da 3ª coluna: {somaColuna3}')
print(f'Maior valor da segunda linha: {max(matriz[1])}')
