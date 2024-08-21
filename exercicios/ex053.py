frase = input('Digite uma frase: ').strip().upper().split()
frase = ''.join(frase)
'''inverso = ''
i = -1
for letra in frase:
    inverso += frase[i]
    i-=1'''
inverso = frase[::-1]
print('O inverso de {} é {}.'.format(frase, inverso))
print('TEMOS UM PALÍNDROMO!' if frase==inverso else 'A frase digitada NÃO é um palíndromo!')
