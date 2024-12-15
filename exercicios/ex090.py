aluno = {}
aluno['nome'] = input('Nome do aluno: ')
aluno['média'] = float(input(f'Média de {aluno["nome"]}: '))
if aluno['média'] >= 7:
    aluno['situação'] = 'APROVADO'
elif aluno['média'] >= 5:
    aluno['situação'] = 'RECUPERAÇÃO'
elif aluno['média'] < 5:
    aluno['situação'] = 'REPROVADO'
print('-=' * 30)
for chave, valor in aluno.items():
    print(f'  - {chave.capitalize()} é igual a {valor}')
