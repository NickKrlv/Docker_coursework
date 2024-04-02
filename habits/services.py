from django.conf import settings
import requests


class MyBot:
    URL = 'https://api.telegram.org/bot/'
    TOKEN = settings.TELEGRAM_TOKEN
    CHAT_ID = settings.TELEGRAM_CHAT_ID

    def send_message(self, text):
        requests.post(
            url=self.URL + self.TOKEN + '/sendMessage',
            data=dict(
                chat_id=self.CHAT_ID,
                text=text

            )
        )
