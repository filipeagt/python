salario = float(input('Informe o salário atual: R$'))
if salario > 1250:
    aumento = salario*.10
else:
    aumento = salario*.15
print('Quem ganhava R${:.2f}, passa a ganhar R${:.2f}.'.format(salario, salario+aumento))
