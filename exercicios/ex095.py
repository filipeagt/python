listaJogadores = []
while True:
    jogador = {}
    partidas = []
    jogador['nome'] = input('Nome do jogador: ').strip()
    nPartidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    for x in range(nPartidas):
        partidas.append(int(input(f'Quantos gols na partida {x}? ')))
    jogador['gols'] = partidas
    jogador['total'] = sum(partidas)
    opção = input('Quer continuar? [S/N] ').strip().upper()[0]
    listaJogadores.append(jogador)
    if opção == 'N':
        break
print('-=' * 30)
print('cod nome          gols            total')
print('-' * 40)
for i, j in enumerate(listaJogadores):
    print(f'{i:>3} {j["nome"]:<14}{str(j["gols"]):<15} {j["total"]}')
print('-' * 40)
while True:
    cod = int(input('Mostrar dados de qual jogador? '))
    if cod == 999:
        break
    elif cod < len(listaJogadores):
        print(f'--- LEVANTAMENTO DO JOGADOR {listaJogadores[cod]["nome"]}:')
        for num, gols in enumerate(listaJogadores[cod]["gols"]):
            print(f'    No jogo {num} fez {gols} gols.')
        print('-' * 40)
    elif cod >= len(listaJogadores):
        print(f'ERRO! Não existe jogador com código {cod}! Tente novamente.')
        print('-' * 40)
print('<<< VOLTE SEMPRE! >>>')
