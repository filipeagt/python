from random import randint
vitorias = 0
print('=-'*15)
print('Vamos jogar par ou ímpar')
print('=-'*15)
while True:
    num = int(input('Diga um valor: '))
    cpu = randint(0, 10)    
    soma =  cpu + num
    jogador = ' '
    while jogador not in 'PI':
        jogador = input('Par ou Ímpar? [P/I] ').upper().strip()[0]
    resultado = 'PAR' if soma % 2 == 0 else 'ÍMPAR'
    print('-'*30)
    print(f'Você jogou {num} e o computador {cpu}. Total de {soma} deu {resultado}')
    print('-'*30)
    if resultado == 'PAR' and jogador == 'P' or resultado == 'ÍMPAR' and jogador == 'I':
        print('Você GANHOU!')
        print('=-'*15)
        vitorias += 1
    else:
        print('Você PERDEU!')
        break
    
print('=-'*15)
print(f'Game Over! Você venceu {vitorias} vez(es).')
