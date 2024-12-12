times_brasileirao = (
    "Botafogo", "Palmeiras", "Atlético-MG", "Flamengo", "Grêmio",
    "Internacional", "São Paulo", "Fluminense", "Corinthians", "Cruzeiro",
    "Athletico-PR", "Santos", "Fortaleza", "Bahia", "Vasco",
    "Cuiabá", "Goiás", "Red Bull Bragantino", "América-MG", "Coritiba"
)
def linha():
    print('-='*20)
linha()
print(f'Lista de times do Brasileirão: {times_brasileirao}')
linha()
print(f'Os 5 primeiros colocados são {times_brasileirao[:5]}')
linha()
print(f'Os últimos 4 colocados são {times_brasileirao[-4:]}')
linha()
print(f'Times em ordem alfabética: {sorted(times_brasileirao)}')
linha()
print(f'O São Paulo está na {times_brasileirao.index("São Paulo")+1}ª posição.')
