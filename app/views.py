from .models import Identifier

from flask import Blueprint, jsonify, request

checker = Blueprint('checker', __name__)


@checker.route('/', methods=['GET'])
def check_id():
    pk = request.args.get('id')
    if not pk:
        # TODO: fix with correct status
        return jsonify({'all': 'ID must be provided!'}), 400

    # TODO: implement exception handling
    # try:
    #     row = Identifier.get_by_id(pk=pk)
    # except:
    row = Identifier.get_by_id(pk=pk)

    if not row:
        'notify telegram bot admin'
        errors = {'all': "Requested ID doesn't exist in database!"}
        return jsonify(errors), 400

    return jsonify({'all': 'Requested ID exists in database!'}), 200
