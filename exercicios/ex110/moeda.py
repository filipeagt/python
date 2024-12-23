def moeda(valor):
	return f'R${valor:.2f}'.replace('.', ',')


def aumentar(valor, percentual, format=False):
	valor += valor * percentual / 100
	return moeda(valor) if format else valor
	

def diminuir(valor, percentual, format=False):
	valor -= valor * percentual / 100
	return moeda(valor) if format else valor
	
	
def metade(valor, format=False):
	return moeda(valor / 2) if format else valor / 2
	
	
def dobro(valor, format=False):
	return moeda(valor * 2) if format else valor * 2
	

def resumo(valor, aumento, desconto):
	print('-' * 30)
	print(f'{"RESUMO DO VALOR":^30}')
	print('-' * 30)
	print(f'{"Preço analisado":<20} {moeda(valor)}')
	print(f'{"Dobro do preço":<20} {dobro(valor, True)}')
	print(f'{"Metade do preço":<20} {metade(valor, True)}')
	print(f'{f"{aumento}% de aumento":<20} {aumentar(valor, aumento, True)}')
	print(f'{f"{desconto}% de redução":<20} {diminuir(valor, desconto, True)}')
	print('-' * 30)