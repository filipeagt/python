def escreva(texto, cor=''):
	comprimento = len(texto) + 4
	print(f'\033[{cor}m', end='')
	print('~' * comprimento)
	print(f'  {texto}  ')
	print('~' * comprimento)
	print('\033[m', end='')


def ajuda():
	while True:
		escreva('Sistema de ajuda PyHELP', '7;32;47')
		palavra = input('Função ou Biblioteca > ').strip().lower()
		if palavra == 'fim':
			escreva('ATÉ LOGO!', '7;31;47')
			break
		escreva(f"Acessando o manual do comando '{palavra}'", '7;34;47')
		print('\033[7;30m', end='')
		help(palavra)
		print('\033[m', end='')
	
ajuda()
