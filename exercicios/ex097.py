def escreva(texto):
    comprimento = len(texto) + 4
    print('~' * comprimento)
    print(f'  {texto}  ')
    print('~' * comprimento)


escreva('Olá, Mundo!')
escreva('Curso de Python no YouTube')
