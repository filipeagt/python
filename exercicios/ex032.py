from datetime import date
ano = int(input('Informe um ano ou coloque 0 para analisar o ano atual): '))
if ano == 0:
    ano = date.today().year
if ano % 4 != 0 or ano % 100 == 0 and ano % 400 != 0:
    print('O ano de {} não é bissexto'.format(ano))
else:
    print('O ano de {} é bissexto'.format(ano))
