import requests
from config.settings import TELEGRAM_BOT_TOKEN


class MyBot:
    URL = "https://api.telegram.org/bot"
    TOKEN = TELEGRAM_BOT_TOKEN
    chat_id = '359964166'

    def send_message(self, text):
        requests.get(f"{self.URL}{self.TOKEN}/sendMessage?chat_id={self.chat_id}&text={text}")
