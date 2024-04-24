from flask import Flask

from app.views import checker
from app.db import db


app = Flask(__name__)

app.config.from_pyfile('config.py', silent=True)

app.logger.setLevel(app.config['LOG_LEVEL'])

api_checker = '/'

db.init_app(app)

app.register_blueprint(checker, url_prefix=api_checker)

app.logger.info('Application Started Successfully')


if __name__ == '__main__':
    app.run(host=app.config['FLASK_HOST'],
            port=app.config['FLASK_PORT'],
            debug=app.config['DEBUG'])
