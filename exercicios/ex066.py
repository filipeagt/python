soma = qtd = num = 0

while True:
    num = int(input('Digite um número [999 para parar]: '))
    if num == 999:
        break
    qtd += 1
    soma += num
print(f'Foram digitados {qtd} números e a soma entre eles é {soma}.')
