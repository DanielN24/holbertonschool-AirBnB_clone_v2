#!/usr/bin/python3
""" script that starts a Flask web application """
from flask import Flask, render_template
from models import storage
from models.state import State
app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def lists():
    """ list of states """
    states = storage.all(State)
    return render_template("7-states_list.html", states=states)


@app.teardown_appcontext
def tear(exc):
    """ teardown_appcontext """
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
