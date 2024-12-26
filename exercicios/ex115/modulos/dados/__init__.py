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
        

def menu(opcoes):
    titulo('MENU PRINCIPAL')
    for indice, valor in enumerate(opcoes):
        opcao(indice + 1, valor)
    linha()
    escolha = leiaInt('\033[32mSua Opção: \033[m')
    return escolha

    
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


def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            erro('Por favor, digite um número inteiro válido.')
            continue
        except (KeyboardInterrupt):
            erro('O usuário preferiu não digitar esse número.')
            return 0
        else:
            return n
