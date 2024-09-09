from random import randint
from time import sleep
ale = randint(0, 10)
palpites = 1
num = int(input("Em qual número entre 0 e 10 eu pensei? "))
while (ale != num):
    print("Processando...")
    sleep(1)
    num = int(input("ERROU! Escolha outro número: "))
    palpites += 1
sleep(1)
print("Processando...")
print("Acertou! Eu pensei no número {} e foram necessários {} palpites para você acertar.".format(num, palpites))
