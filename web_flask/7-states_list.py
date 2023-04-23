#!/usr/bin/python3
"""
Starting my first Flask web application
"""
from models import storage
from models.state import State
from os import environ
from flask import Flask, render_template
app = Flask(__name__)


@app.teardown_appcontext
def close_db(error):
    """
    Remove the SQLAlchemy session
    """
    storage.close()


@app.route('/states_list', strict_slashes=False)
def list_states():
    """
    A route that displays cities in our database in html
    """
    states = storage.all(State).values()
    states = sorted(states, key=lambda k: k.name)
    return render_template('7-states_list.html', states=states)


if __name__ == "__main__":
    """ Main Function """
    app.run(host='0.0.0.0', port=5000, debug=True)
