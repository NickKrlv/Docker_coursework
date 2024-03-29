import requests
from config.settings import TELEGRAM_BOT_TOKEN


class MyBot:
    URL = "https://api.telegram.org/bot"
    TOKEN = TELEGRAM_BOT_TOKEN
    chat_id = ''  # введи свой chat_id

    def send_message(self, text):
        requests.get(f"{self.URL}{self.TOKEN}/sendMessage?chat_id={self.chat_id}&text={text}")
