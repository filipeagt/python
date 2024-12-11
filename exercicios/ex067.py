while True:
    num = int(input("Qual tabuada vc quer ver? [digite um valor negativo para sair] "))
    print('-'*12)
    if num < 0:
        break    
    for x in range(1, 11):
        print(f'{num} x {x:2} = {num*x}')
    print('-'*12)
print('Programa da tabuada encerrado!')
