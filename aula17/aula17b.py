valores = []
for x in range(5):
    valores.append(int(input('Digite um valor: ')))

for chave, valor in enumerate(valores):
    print(f'Na posição {chave} encontrei o valor {valor}!')
print('Cheguei ao final da lista.')
