print('Cadastro de pessoas')
pessoas = list()
mediaIdade = 0
menos20 = 0
idadeVelho = 0
NCADASTROS = 4
for x in range(NCADASTROS):
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

print('Média das idadades: {} anos'.format(mediaIdade))
print('Homem mais velho: {}'.format(nomeVelho))
print('Mulheres com menos de 20 anos: {}'.format(menos20))
