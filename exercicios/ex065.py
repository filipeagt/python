continuar = 'S'
soma = 0
cont = 0
maior = 0
menor = 0
inicio = True

while continuar == 'S':
    n = int(input('Digite um número: '))
    cont += 1
    soma += n
    if inicio:
        inicio = False
        maior = n
        menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    continuar = input('Quer continuar? [S/N] ').upper()
print('A média dos valores digitados foi {}'.format(soma/cont))
print('O maior valor digitado foi {} e o menor foi {}'.format(maior, menor))
