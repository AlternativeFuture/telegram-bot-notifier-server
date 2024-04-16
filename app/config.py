import os
import logging

from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = os.environ.get('SECRET_KEY', 'dev')

TELEGRAM_BOT_TOKEN = os.environ.get('TELEGRAM_TOKEN', 'token')

FLASK_HOST = os.environ.get('FLASK_HOST', '127.0.0.1')
FLASK_PORT = os.environ.get('FLASK_PORT', 8000)
DEBUG = True

SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_ECHO = os.environ.get('FLASK_ENV') == 'development'

LOG_LEVEL = logging.INFO
if os.environ.get('FLASK_ENV') == 'development':
    LOG_LEVEL = logging.DEBUG
