from random import randint
soma = vitorias = num = cpu = 0
resultado = jogador = ''
print('=-'*15)
print('Vamos jogar par ou ímpar')
print('=-'*15)
while True:
    num = int(input('Diga um valor: '))
    cpu = randint(1, 10)
    jogador = input('Par ou Ímpar? [P/I] ').upper().strip()[0]
    soma =  cpu + num
    resultado = 'PAR' if soma % 2 == 0 else 'ÍMPAR'
    print('-'*15)
    print(f'Você jogou {num} e o computador {cpu}. Total de {soma} deu {resultado}')
    print('-'*15)
    if resultado == 'PAR' and jogador == 'I' or resultado == 'ÍMPAR' and jogador == 'P':
        break
    else:
        vitorias += 1
print('=-'*20)
print(f'Game Over! Você venceu {vitorias} vezes.')
