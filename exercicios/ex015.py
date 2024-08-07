dias = int(input('Quantos dias alugados? '))
km = float(input('Quantos km rodados? '))
preco =  60*dias + 0.15*km
print('O total a pagar é R${:.2f}'.format(preco))