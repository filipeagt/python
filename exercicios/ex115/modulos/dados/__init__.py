def criarArquivo(nome):
    try:
        arquivo = open(nome, 'wt+')
        arquivo.close()
    except:
        erro('Não foi possível criar o arquivo!')
    else:
        print(f'Arquivo {nome} criado com sucesso!')


def escrever(nomeArquivo):
    try:
        arquivo = open(nomeArquivo, 'at')
    except:
        erro('Não foi possível abrir o arquivo!')
    else:
        titulo('NOVO CADASTRO')
        nome = input('Nome: ')
        idade = leiaInt('Idade: ')
        try:
            arquivo.write(f'{nome};{idade}\n')
        except:
            erro('Houve um problema na hora de escrever os dados.')
        else:
            print(f'Novo registro de {nome} adicionado.')
    finally:
        arquivo.close()


def ler(nomeArquivo):
    try:
        arquivo = open(nomeArquivo, 'r')
    except:
        erro('Não foi possível ler o arquivo')
    else:
        titulo('PESSOAS CADASTRADAS')
        for linha in arquivo:
            pessoa = linha[:-1].split(";")
            print(f'{pessoa[0]:<30}{pessoa[1]:>3} anos')
    finally:
        arquivo.close()
        

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
        

def arquivoExiste(nome):
    try:
        arquivo = open(nome, 'rt')
        arquivo.close()
    except FileNotFoundError:
        return False
    else:
        return True
