from random import randint
lista = []
menor = maior = 0
for x in range(5):
    lista.append(randint(0, 10))
    if x == 0:
        menor = maior = lista[x]
    else:
        if lista[x] < menor:
            menor = lista[x]
        if lista[x] > maior:
            maior = lista[x]
tupla = tuple(lista)
print(f'Número sorteados: {tupla}')
print(f'O menor valor na tupla é {menor} e o maior é {maior}.')
