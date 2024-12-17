from time import sleep
def contador(inicio, fim, passo):
    passo = abs(passo) if passo != 0 else 1
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
    for x in range(inicio, (fim + 1) if fim >= inicio else (fim - 1), passo if fim >= inicio else -passo):
        sleep(0.5)
        print(x, end=' ', flush=True)
    print('FIM!')



def linha():
    print('-=' * 20)


linha()
contador(1, 10, 1)
linha()
contador(10, 0, 2)
linha()
print('Agora é sua vez de personalizar a contagem!')
i = int(input('Início: '))
f = int(input('Fim:    '))
p = int(input('Passo:  '))
linha()
contador(i, f, p)
