opcao = 4
while (opcao != 5):
    num1 = int(input('Digite um número: '))
    num2 =  int(input('Digite outro número: '))
    opcao = int(input('----Menu----\n[1]somar\n[2]multiplicar\n[3]maior\n[4]novos números\n[5]sair\n'))
    if opcao == 1:
        print('A soma entre {} e {} é igual a {}.'.format(num1, num2, num1 + num2))
    elif opcao == 2:
        print('A multiplicação entre {} e {} é igual a {}.'.format(num1, num2, num1 * num2))
    elif opcao == 3:
        maior = num1
        if num2 > maior:
            maior = num2
        print('O maior valor entre {} e {} é {}'.format(num1, num2, maior))
    elif opcao == 4:
        print('Escolha novos valores!')
        continue
    elif opcao == 5:
        print('Até logo!')
        break
    else:
        print('Opção inválida!')