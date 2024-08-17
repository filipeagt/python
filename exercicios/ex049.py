num =  int(input('Qual tabuada você quer ver? '))
for x in range(1,11):
    print('{} x {:2} = {:2}'.format(num, x, num*x))
