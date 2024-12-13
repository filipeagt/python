teste = list()
teste.append('Filipe')
teste.append(32)
galera = list()
galera.append(teste[:])
teste[0] = 'Taís'
teste[1] = 31
galera.append(teste[:])
print(galera)
