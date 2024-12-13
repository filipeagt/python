lista = []
indiceAux = 0
for x in range(5):
    lista.append(int(input(f'Digite um número para a posição {x}: ')))
print('-='*30)
print(f'Você digitou os valores {lista}')
print(f'O maior valor digitado foi {max(lista)} na(s) posição(ões)', end=' ')
for x in range(lista.count(max(lista))):
    print(f'{lista.index(max(lista), indiceAux)}', end='... ')
    indiceAux = lista.index(max(lista), indiceAux) + 1
indiceAux = 0
print(f'\nO menor valor digitado foi {min(lista)} na(s) posição(ões)', end=' ')
for x in range(lista.count(min(lista))):
    print(f'{lista.index(min(lista), indiceAux)}', end='... ')
    indiceAux = lista.index(min(lista), indiceAux) + 1
print()
