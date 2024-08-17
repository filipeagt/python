soma = 0
for x in range(6):
    num =  int(input('Digite o {}º número: '.format(x+1)))
    if num%2 == 0:
        soma += num
print(soma)
