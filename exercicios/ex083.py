pilha = []
expressao = input('Digite um expressão com parênteses: ')
for caractere in expressao:
    if caractere == '(':
        pilha.append(caractere)
    elif caractere == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(caractere)
            break
if len(pilha) == 0:
    print(f'A expressão {expressao} é válida!')
else:
    print(f'A expressão {expressao} está errada!')
