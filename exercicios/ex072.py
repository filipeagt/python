contagem = (
    "Zero", "Um", "Dois", "Três", "Quatro", "Cinco", 
    "Seis", "Sete", "Oito", "Nove", "Dez", 
    "Onze", "Doze", "Treze", "Quatorze", "Quinze", 
    "Dezesseis", "Dezessete", "Dezoito", "Dezenove", "Vinte"
)
while True:
    num =  int(input('Digite um número entre 0 e 20: '))
    continuar = 'S'    
    while num < 0 or num > 20:
        num = int(input('Tente novamente. Digite um número entre 0 e 20: '))
    print(f'Você digitou o número {contagem[num]}.')
    while True:
        continuar = input('Deseja continuar [S/N]: ').strip().upper()[0]
        if continuar in 'SN':
            break
    if continuar == 'N':
        break