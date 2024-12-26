from modulos.dados import *
from time import sleep

while True:
    escolha = menu(['Ver pessoas cadastradas', 'Cadastrar nova Pessoa', 'Sair do sistema'])
    if escolha == 1:
        ler()
    elif escolha == 2:
        escrever()
    elif escolha == 3:
        titulo('Saindo do sistema... Até logo!')
        break
    else:
        erro('Digite uma opção válida')
    sleep(2)
