def escrever():
    titulo('NOVO CADASTRO')
    nome = input('Nome: ')
    while True:
        try:
            idade = int(input('Idade: '))
            break
        except:
            erro('Digite um número inteiro válido.')
    try:
        arquivo = open('dados.txt', 'a+')
        arquivo.write(f'{nome:<30}{idade} anos\n')
        arquivo.close()
        print(f'Novo registro de {nome} adicionado.')
    except:
        erro('Não foi possível abrir o arquivo!')


def ler():
    titulo('PESSOAS CADASTRADAS')
    try:
        arquivo = open('dados.txt', 'r')
        print(arquivo.read())
        arquivo.close()
    except:
        erro('Não foi possível abrir o arquivo')
        

def menu():
    while True:
        titulo('MENU PRINCIPAL')
        opcao(1, 'Ver pessoas cadastradas')
        opcao(2, 'Cadastrar nova Pessoa')
        opcao(3, 'Sair do sistema')
        linha()
        while True:
            try:
                escolha = int(input('\033[0;33mSua Opção: \033[m'))
                if escolha in (1, 2, 3):
                    break
                erro(f'Escolha uma opção entre 1 e 3.')
            except:
                erro(f'{escolha} não é uma opção válida.')
        if escolha == 1:
            ler()
        elif escolha == 2:
            escrever()
        elif escolha == 3:
            titulo('Saindo do sistema... Até logo!')
            break

    

def titulo(msg):
    linha()
    print(f'{msg:^40}')
    linha()


def opcao(num, msg):
    print(f'\033[0;33m{num} - \033[0;34m{msg}\033[m')


def erro(msg):
    print(f'\033[0;31mERRO! {msg}\033[m')


def linha():
    print('-' * 40)
