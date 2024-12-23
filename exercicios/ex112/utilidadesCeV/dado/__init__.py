def leiaDinheiro(texto):
    while True:
        valor = input(texto).strip().replace(',', '.')
        valido = True
        for char in valor:
            if char not in '0123456789.':
                valido = False
                break
        if valido and len(valor) > 0 and valor.count('.') <= 1:
            valor = float(valor)
            break
        else:
            print(f'\033[0;31mERRO: "{valor}" é um preço inválido\033[m')
    return valor
