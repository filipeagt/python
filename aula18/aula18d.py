estado = dict()
brasil = list()
for c in range(3):
    estado['uf'] = input('Unidade Federativa: ')
    estado['sigla'] = input('Sigla do Estado: ')
    brasil.append(estado.copy())
    estado.clear()
for e in brasil:
    for v in e.values():
        print(v, end=' - ')
    print()
