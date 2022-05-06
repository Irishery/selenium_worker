from crypt import methods
from flask import Blueprint, request
from worker_threads import thread

worker_api = Blueprint('user_api', __name__)

@worker_api.route('/worker/run/', methods=['GET'])
def run_worker():
    data = request.args
    new_worker = thread('111', '111')
    new_worker.start()
    print('asasdasd')

    return {'worker': '111',
            'status': 'started'}
