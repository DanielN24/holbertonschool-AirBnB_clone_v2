#!/usr/bin/python3
""" script that starts a Flask web application """
from flask import Flask
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """ function that display Hello HBNB! """
    return "Hello HBNB!"

@app.route("/hbnb", strict_slashes=False)
def HBNB():
    """ function that display Hello HBNB! """
    return "HBNB"

@app.route("/c/<text>", strict_slashes=False)
def c(text):
    """ function that display Hello HBNB! """
    replaces = text.replace("_", " ")
    return ("c {}".format(replaces))

@app.route("/python/", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def Python_(text='is cool'):
    """ function that display Hello HBNB! """
    replaces = text.replace("_", " ")
    return ("Python {}".format(replaces))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
