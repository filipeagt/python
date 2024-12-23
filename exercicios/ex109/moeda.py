def moeda(valor=0, moeda='R$'):
	return f'{moeda}{valor:.2f}'.replace('.', ',')


def aumentar(valor=0, percentual=0, format=False):
	valor += valor * percentual / 100
	return moeda(valor) if format else valor
	

def diminuir(valor=0, percentual=0, format=False):
	valor -= valor * percentual / 100
	return moeda(valor) if format else valor
	
	
def metade(valor=0, format=False):
	return moeda(valor / 2) if format else valor / 2
	
	
def dobro(valor=0, format=False):
	return moeda(valor * 2) if format else valor * 2
