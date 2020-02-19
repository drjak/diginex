import flask
import json
from flask import request
from random import seed
from random import random

app = flask.Flask(__name__)
app.config["DEBUG"] = True

def reverting_message(message):
    reversedstring = ''.join(reversed(message))
    return reversedstring

@app.route('/reverse', methods=['POST'])
def api_post():
    content = request.get_json()
    print ("Received json: ",content)
    reverted = reverting_message(content['message'])

    response = app.response_class(
        response=json.dumps({
            "message":reverted,
            }),
        status=200,
        mimetype='application/json'
    )
    return response

app.run(host='0.0.0.0', port=6000)

