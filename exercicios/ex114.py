import urllib.request
try:
    webUrl = urllib.request.urlopen('https://www.pudim.com.br/')
except:
    print('\033[0;31mO site Pudim não está acessível no momento!\033[m')
else:
    print('\033[0;33mConsegui acessar o site Pudim com sucesso!\033[m')
