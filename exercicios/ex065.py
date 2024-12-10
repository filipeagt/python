continuar = 'S'
soma = cont = media = maior = menor = 0
while continuar == 'S':
    n = int(input('Digite um número: '))
    cont += 1
    soma += n
    if cont == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    continuar = input('Quer continuar? [S/N] ').upper().strip()[0]
media =  soma / cont
print('Você digitou {} números e a média foi {}'.format(cont, media))
print('O maior valor digitado foi {} e o menor foi {}'.format(maior, menor))
