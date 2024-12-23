def aumentar(valor=0, percentual=0):
	valor += valor * percentual / 100
	return valor
	

def diminuir(valor=0, percentual=0):
	valor -= valor * percentual / 100
	return valor
	
	
def metade(valor=0):
	return valor / 2
	
	
def dobro(valor=0):
	return valor * 2
	
	
def moeda(valor=0, moeda='R$'):
	return f'{moeda}{valor:.2f}'.replace('.', ',')
