from flask import Flask, request, g, url_for
import sqlite3
import json


app = Flask(__name__)

DATABASE = "report"

class Report:
    def __init__(self, type, date, time, description, latitude, longitude):
        self.type = type
        self.date = date
        self.time = time
        self.description = description
        self.latitude = latitude
        self.longitude = longitude


def get_db(param=0):
    db = getattr(g, '_database', None)
    if db is None or param == 1:
        db = g._database = sqlite3.connect(DATABASE)
        conn = sqlite3.connect(DATABASE)
        cur = conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS REPORT(Id INTEGER PRIMARY KEY AUTOINCREMENT, type VARCHAR, "
                    "date VARCHAR, time VARCHAR, description VARCHAR, latitude VARCHAR, longitude VARCHAR)")
        conn.commit()
        conn.close()
    return db


@app.route('/', methods=['GET, ''PUT,' 'POST'])
def hello_world():
    return 'Hello World!'


@app.route('/report', methods=['PUT', 'POST', 'GET'])
def report():
    if request.method == 'POST' or request.method == 'PUT':
        print("putting/posting")
        print(request.json)
        type = request.json["type"]
        date = request.json["date"]
        time = request.json["time"]
        description = request.json["description"]
        latitude = request.json["latitude"]
        longitude = request.json["longitude"]
        report = Report(type, date, time, description, latitude, longitude)
        print(report)

        get_db(1).execute("INSERT INTO REPORT VALUES (NULL, ?, ?, ?, ?, ?, ?)",
                          (type, date, time, description, latitude, longitude))
        get_db().commit()
        get_db().close
        return("success")

    elif request.method == 'GET':
        print("here")
        reports = ""
        for col in get_db().execute("SELECT * FROM REPORT"):
            current_report = Report(col[1], col[2], col[3], col[4], col[5], col[6])
            json_obj = json.dumps(current_report.__dict__)
            reports += json_obj + '\n'
        print(reports)
        return reports
    else:
        return "nothing"


if __name__ == '__main__':
    app.run()
