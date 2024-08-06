n = int(input('Digite um número para ver sua tabuada: '))
linha = 12*'='
print(linha)
for x in range(1,11):
    print('{} x {:2} = {}'.format(n, x, x*n))
print(linha)