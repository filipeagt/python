preco =  float(input('Qual o preço do produto? '))
print('Condições de pagamento:')
print('Digite 1 para à vista dinheiro')
print('Digite 2 para à vista cartão')
print('Digite 3 para até 2x no cartão')
print('Digite 4 para 3x ou mais no cartão')
condicao = int(input('Qual a condição desejada? '))

if condicao == 1:
    NovoPreco = preco * .9 #10% de desconto
elif condicao == 2:
    NovoPreco = preco * .95 #5% de desconto
elif condicao == 3:
    NovoPreco = preco #preço normal
elif condicao == 4:
    NovoPreco = preco * 1.2 #20% de juros

print('Valor final do produto R${:.2f}'.format(NovoPreco))
