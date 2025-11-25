import subprocess
import re
import requests
import os

# ------- CONFIGURAÇÃO DO TELEGRAM --------
TELEGRAM_TOKEN = "COLOQUE_SEU_TOKEN_AQUI"
TELEGRAM_CHAT_ID = "COLOQUE_SEU_CHAT_ID_AQUI"

def send_telegram_message(message):
    """
        envia notificação para o Telegram
    """
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    data = {"chat_id": TELEGRAM_CHAT_ID, "text": message}

    try:
        requests.post(url, data=data)
    except Exception as e:
        print(f"Erro ao enviar mensagem ao Telegram: {e}")

# -----------------------------------------------


def sanitize_filename(url):
    """
        sanitiza o nome do arquivo para evitar caracteres especiais
    """
    return re.sub(r'[^a-zA-Z0-9_\-]', '_', url)


def run_nuclei(urls):
    """
        roda o nuclei para cada url de uma lista
    """
    for url in urls:
        filename = f"nuclei_result_{sanitize_filename(url)}.txt"
        print(f"Analisando {url} com Nuclei...")

        try:
            result = subprocess.run(
                ["nuclei", "-u", url, "-o", filename, "-silent"],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )

            if result.returncode == 0:
                print(f"Análise de {url} concluída. Resultado salvo em {filename}")

                # Verifica se o arquivo contém vulnerabilidades
                if os.path.isfile(filename) and os.path.getsize(filename) > 0:
                    send_telegram_message(
                        f"🔴 Vulnerabilidade encontrada em: {url}\nArquivo: {filename}"
                    )
                else:
                    print("Nenhuma vulnerabilidade encontrada.")
            else:
                print(f"Erro ao analisar {url}: {result.stderr}")

        except Exception as e:
            print(f"Erro ao executar Nuclei para {url}: {e}")

    print("Análise concluída para todos os sites.")


urls_to_analyze = [
    "https://google.com",
    "https://facebook.com",
    "https://youtube.com"
]

run_nuclei(urls_to_analyze)