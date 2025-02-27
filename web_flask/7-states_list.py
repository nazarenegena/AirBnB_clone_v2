#!/usr/bin/python3
# lists the states
from flask import Flask, render_template
from models import storage
app = Flask(__name__)


@app.route('/states_list')
def stateList():
    # listing all the states in html
    return render_template('7-states_list.html', storage=storage.all('State'))


@app.teardown_appcontext
def closer(exception):
    storage.close()


if __name__ == "__main__":
    app.url_map.strict_slashes = False
    app.run(host="0.0.0.0", port=5000)
