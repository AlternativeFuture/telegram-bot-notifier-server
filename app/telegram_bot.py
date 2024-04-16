import requests


class Telebot:
    def __init__(self, bot_token):
        self.bot_token = bot_token

    def send_notification(self, chat_id, message):
        url = 'https://api.telegram.org/bot{}/sendMessage?chat_id={}&text={}'.format(self.bot_token, chat_id, message)
        requests.get(url)

    def get_updates(self):
        url = 'https://api.telegram.org/bot{}/getUpdates'.format(self.bot_token)

        requests.get(url)
