def ficha(nome='<desconhecido>', gols=0):
    if nome == '':
        nome = '<desconhecido>'
    if gols == '':
        gols = 0
    print(f'O jogador {nome} fez {gols} gol(s) no campeonato.')

print('-' * 30)
nome = input('Nome do jogador: ').strip()
numero = input('Número de gols: ').strip()
ficha(nome, numero)
