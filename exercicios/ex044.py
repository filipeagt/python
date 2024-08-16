print('{:=^40}'.format(' LOJAS ALMEIDA '))
preco =  float(input('Qual o preço dos produtos? R$'))
print('Condições de pagamento:')
print('[ 1 ] à vista dinheiro')
print('[ 2 ] à vista cartão')
print('[ 3 ] 2x no cartão')
print('[ 4 ] 3x ou mais no cartão')
condicao = int(input('Qual a condição desejada? '))

if condicao == 1:
    novoPreco = preco * .9 #10% de desconto
elif condicao == 2:
    novoPreco = preco * .95 #5% de desconto
elif condicao == 3:
    novoPreco = preco #preço normal
    prestacao = novoPreco / 2
    print('Sua compra será parcelada em 2x de R${:.2f} sem juros.'.format(prestacao))
elif condicao == 4:
    novoPreco = preco * 1.2 #20% de juros
    parcelas =  int(input('Quantas parcelas? '))
    prestacao = novoPreco / parcelas
    print('Sua compra será parcelada em {}x de R${:.2f} com juros.'.format(parcelas, prestacao))
else:
    novoPreco = preco
    print('\033[1;31mOPÇÃO DE PAGAMENTO INVÁLIDA!\033[m')

print('Valor final da compra R${:.2f}.'.format(novoPreco))
