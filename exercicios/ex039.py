from datetime import date
anoAtual = date.today().year
print('Alistamento Militar')
nascimento = int(input('Qual o ano de nascimento: '))
sexo = str(input('Sexo: (F, M)')).upper()
idade = anoAtual - nascimento
alistamento = nascimento + 18
print('Quem nasceu em {} faz {} anos em {}'.format(nascimento, idade, anoAtual))
if sexo == 'M':
    if(idade < 18):
        prazo = 18 - idade
        print('Você ainda vai se alistar, faltam {} anos'.format(prazo) if prazo > 1 else 'Você ainda vai se alistar, falta 1 ano')
        print('Seu alistamento será em {}'.format(alistamento))
    elif idade == 18:
        print('Está na hora de se alistar')
    else:
        prazo = idade - 18
        print('Passaram {} anos do prazo'.format(prazo) if prazo > 1 else 'Passou 1 ano do prazo')
        print('Seu alistamento foi em {}'.format(alistamento))
elif sexo == 'F':
    print('O alistamento NÃO é obrigatório para o sexo feminino.')
else:
    print('Opção inválida.')

