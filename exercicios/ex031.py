dist = int(input('Informe a distância da viagem em km: '))
if dist <= 200:
    passagem  = dist * .50
else:
    passagem = dist * .45
print('O valor da passagem será {:.2f}.'.format(passagem))