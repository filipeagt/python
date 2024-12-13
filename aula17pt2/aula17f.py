galera = []
dado = []
totMaior = totMenor = 0
for c in range(3):
    dado.append(input('Nome: '))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:]) #importante criar cópia com [:], se não ao final vai exibir listas vazias
    dado.clear()
print(galera)
for pessoa in galera:
    if pessoa[1] >= 21:
        print(f'{pessoa[0]} é maior de idade.')
        totMaior += 1
    else:
        print(f'{pessoa[0]} é menor de idade.')
        totMenor += 1
print(f'Temos {totMaior} maiores e {totMenor} menores de idade.')