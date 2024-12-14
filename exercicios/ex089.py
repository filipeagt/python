listaAlunos = []
while True:
    aluno = []
    notas = []
    aluno.append(input('Nome do aluno: '))
    notas.append(float(input('Nota 1: ')))
    notas.append(float(input('Nota 2: ')))
    aluno.append(notas)
    listaAlunos.append(aluno)
    opcao = input('Quer continuar? [S/N] ').strip().upper()[0]
    if opcao == 'N':
        break
print('-='*15)
print('Nº  NOME           MÉDIA')
print('-'*30)
for num, aluno in enumerate(listaAlunos):
    print(f'{num:<3} {aluno[0]:<14} {(aluno[1][0] + aluno[1][1]) / 2:>5.1f}')
print('-'*30)
while True:
    nAluno = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if nAluno == 999:
        break
    if nAluno >= len(listaAlunos):
        print('Aluno não encontrado.')
        continue
    print(f'Notas de {listaAlunos[nAluno][0]} são {listaAlunos[nAluno][1]}')
    print('-'*30)
print('FINALIZANDO...\n<<< VOLTE SEMPRE >>>')
