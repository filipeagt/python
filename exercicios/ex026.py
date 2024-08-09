frase = input('Digite uma frase: ').upper()

for pos in range(len(frase)-1, -1, -1):    
    if frase[pos] == 'A':
        break

print('A letra "A" aparece {} vezes na frase.'.format(frase.count('A')))
print('A letra "A" aparece pela primeira vez na posição {}, e pela última vez na posição {}.'.format(frase.find('A'), pos))