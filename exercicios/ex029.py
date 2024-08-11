vel = float(input('Qual a velocidade do carro? (km/h) '))
if vel > 80:
    diferenca = vel - 80
    multa = diferenca * 7
    print('Você ultrapassou {}km/h do limite da via! MULTADO! R${:.2f}'.format(diferenca, multa))
