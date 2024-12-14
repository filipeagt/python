matriz = [[], [], []]
for linha in range(3):
    for coluna in range(3):
        matriz[linha].append(int(input(f'Digite o valor para [{linha}, {coluna}]: ')))
print('-='*30)
for linha in matriz:
    for item in linha:
        print(f'[ {item} ]', end='')
    print()
