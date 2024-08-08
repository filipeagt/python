from math import sin, cos, tan, radians
angulo = float(input('Digite um ângulo: '))
radiano = radians(angulo)
seno = sin(radiano)
coseno = cos(radiano)
tangente = tan(radiano)
print('O angulo {}° possui: \nSeno = {:.2f} \nCosseno = {:.2f} \nTangente = {:.2f}'.format(angulo, seno, coseno, tangente))
