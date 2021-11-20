import os

from ml_dev_utils.TelegramNotifier import TelegramNotifier


def test_message_is_send_to_chat_bot():
    """Send message to Telegram

    This test sends a message to Telegram and checks for a successful response.
    You need to set the Telegram BOT_TOKEN and CHAT_ID as environment variable
    for test execution.
    """
    # given
    # TODO set environment variable: BOT_TOKEN and CHAT_ID
    os.environ['TELEGRAM_BOT_TOKEN'] = os.environ['BOT_TOKEN']
    os.environ['TELEGRAM_CHAT_ID'] = os.environ['CHAT_ID']
    telegram_notifier = TelegramNotifier()

    # when
    response = telegram_notifier.send("Training finished with 99,9% accuracy!")

    # then
    print(response)
    assert response['ok'] == True


def test_missing_env_variables():
    # given
    try:
        del os.environ['TELEGRAM_BOT_TOKEN']
        del os.environ['TELEGRAM_CHAT_ID']
    except KeyError:
        pass

    telegram_notifier = TelegramNotifier()

    # when
    response = telegram_notifier.send("Training finished with 99,9% accuracy!")

    # then
    assert response['ok'] == False
