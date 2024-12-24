def leiaInt(msg):
	while True:
		try:
			n = int(input(msg))
			return n
		except KeyboardInterrupt:
			print('O usuário preferiu não digitar esse número.')
			return 0
		except Exception:
		    print('\033[0;31mERRO! Digite um número inteiro válido.\033[m')

	
def leiaFloat(msg):
	while True:
		try:
			n = float(input(msg))
			return n
		except KeyboardInterrupt:
			print('O usuário preferiu não digitar esse número.')
			return 0
		except Exception:
		    print('\033[0;31mERRO! Digite um número real válido.\033[m')


#Programa Principal
inteiro = leiaInt('Digite um Inteiro: ')
real = leiaFloat('Digite um Real: ')
print(f'O valor inteiro digitado foi {inteiro} e o real foi {real}')
