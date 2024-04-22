import requests


class Telebot:
    def __init__(self, bot_token):
        self._bot_token = bot_token
        self._url = 'https://api.telegram.org/bot{}'.format(self._bot_token)

    def send_notification(self, chat_id, message):
        url = '{}/sendMessage?chat_id={}&text={}'.format(self._url, chat_id, message)
        return requests.get(url)

    def get_updates(self):
        url = '{}/getUpdates'.format(self._url)
        return requests.get(url)
