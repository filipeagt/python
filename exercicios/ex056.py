print('Cadastro de pessoas')
pessoas = list()
mediaIdade = 0
menos20 = 0
idadeVelho = 0
NCADASTROS = 4
for x in range(NCADASTROS):
    print('----- {}ª Pessoa -----'.format(x+1))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo (F ou M): ')).upper().strip()
    pessoas.append({'nome':nome, 'idade':idade, 'sexo':sexo})

for pessoa in pessoas:
    mediaIdade += pessoa['idade']
    if pessoa['sexo'] == 'F' and pessoa['idade'] < 20:
        menos20 += 1
    if pessoa['sexo'] == 'M' and pessoa['idade'] > idadeVelho:
        idadeVelho = pessoa['idade']
        nomeVelho = pessoa['nome']
mediaIdade /= NCADASTROS

print('A média das idadades é {} anos.'.format(mediaIdade))
print('O homem mais velho tem {} anos e se chama {}.'.format(idadeVelho, nomeVelho))
print('Existem {} mulheres com menos de 20 anos no grupo.'.format(menos20))
