def moeda(valor=0, moeda='R$'):
	return f'{moeda}{valor:.2f}'.replace('.', ',')


def aumentar(valor=0, percentual=0, format=False):
	"""
	=> Calcula o aumento de um determinado preço,
	retornando oresultado com ou sem formatação.
	:param valor: o preço que se quer reajustar.
	:param percentual: qual é a a porcentagem do aumento.
	:param format: quer a saída formatada ou não?
	:return: o valor reajustado com ou sem formato.
	"""
	valor += valor * percentual / 100
	return moeda(valor) if format else valor
	

def diminuir(valor=0, percentual=0, format=False):
	valor -= valor * percentual / 100
	return moeda(valor) if format else valor
	
	
def metade(valor=0, format=False):
	return moeda(valor / 2) if format else valor / 2
	
	
def dobro(valor=0, format=False):
	return moeda(valor * 2) if format else valor * 2
	

def resumo(valor=0, aumento=10, desconto=5):
	print('-' * 30)
	print(f'{"RESUMO DO VALOR":^30}')
	print('-' * 30)
	print(f'{"Preço analisado":<20} {moeda(valor)}')
	print(f'{"Dobro do preço":<20} {dobro(valor, True)}')
	print(f'{"Metade do preço":<20} {metade(valor, True)}')
	print(f'{f"{aumento}% de aumento":<20} {aumentar(valor, aumento, True)}')
	print(f'{f"{desconto}% de redução":<20} {diminuir(valor, desconto, True)}')
	print('-' * 30)
