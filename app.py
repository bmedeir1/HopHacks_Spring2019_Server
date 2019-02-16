from flask import Flask, request, g, url_for
import sqlite3

import requests

app = Flask(__name__)

DATABASE = "report"

class Report:
    def __init__(self, type, date, time, latitude, longitude):
        self.type = type
        self.date = date
        self.time = time
        self.latitude = latitude
        self.longitude = longitude


def get_db(param=0):
    db = getattr(g, '_database', None)
    if db is None or param == 1:
        db = g._database = sqlite3.connect(DATABASE)
        conn = sqlite3.connect(DATABASE)
        cur = conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS REPORT(Id INTEGER PRIMARY KEY AUTOINCREMENT, type VARCHAR, "
                    "date VARCHAR, time VARCHAR, latitude VARCHAR, longitude VARCHAR)")
        conn.commit()
        conn.close()
    return db


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/report', methods=['PUT', 'POST'])
def report():
    print(request.json)
    type = request.json["type"]
    date = request.json["date"]
    time = request.json["time"]
    latitude = request.json["latitude"]
    longitude = request.json["longitude"]
    report = Report(type, date, time, latitude, longitude)
    print(report)

    get_db(1).execute("INSERT INTO REPORT VALUES (NULL, ?, ?, ?, ?, ?)",
                      (type, date, time, latitude, longitude))
    get_db().commit()
    get_db().close
    return("success")


if __name__ == '__main__':
    app.run()
