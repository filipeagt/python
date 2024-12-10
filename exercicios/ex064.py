soma = cont = 0
num = int(input('Digite um número [999 para parar]: '))
while num != 999:
    cont  += 1
    soma += num
    num = int(input('Digite um número [999 para parar]: '))
    
print('Ao todo foram digitados {} números e a soma entre eles é {}'.format(cont, soma))
