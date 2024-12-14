aluno = {}
aluno['nome'] = input('Nome do aluno: ')
aluno['média'] = float(input(f'Média de {aluno["nome"]}: '))
aluno['situação'] = 'APROVADO' if aluno['média'] >= 7 else 'REPROVADO'
for chave, valor in aluno.items():
    print(f'{chave.capitalize()} é igual a {valor}')
