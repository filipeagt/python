cores = {'vermelho':'\033[1;31m', 'verde':'\033[1;32m', 'amarelo':'\033[1;33m', 'azul':'\033[1;34m', 'limpa':'\033[m'}
linha = '-=-'*10

print('{}{}\n    Minha Casa Minha Vida\n{}{}'.format(cores['azul'], linha, linha, cores['limpa']))

casa = float(input('Qual o valor da casa? '))
salario = float(input('Qual o salário? '))
anos = int(input('Quantos anos para pagar? '))
meses = anos * 12
prestacao = casa / meses
if prestacao <= salario*.30:
    print('Finaciamento {}APROVADO{} em {} meses com prestações de R${:.2f}'.format(cores['verde'], cores['limpa'], meses, prestacao))
else:
    print('Finaciamento {}REPROVADO{}, a prestação de R${:.2f} ultrapassa 30% do salário.'.format(cores['vermelho'], cores['limpa'], prestacao))