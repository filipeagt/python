valores = [[], []]
for x in range(1, 8):
    num = int(input(f'Digite o {x}º valor: '))
    if num % 2 == 0:
        valores[0].append(num)
    else:
        valores[1].append(num)
print('-='*30)
print(valores)
print(f'Valores pares: {sorted(valores[0])}')
print(f'Valores ímpares: {sorted(valores[1])}')
