from flask import Flask


def create_app(config_filename='config.py'):

    app = Flask(__name__)

    app.config.from_pyfile(config_filename, silent=True)
    # app.logger.setLevel(app.config['LOG_LEVEL'])

    api_checker = '/'

    from .db import db

    db.init_app(app)

    from .views import checker

    app.register_blueprint(checker, url_prefix=api_checker)

    return app
