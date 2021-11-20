import os
import requests


class TelegramNotifier:

    def __init__(self):
        self.bot_token = os.getenv('TELEGRAM_BOT_TOKEN')
        self.chat_id = os.getenv('TELEGRAM_CHAT_ID')

    def send(self, message):
        if self.bot_token == None or self.chat_id == None:
            return {
                'ok': False,
                'error_code': 404,
                'description': '"No telegram settings set. Skipping notification"'
            }

        send_message_url = (f'https://api.telegram.org'
                            f'/bot{self.bot_token}/sendMessage?'
                            f'chat_id={self.chat_id}'
                            f'&parse_mode=Markdown'
                            f'&text={message}')
        response = requests.get(send_message_url)

        return response.json()
