sexo = str(input('Informe o sexo da pessoa [F/M]: ')).strip().upper()[0]
while sexo not in 'MF':
    sexo = str(input('Dado inválido, informe o sexo [F/M]: ')).strip().upper()[0]
print('Sexo {} registrado com sucesso.'.format('Masculino' if sexo=='M' else 'Feminino'))
