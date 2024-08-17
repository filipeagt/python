frase = input('Digite uma frase: ').strip().upper().split()
frase = ''.join(frase)
i = -1
palindromo = True
for letra in frase:
    if letra != frase[i]:
        palindromo = False
        break
    i-=1
print('É UM PALÍNDROMO!' if palindromo else 'NÃO É UM PALÍNDROMO!')
