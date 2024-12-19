def fatorial(numero, show=False):
    """
    => Calcula o fatorial de um número.
    :param numero: O número a ser calculado
    :param show: (Opcional) Mostrar ou não a conta
    :return: O valor do fatorial de um número.
    """
    f = 1
    s = ''
    for x in range(numero, 0, -1):
        f *= x
        if show:
            s += f'{x} {"x" if x != 1 else "="} '
    if show:
        s += f'{f}'
        return '-' * 30 + '\n' + s
    else:
        return '-' * 30 + '\n' + str(f)


print(fatorial(5, True))
