matriz = [[0,0,0],[0,0,0],[0,0,0]]
determinate = 0
print('Calculadora de determinate de matriz 3x3')
for linha in range(3):
    for coluna in range(3):
        matriz[linha][coluna] = int(input('Digite um número da posição {},{}: '.format(linha, coluna)))

determinate += matriz[0][0]*matriz[1][1]*matriz[2][2]
determinate += matriz[0][1]*matriz[1][2]*matriz[2][0]
determinate += matriz[0][2]*matriz[1][0]*matriz[2][1]
determinate -= matriz[0][2]*matriz[1][1]*matriz[2][0]
determinate -= matriz[0][0]*matriz[1][2]*matriz[2][1]
determinate -= matriz[0][1]*matriz[1][0]*matriz[2][2]

for linha in range(3):
    print('|',end='')
    for coluna in range(3):
        print('{:^3}'.format(matriz[linha][coluna]),end='')
    print('|')
        
print('Determiante = {}'.format(determinate))
print('Tem inversa!' if determinate != 0 else 'Não tem inversa!')
