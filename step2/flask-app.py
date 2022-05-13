from flask import Flask, request
import logging
logging.basicConfig(level=logging.INFO)

app = Flask(__name__)

@app.route("/<param1>")  # Route à appeler
def hello_world(param1, **kw):
    # Les paramètres sont loggés
    logging.info(param1)
    logging.info(kw)
    logging.info(request.args)
    return "<h1>{}</h1><p>{}</p>".format(param1, request.args)

app.run()
