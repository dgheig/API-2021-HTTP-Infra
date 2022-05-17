from flask import Flask, request
import datetime
import logging
logging.basicConfig(level=logging.INFO)

app = Flask(__name__)

@app.route("/")  # Route à appeler
def timestamp():
    return {
        "timestamp": datetime.datetime.now().strftime("%Y-%m-%d %M:%s")
    }

@app.route("/<param1>")  # Route à appeler
def hello_world(param1, **kw):
    return "<h1>Hi {}</h1>".format(param1)

app.run("0.0.0.0")
