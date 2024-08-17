num = int(input('Digite um número: '))
primo = True
for x in range(2, num):
    if num % x == 0:
        primo = False
        break
if primo:
    print('O número {} é PRIMO.'.format(num))
else:
    print('O número {} NÃO é primo.'.format(num))
