#!/usr/bin/python3
"""starting a Flask web application.

app listens on 0.0.0.0, port 5000.
Routes:
    /cities_by_states: shows the HTML page listing all states & cities.
"""
from models import storage
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/cities_by_states", strict_slashes=False)
def cities_by_states():
    """to display an HTML page listing all states and related cities.

    States/cities are sorted by name.
    """
    states = storage.all("State")
    return render_template("8-cities_by_states.html", states=states)


@app.teardown_appcontext
def teardown(exc):
    """close current SQLAlchemy session."""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0")
