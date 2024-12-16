listaJogadores = []
while True:
    jogador = {}
    partidas = []
    jogador['nome'] = input('Nome do jogador: ').strip()
    nPartidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    for x in range(nPartidas):
        partidas.append(int(input(f'Quantos gols na partida {x+1}? ')))
    jogador['gols'] = partidas
    jogador['total'] = sum(partidas)
    listaJogadores.append(jogador)
    while True:
        opção = input('Quer continuar? [S/N] ').strip().upper()[0]
        if opção in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')    
    if opção == 'N':
        break
print('-=' * 30)
print('cod ', end='')
for chave in listaJogadores[0].keys():
    print(f'{chave:<15}', end='')
print()
print('-' * 40)
for i, j in enumerate(listaJogadores):
    print(f'{i:>3} {j["nome"]:<15}{str(j["gols"]):<15}{j["total"]}')
print('-' * 40)
while True:
    cod = int(input('Mostrar dados de qual jogador? (999 para parar)'))
    if cod == 999:
        break
    elif cod < len(listaJogadores):
        print(f'--- LEVANTAMENTO DO JOGADOR {listaJogadores[cod]["nome"]}:')
        for num, gols in enumerate(listaJogadores[cod]["gols"]):
            print(f'    No jogo {num+1} fez {gols} gols.')
        print('-' * 40)
    elif cod >= len(listaJogadores):
        print(f'ERRO! Não existe jogador com código {cod}! Tente novamente.')
        print('-' * 40)
print('<<< VOLTE SEMPRE! >>>')
