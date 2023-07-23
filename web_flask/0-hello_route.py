#!/usr/bin/python3
""" code to start a flask web app.
app is on 0.0.0.0, port 5000.
Routes:
    /: to display 'Hello HBNB!'
"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """ to display 'Hello HBNB!'"""
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run(host="0.0.0.0")
