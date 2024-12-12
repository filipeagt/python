palavras = ('Lorem', 'ipsum', 'dolor', 'sit', 'amet', 'consectetur', 'adipisicing', 'elit')
for palavra in palavras:
    print(f'A palavra {palavra.upper()} possui as vogais: ', end='')
    for letra in palavra:
        if letra.lower() in 'aeiou':
            print(f'{letra} ', end='') 
    print()