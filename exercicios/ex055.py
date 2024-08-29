for pessoa in range(1, 6):
    peso = float(input('Digite o peso da {}ª pessoa (kg): '.format(pessoa)))
    if pessoa == 1: #se estiver na primeira iteração
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O menor peso registrado foi {}kg e o maior foi {}kg.'.format(menor, maior))
