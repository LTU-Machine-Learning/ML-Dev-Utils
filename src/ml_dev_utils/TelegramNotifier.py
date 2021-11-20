"""
TelegramNotifier
================
"""

import os
import requests


class TelegramNotifier:
    """Sends message to Telegram.

    This class sends messages to Telegram. To access Telegram, you need to set 
    the environment variables `TELEGRAM_BOT_TOKEN` and `TELEGRAM_CHAT_ID.` The 
    documentation on setting up a Telegram bot can be found here: 
    https://core.telegram.org/bots.

    Example to set ENV on Mac/Linux::

        export TELEGRAM_BOT_TOKEN=your-token-here
        export TELEGRAM_CHAT_ID=your-chat-id-here
    """

    def __init__(self):
        self.bot_token = os.getenv('TELEGRAM_BOT_TOKEN')
        self.chat_id = os.getenv('TELEGRAM_CHAT_ID')

    def send(self, message: str) -> dict:
        """Send a message

        Args:
            message (str): The text of the message

        Returns:
            dict: JSON response from Telegram

        Example::

            from ml_dev_utils.TelegramNotifier import TelegramNotifier

            telegram_notifier = TelegramNotifier()
            response = telegram_notifier.send("Training finished with 99,9% accuracy!")
            print(response)
        """
        if self.bot_token == None or self.chat_id == None:
            return {
                'ok': False,
                'result': {
                    'text': 'No telegram settings set. Skipping notification'
                }
            }

        send_message_url = (f'https://api.telegram.org'
                            f'/bot{self.bot_token}/sendMessage?'
                            f'chat_id={self.chat_id}'
                            f'&parse_mode=Markdown'
                            f'&text={message}')
        response = requests.get(send_message_url)

        return response.json()


# remove the main
if __name__ == "__main__":
    telegram_notifier = TelegramNotifier()
    response = telegram_notifier.send("Training finished with 99,9% accuracy!")
    print(type(response))
    print(response)
