salario = float(input('Informe o salário atual: R$'))
if salario > 1250:
    aumento = salario*.10
else:
    aumento = salario*.15
print('O novo salário será R${:.2f}.'.format(salario+aumento))
