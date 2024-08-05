print('Calculadora de tinta')
largura =  float(input('Digite a largura da parede (m): '))
altura = float(input('Digite a altura da parede (m): '))
area = largura * altura
tinta = area / 2 #Cada litro de tinta pinta 2m²
print('Para pintar uma parede de {:.2f}m², você vai precisar de {:.2f} litros de tinta'. format(area, tinta))