def voto(nascimento):
    from datetime import date
    idade = date.today().year - nascimento
    texto = 'VOTO '
    if idade < 16:
        texto += 'NEGADO'
    elif idade < 18:
        texto += 'OPCIONAL'
    elif idade < 65:
        texto += 'OBRIGATÓRIO'
    else:
        texto += 'OPCIONAL'
    return f'Com {idade} anos: {texto}.'


print('-' * 40)
ano = int(input('Em que ano você nasceu? '))
print(voto(ano))
