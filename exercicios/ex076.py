listagem = (
    'Lápis', 1.75,
    'Borracha', 2.0, 
    'Caderno', 15.90, 
    'Estojo', 25.0, 
    'Trasnsferidor', 4.20, 
    'Compasso', 9.99, 
    'Mochila', 120.32, 
    'Canetas', 22.30, 
    'Livro', 34.9
)
print('-'*40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-'*40)
for indice in range(len(listagem)):
    if indice % 2 == 0:
        print(f'{listagem[indice]:.<30}', end='')
    else:
        print(f'R${listagem[indice]:7.2f}'.replace('.', ','))
print('-'*40)
