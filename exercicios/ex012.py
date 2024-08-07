preço = float(input('Qual é o preço do produto: '))
desconto = preço*5/100
print('O produto que custava R${:.2f}, na promoção com 5% de desconto vai custar R${:.2f}'.format(preço, preço-desconto))