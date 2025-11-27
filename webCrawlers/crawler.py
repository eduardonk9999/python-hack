import requests

URL_AUTOMOVEIS = "https://django-anuncios.solyd.com.br/automoveis/"

def buscar(url):
    try:
        respostas = requests.get(url)
        if respostas.status_code == 200:
            print(respostas.text)
        else:
            print("Erro ao fazer requisição")

    except Exception as error:
        print("Erro ao fazer a requisição")
        print(error)


buscar(URL_AUTOMOVEIS)