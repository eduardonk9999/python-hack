import requests
from bs4 import BeautifulSoup


URL_AUTOMOVEIS = "https://django-anuncios.solyd.com.br/automoveis/"

def buscar(url):
    try:
        respostas = requests.get(url)
        if respostas.status_code == 200:
            return respostas.text
        else:
            print("Erro ao fazer requisição")

    except Exception as error:
        print("Erro ao fazer a requisição")
        print(error)

def parsing(resposta_html):
    try:
        soup = BeautifulSoup(resposta_html, 'html.parser')
        return soup
    except Exception as error:
        print("Erro ao fazer o parsing HTML")
        print(error)
    


resposta = buscar(URL_AUTOMOVEIS)
if resposta:
    soup = parsing(resposta)