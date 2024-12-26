#from modulos.interface import *
from modulos.arquivo import *
from time import sleep

arquivo = 'dados.txt'
if not arquivoExiste(arquivo):
    criarArquivo(arquivo)

while True:
    escolha = menu(['Ver pessoas cadastradas', 'Cadastrar nova Pessoa', 'Sair do sistema'])
    if escolha == 1:
        ler(arquivo)
    elif escolha == 2:
        escrever(arquivo)
    elif escolha == 3:
        titulo('Saindo do sistema... Até logo!')
        break
    else:
        erro('Digite uma opção válida')
    sleep(1)
