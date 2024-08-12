linha = '-=-'*10
print(linha)
print('Analisador de trângulos')
print(linha)
r1 = float(input('Comprimento da primeira reta: '))
r2 = float(input('Comprimento da segunada reta: '))
r3 = float(input('Comprimento da terceira reta: '))
if r1>=r2+r3 or r2>=r1+r3 or r3>=r1+r2:
    print('As retas {}, {} e {}, não podem formar um triângulo.'.format(r1, r2, r3))
else:
    print('As retas {}, {} e {}, formam um triângulo.'.format(r1, r2, r3))