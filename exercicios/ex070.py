produtos = []
maisBararto = CustaMaisDeMil = total = 0
nomeMaisBarato = ''
print('=-'*10)
print('Carrinho de Compras')
print('=-'*10)
while True:
    nome = input('Nome: ').strip()
    preço = float(input('Preço (R$): '))
    produtos.append({'nome': nome, 'preço': preço})
    continuar = ''
    while True:
        continuar = input('Deseja continuar? [S/N] ').upper().strip()[0]
        if continuar in 'SN':
            print('-'*20)
            break
    if continuar == 'N':
        break
for produto in produtos:
    total += produto['preço']
    if produto['preço'] > 1000:
        CustaMaisDeMil += 1
    if produto == produtos[0]: #Primeira iteração
        maisBararto = produto['preço']
        nomeMaisBarato = produto['nome']
    else: #Demais iterações
        if produto['preço'] < maisBararto:
            maisBararto = produto['preço']
            nomeMaisBarato = produto['nome']
print('-'*10, f'FIM DO PROGRAMA', '-'*10)
print(f'O total gasto na compra foi R${total:.2f}.'.replace('.',',',1))
print(f'{CustaMaisDeMil} produto(s) custa(m) mais de R$1000,00.')
print(f'O produto "{nomeMaisBarato}" foi o mais barato custando R${maisBararto:.2f}.'.replace('.', ',', 1))
