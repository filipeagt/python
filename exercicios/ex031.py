dist = int(input('Informe a distância da viagem em km: '))
print('Você está prestes a começar uma viagem de {}km.'.format(dist))
if dist <= 200:
    passagem  = dist * .50
else:
    passagem = dist * .45
print('O valor da passagem será R${:.2f}.'.format(passagem))