import requests


class Telebot:
    """
    A simple wrapper class for interacting with the Telegram Bot API.

    Attributes:
        _bot_token (str): The token used to authenticate with the Telegram Bot API.
        _url (str): The base URL for making requests to the Telegram Bot API.

    Methods:
        __init__(bot_token): Initializes a Telebot instance with the provided bot token.
        send_notification(chat_id, message): Sends a notification message to a specified chat.
        get_updates(): Retrieves the latest updates from the Telegram Bot API.
    """

    def __init__(self, bot_token: str):
        """
        Initialize a Telebot instance with the provided bot token.

        Args:
            bot_token (str): The token used to authenticate with the Telegram Bot API.
        """

        self._bot_token = bot_token
        self._url = f'https://api.telegram.org/bot{self._bot_token}'

    def send_notification(self, chat_id: str, message: str) -> requests.Response:
        """
        Send a notification message to a specified chat.

        Args:
            chat_id (int): The unique identifier for the target chat.
            message (str): The text message to be sent.

        Returns:
            requests.Response: The response object returned from the API request.
        """

        url = f'{self._url}/sendMessage?chat_id={chat_id}&text={message}'
        return requests.get(url)

    def get_updates(self) -> requests.Response:
        """
        Retrieve the latest updates from the Telegram Bot API.

        Returns:
            requests.Response: The response object containing the latest updates.
        """

        url = f'{self._url}/getUpdates'
        return requests.get(url)
