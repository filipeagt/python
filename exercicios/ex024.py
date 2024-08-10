cidade = (input('Digite o nome de uma cidade: ')).upper().strip()
print('O nome da cidade {}começa com "SANTO"'.format('' if cidade[:5]=='SANTO' else 'NÃO '))

