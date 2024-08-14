cores = {'vermelho':'\033[1;31m', 'verde':'\033[1;32m', 'amarelo':'\033[1;33m', 'azul':'\033[1;34m', 'limpa':'\033[m'}
linha = '-=-'*10
print('{}{}\nConfederação Nacional de Natação\n{}{}'.format(cores['azul'], linha, linha, cores['limpa']))
idade = int(input('Informe a idade do atleta: '))
if idade <= 9:
    categoria = 'MIRIM'
elif idade <= 14:
    categoria = 'INFANTIL'
elif idade <= 19:
    categoria = 'JUNIOR'
elif idade <= 20:
    categoria = 'SÊNIOR'
else:
    categoria = 'MASTER'
print('Categoria do atleta: {}'.format(categoria))