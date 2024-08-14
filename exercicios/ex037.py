print('Calculadora de bases numéricas')
num =  int(input('Digite um número inteiro: '))
print('- Digite 1 para binário')
print('- Digite 2 para octal')
print('- Digite 3 para hexadecimal')
opcao = int(input('Opção: '))
if opcao == 1:
    print('O valor {} em binário é {}'.format(num, bin(num)[2:]))
elif opcao == 2:
    print('O valor {} em octal é {}'.format(num, oct(num)[2:]))
elif opcao == 3:
    print('O valor {} em hexadecimal é {}'.format(num, hex(num)[2:]))
else:
    print('Opção inválida')