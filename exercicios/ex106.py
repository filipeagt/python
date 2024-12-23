from time import sleep


def escreva(texto, cor=''):
	comprimento = len(texto) + 4
	print(f'\033[{cor}m', end='')
	print('~' * comprimento)
	print(f'  {texto}  ')
	print('~' * comprimento)
	print('\033[m', end='')
	sleep(1)


def ajuda():
	while True:
		escreva('Sistema de ajuda PyHELP', '0;30;42')
		palavra = input('Função ou Biblioteca > ').strip().lower()
		if palavra == 'fim':
			escreva('ATÉ LOGO!', '0;30;41')
			break
		escreva(f"Acessando o manual do comando '{palavra}'", '0;30;44')
		print('\033[7;30m', end='')
		help(palavra)
		print('\033[m', end='')
		sleep(2)
	
ajuda()
