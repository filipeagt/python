def area(largura, comprimento):
    print(f'A área de um terreno {largura} x {comprimento} é de {largura * comprimento} m².')


# Program Principal
print(' Controle de Terrenos')
print('-' * 20)
largura = float(input('largura (m): '))
comprimento = float(input('COMPRIMENTO (m): '))
area(largura, comprimento)
