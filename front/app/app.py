import flask
import json
import requests
from flask import request
from random import seed
from random import random

app = flask.Flask(__name__)
app.config["DEBUG"] = True

#generating random number
seed(1)
def random_number():
    for _ in range(1):
        value = random()
        return value

random_number = random_number()

def reverting_message(message):
    reversedstring = ''.join(reversed(message))
    return reversedstring

@app.route('/', methods=['GET'])
def home():
    return "<h1>Test</h1><p>This site is Diginex Test</p>"

@app.route('/api', methods=['POST'])
def api_post():
    content = request.get_json()
    print ("Received json: ",content)

    reverted = reverting_message(content['message'])

    res = requests.post('http://localhost:6000/reverse', json={"message":content['message']})
    print res
    if res.ok:
        print res.json()
#    reverted = remotely_reverted(content['message'])

    response = app.response_class(
        response=json.dumps({
            "message":reverted,
            "random":random_number,
            "original":content['message'],
            }),
        status=200,
        mimetype='application/json'
    )
    return response

app.run(host='0.0.0.0', port=5000)

