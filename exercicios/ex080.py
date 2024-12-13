numeros = []
for x in range(1, 6):
    num = int(input(f'Digite o {x}º número: '))
    if x == 1 or num > numeros[-1]:
        numeros.append(num)
        print(f'Valor {num} adicionado no final da lista...')
    else:
        for chave, valor in enumerate(numeros):
            if valor >= num:
                numeros.insert(chave, num)
                print(f'Valor {num} adicionado na posição {chave} da lista...')
                break
print('-='*30)
print(f'Os valores digitados em ordem foram: {numeros}')
