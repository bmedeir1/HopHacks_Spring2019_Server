from flask import Flask, request

import requests

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/report', methods=['PUT'])
def report():
    print(request.json)
    return("success")


if __name__ == '__main__':
    app.run()
