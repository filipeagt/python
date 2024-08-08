from math import hypot

co = float(input('Cateto oposto: '))
ca = float(input('Cateto adjacente: '))
hip = hypot(co, ca)
print('Um triângulo retângulo com os catetos medindo {} e {}, tem uma hipotenusa de {:.2f}'.format(co, ca, hip))