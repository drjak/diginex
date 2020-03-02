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

def reverting_message_remote(message):
    try:
        res = requests.post('http://jak.slave.arkdevs.ee:6000/reverse', json={"message":message})
        if res.ok:
            print ("Response from backend ", res.json())
            return res.json()
    except:
        print "Can't call backend"
    finally:
        res.close

@app.route('/', methods=['GET'])
def home():
    return "<h1>Test</h1><p>This site is Diginex Test</p>"

@app.route('/api', methods=['POST'])
def api_post():
    content = request.get_json()
    reverted = reverting_message_remote(content['message'])

    response = app.response_class(
        response=json.dumps({
            "message":reverted['message'],
            "random":random_number
            }),
        status=200,
        mimetype='application/json'
    )
    return response

app.run(host='0.0.0.0', port=5000)
