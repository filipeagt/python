from time import sleep
from emoji import emojize
for x in range(10, -1, -1):
    print(x)
    sleep(1)
print('Feliz ano novo! {}'.format(emojize(':fireworks:')))
