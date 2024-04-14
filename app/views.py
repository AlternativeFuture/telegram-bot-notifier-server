from .models import Table

from flask import Blueprint, jsonify, request

checker = Blueprint('checker', __name__)


@checker.route('/', methods=['GET'])
def check_id():
    pk = request.args.get('id')
    if not pk:
        # TODO: fix with correct status
        errors = {'all': 'ID must be provided!'}
        return jsonify(errors), 204

    # TODO: implement exception handling
    # try:
    #     row = Table.get_by_id(pk=pk)
    # except:
    row = Table.get_by_id(pk=pk)

    if not row:
        'notify telegram bot admin'
        errors = {'all': "Requested ID doesn't exist in database!"}
        return jsonify(errors), 204

    errors = {'all': 'Requested ID exists in database!'}
    return jsonify(errors), 200


# if __name__ == '__main__':
#     app.run()
