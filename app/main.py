import config
from db import db

from flask import Flask, request

app = Flask(__name__)
app.config.from_pyfile('config.py')
db.init_app(app)


@app.route('/', methods=['GET'])
def check_id():
    pk = request.args.get('id')
    return f"Hello, World! PK: {pk}"


if __name__ == '__main__':
    app.run()
