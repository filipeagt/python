#No dicionário append não funciona, usar dados['chave'] = 'valor'
# apagar um elemnto del dados['chave']
filme = {
    'titulo': 'Satr Wars',
    'ano': 1977,
    'diretor': 'George Lucas'
}
print(filme.values())
print(filme.keys())
print(filme.items())
for k, v in filme.items():
    print(f'O {k} é {v}')
locadora = [filme]
print(locadora[0]['ano'])
print(locadora[0]['titulo'])
