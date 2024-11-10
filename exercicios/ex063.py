n = int(input('Quantos números de Fibonacci vc quer ver? '))
a=0
b=1
while n > 0:    
    print('{}'.format(a),end=' => ')
    n -= 1
    if n == 0:
        break
    print('{}'.format(b), end=' => ')
    n -= 1
    a += b
    b += a
print('Fim')
