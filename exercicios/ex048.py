soma = 0
nVal = 0
for x in range(3,501,3):
    if x%2 != 0:
        soma += x
        nVal += 1
print('A soma dos {} valores solicitados é {}.'.format(nVal, soma))
