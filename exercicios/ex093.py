jogador = {}
partidas = []
jogador['nome'] = input('Nome do jogador: ').strip()
nPartidas = int(input(f'    Quantas partidas {jogador["nome"]} jogou? '))
for x in range(nPartidas):
    partidas.append(int(input(f'    Quantos gols na partida {x}? ')))
jogador['gols'] = partidas
jogador['total'] = sum(partidas)
print('-=' * 30)
print(jogador)
print('-=' * 30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}.')
print('-=' * 30)
print(f'O jogador {jogador["nome"]} jogou {nPartidas} partidas.')
for num, gols in enumerate(partidas):
    print(f'    => Na partida {num}, fez {gols} gols.')
print(f'Foi um total de {jogador["total"]} gols.')
