for pessoa in range(5):
    peso = float(input('Digite o peso da {}ª pessoa (kg): '.format(pessoa+1)))
    if pessoa == 0: #se estiver na primeira iteração
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O menor peso registrado foi {}kg e o maior foi {}kg.'.format(menor, maior))
