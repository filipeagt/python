from time import sleep


def linha():
    print('-=' * 20)


def contador(inicio, fim, passo):
    passo = abs(passo) if passo != 0 else 1
    linha()
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
    sleep(2)
    for x in range(inicio, (fim + 1) if fim >= inicio else (fim - 1), passo if fim >= inicio else -passo):
        sleep(0.5)
        print(x, end=' ', flush=True)
    print('FIM!')


contador(1, 10, 1)
contador(10, 0, 2)
linha()
print('Agora é sua vez de personalizar a contagem!')
i = int(input('Início: '))
f = int(input('Fim:    '))
p = int(input('Passo:  '))
contador(i, f, p)
