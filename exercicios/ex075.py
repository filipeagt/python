lista = []
for x in range(4):
    num = int(input('Digite um número: '))
    lista.append(num)
tupla = tuple(lista)
print(f'Você digitou os valores {tupla}')
print(f'O número 9 apareceu {tupla.count(9)} vezes.')
if 3 in tupla:
    print(f'O primeiro valor 3 foi digitado na {tupla.index(3)+1}ª posição.')
else:
    print('O valor 3 não foi digitado em nenhuma posição.')
print('Os números pares foram: ', end='')
for numero in tupla:
    if numero % 2 == 0:
        print(f'{numero} ', end='')
print()
