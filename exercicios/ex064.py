n = 0
soma = 0
cont = 0

while n != 999:
    cont  += 1
    soma += n
    n = int(input('Digite um número: '))
    
print('Ao todo foram digitados {} números e a soma entre eles é {}'.format(cont-1, soma))
