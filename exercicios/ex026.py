frase = input('Digite uma frase: ').upper().strip()
print('A letra "A" aparece {} vezes na frase.'.format(frase.count('A')))
print('A letra "A" aparece pela primeira vez na posição {}, e pela última vez na posição {}.'.format(frase.find('A'), frase.rfind('A')))