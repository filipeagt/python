cores = {'vermelho':'\033[1;31m', 'verde':'\033[1;32m', 'amarelo':'\033[1;33m', 'azul':'\033[1;34m', 'limpa':'\033[m'}
linha = '-=-'*10
print('{}{}\n      Calculo de média\n{}{}'.format(cores['azul'], linha, linha, cores['limpa']))
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a seguda nota: '))
media  = (n1 + n2) / 2
print('Tirando {:.1f} e {:.1f}, a média do aluno é {:.1f}'.format(n1, n2, media))
if media < 5:
    print('{}REPROVADO{}'.format(cores['vermelho'], cores['limpa']))
elif media < 7:
    print('{}RECUPERAÇÃO{}'.format(cores['amarelo'], cores['limpa']))
else:
    print('{}APROVADO{}'.format(cores['verde'], cores['limpa']))