from flask import Flask, request, Response
import datetime
import json
import logging
import names
import random
logging.basicConfig(level=logging.INFO)

app = Flask(__name__)

REF_DATETIME = datetime.datetime(1950, 1, 1)
DAYS = (datetime.datetime.now() - REF_DATETIME).days

def randomBirthday():
    return (
        REF_DATETIME +
        datetime.timedelta(random.randrange(DAYS))
    )

def getStudent():
    gender = random.choice(["male", "female"])
    return {
        "firstName": names.get_first_name(gender=gender),
        "lastName": names.get_last_name(),
        "gender": gender.capitalize(),
        "birthday": randomBirthday().ctime(),
    }

@app.route("/")  # Route à appeler
def students():
    nb = request.args.get("nb", 30)
    if not isinstance(nb, int) or nb < 1:
        nb = 30
    data = [
        getStudent()
        for _ in range(nb)
    ]
    return Response(json.dumps(data),  mimetype='application/json')

@app.route("/timestamp")  # Route à appeler
def timestamp():
    return {
        "timestamp": datetime.datetime.now().strftime("%Y-%m-%d %M:%s")
    }

@app.route("/hello/<param1>")  # Route à appeler
def hello_world(param1, **kw):
    return "<h1>Hi {}</h1>".format(param1)

app.run("0.0.0.0")
