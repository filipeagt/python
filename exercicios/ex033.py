numeros = []
for x in range(3):
    numeros.append(int(input('Informe o {}º número: '.format(x+1))))
print('O menor número é {}'.format(min(numeros)))
print('O maior número é {}'.format(max(numeros)))
