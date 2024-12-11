num = 0
while True:
    num = int(input("Qual tabuada vc quer ver? [digite -1 para sair]"))
    if num < 0:
        break
    print('-'*12)
    for x in range(1, 11):
        print(f'{num} x {x:2} = {num*x}')
    print('-'*12)
print('Programa da tabuada encerrado!')
