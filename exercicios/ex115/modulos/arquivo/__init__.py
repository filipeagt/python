from modulos.interface import *

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


def arquivoExiste(nome):
    try:
        arquivo = open(nome, 'rt')
        arquivo.close()
    except FileNotFoundError:
        return False
    else:
        return True
