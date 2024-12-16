pessoas = {'nome': 'Filipe', 'sexo': 'M', 'idade': 32}
print(f'O {pessoas["nome"]} tem {pessoas["idade"]}anos.')
pessoas['nome'] = 'Augusto'
pessoas['peso'] = 70.5
#del pessoas['sexo']
for k, v in pessoas.items():
    print(f'{k} = {v}')