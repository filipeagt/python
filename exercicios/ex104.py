def leiaInt(texto):
	while True:
		n = input(texto).strip()
		if n.isnumeric():
			n = int(n)
			break
		print('\033[0;31mERRO! Digite um número inteiro válido.\033[m')
	return n
	
	
#Programa Principal
num = leiaInt('Digite um valor: ')
print(f'Você acabou de digitar o número {num}.')
