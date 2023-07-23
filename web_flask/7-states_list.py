#!/usr/bin/python3
"""starting a Flask web application.

app listens on 0.0.0.0, port 5000.
Routes:
    /states_list: shows the HTML page listing all State obj in DBStorage.
"""
from models import storage
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def states_list():
    """to display HTML page listing all State obj in DBStorage.
    """
    states = storage.all("State")
    return render_template("7-states_list.html", states=states)


@app.teardown_appcontext
def teardown(exc):
    """closes current SQLAlchemy session."""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0")
