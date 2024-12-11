produtos = []
maisBararto = CustaMaisDeMil = total = 0
nomeMaisBarato = ''
print('=-'*20)
print(f'{"Carrinho de Compras":^40}')
print('=-'*20)
while True:
    nome = input('Nome do produto: ').strip().capitalize()
    preço = float(input('Preço: R$ '))
    produtos.append({'nome': nome, 'preço': preço})
    continuar = ' '
    while continuar not in 'SN':
        continuar = input('Deseja continuar? [S/N] ').upper().strip()[0]
    print('-'*40)
    if continuar == 'N':
        break
for produto in produtos:
    total += produto['preço']
    if produto['preço'] > 1000:
        CustaMaisDeMil += 1
    if produto == produtos[0] or produto['preço'] < maisBararto: #Primeira iteração ou nas demais iterações se o preço for menor
        maisBararto = produto['preço']
        nomeMaisBarato = produto['nome']
print(f'{" FIM DO PROGRAMA ":-^40}')
print(f'O total gasto na compra foi R${total:.2f}.'.replace('.',',',1))
print(f'Temos {CustaMaisDeMil} produto(s) que custa(m) mais de R$1000,00.')
print(f'O produto "{nomeMaisBarato}" foi o mais barato custando R${maisBararto:.2f}.'.replace('.', ',', 1))
