from flask import Blueprint, current_app, jsonify, request

from .models import Identifier
from .telegram_bot import Telebot


checker = Blueprint('checker', __name__)


@checker.route('/', methods=['GET'])
def id_checker():
    """
        Handle the GET request to check the existence of a Telegram ID in the database.

        Returns:
            tuple: A tuple containing the HTTP response with status code and body.

        Notes:
            This function retrieves the 'id' query parameter from the request.
            If the parameter is missing, it logs a message and returns a 400 error response.
            Otherwise, it queries the database to check if the Telegram ID exists.
            If the ID doesn't exist, it logs a message, sends a notification using the Telebot,
            and returns a 404 error response.
            If the ID exists, it logs a message and returns a 200 success response.
        """

    telegram_id = request.args.get('id')
    if not telegram_id:
        current_app.logger.info('ID did not provided!')
        return jsonify({'all': 'ID must be provided!'}), 400

    row = Identifier.query.filter_by(telegram_id=telegram_id).first()

    if not row:
        current_app.logger.info(f"{telegram_id} ID doesn't exist in database!")

        bot = Telebot(bot_token=current_app.config['TELEGRAM_BOT_TOKEN'])
        bot.send_notification(telegram_id, "Your ID doesn't exist in database!")

        return jsonify({'all': "Requested ID doesn't exist in database!"}), 404

    current_app.logger.info(f"{telegram_id} ID exists in database!")
    return jsonify({'all': 'Requested ID exists in database!'}), 200
