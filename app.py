from flask import Flask, request
import sqlite3

import requests

app = Flask(__name__)


class Report:
    def __init__(self, type, date, time, latitude, longitude):
        self.type = type
        self.date = date
        self.time = time
        self.latitude = latitude
        self.longitude = longitude


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/report', methods=['PUT'])
def report():
    print(request.json)
    type = request.json["type"]
    date = request.json["date"]
    time = request.json["time"]
    latitude = request.json["latitude"]
    longitude = request.json["longitude"]
    report = Report(type, date, time, latitude, longitude)
    print(report)
    return("success")


if __name__ == '__main__':
    app.run()
