print('Calculadora de bases numéricas')
num =  int(input('Digite um número inteiro: '))
print('Escolha uma das bases para conversão:')
print('[ 1 ] converter para binário')
print('[ 2 ] converter para octal')
print('[ 3 ] converter para hexadecimal')
opcao = int(input('Opção: '))
if opcao == 1:
    print('O valor {} em binário é {}'.format(num, bin(num)[2:]))
elif opcao == 2:
    print('O valor {} em octal é {}'.format(num, oct(num)[2:]))
elif opcao == 3:
    print('O valor {} em hexadecimal é {}'.format(num, hex(num)[2:].upper()))
else:
    print('Opção inválida')