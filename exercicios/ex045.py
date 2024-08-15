from random import randint
print('-=-'*5)
print('{:^23}'.format('\033[34mJOKENPO\033[m'))
print('-=-'*5)
jokenpo = {1:'PEDRA', 2:'PAPEL', 3:'TESOURA'}
jogador = int(input('Digite 1 para pedra, 2 para papel ou 3 para tesoura: '))
computador = randint(1, 3)
print('Você escolheu {} e o computador escolheu {}.'.format(jokenpo[jogador], jokenpo[computador]))
if jogador == computador:
    print('\033[1;33mEmpatou!!!\033[m')
elif computador==1 and jogador==3 or computador==2 and jogador==1 or computador==3 and jogador==2:
    print('\033[1;31mVocê perdeu!!!\033[m')
else:
    print('\033[1;32mVocê ganhou!!!\033[m')
