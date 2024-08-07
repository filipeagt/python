print('Calculadora de tinta')
largura =  float(input('Digite a largura da parede (m): '))
altura = float(input('Digite a altura da parede (m): '))
area = largura * altura
tinta = area / 2 #Cada litro de tinta pinta 2m²
print('Sua parede tem a dimensão de {}x{} e sua área é de {:.2f}m².'.format(largura, altura, area))
print('Para pintar essa parede, você precisará de {:.2f}l de tinta.'.format(tinta))
