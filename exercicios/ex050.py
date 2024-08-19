soma = 0
cont = 0
for x in range(6):
    num =  int(input('Digite o {}º número: '.format(x+1)))
    if num%2 == 0:
        soma += num
        cont += 1
print('Você informou {} números pares e a soma deles foi {}.'.format(cont, soma))
