from random import randint
from time import sleep
print('-'*30)
print(f'{"JOGA NA MEGA SENA":^30}')
print('-'*30)
listaJogos = []
qtd = int(input('Quantos jogos você quer que eu sorteie? '))
for x in range(qtd):
    jogo = []
    while True:
        num = randint(1, 60)
        if num not in jogo:
            jogo.append(num)
        if len(jogo) == 6:
            break
    listaJogos.append(sorted(jogo))
print(f'-=-=-= SORTEANDO {qtd} JOGOS -=-=-=')
for indice, jogo in enumerate(listaJogos):
    print(f'Jogo {indice+1}: {jogo}')
    sleep(0.5)
print(f'-=-=-=-= < BOA SORTE > -=-=-=-=')
