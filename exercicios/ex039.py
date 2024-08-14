from datetime import date
anoAtual = date.today().year
print('Alistamento Militar')
nascimento = int(input('Qual o ano de nascimento: '))
idade = anoAtual - nascimento
if(idade < 18):
    prazo = 18 - idade
    print('Você ainda vai se alistar, faltam {} anos'.format(prazo) if prazo > 1 else 'Você ainda vai se alistar, falta 1 ano')
elif idade == 18:
    print('Está na hora de se alistar')
else:
    prazo = idade - 18
    print('Passaram {} anos do prazo'.format(prazo) if prazo > 1 else 'Passou 1 ano do prazo')