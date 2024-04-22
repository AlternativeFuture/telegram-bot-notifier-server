from .models import Identifier
from .telegram_bot import Telebot

from flask import Blueprint, jsonify, request, current_app

checker = Blueprint('checker', __name__)


@checker.route('/', methods=['GET'])
def id_checker():
    telegram_id = request.args.get('id')
    if not telegram_id:
        return jsonify({'all': 'ID must be provided!'}), 400

    row = Identifier.query.filter_by(telegram_id=telegram_id).first()

    if not row:
        bot = Telebot(bot_token=current_app.config['TELEGRAM_BOT_TOKEN'])
        bot.send_notification(telegram_id, "Your ID doesn't exist in database!")
        return jsonify({'all': "Requested ID doesn't exist in database!"}), 404

    return jsonify({'all': 'Requested ID exists in database!'}), 200
