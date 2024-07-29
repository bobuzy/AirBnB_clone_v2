#!/usr/bin/python3
"""Simple python flask script to list all states in the Database"""

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def list_states():
    """Render all states in a template"""
    state_list = storage.all(State)
    sorted_states = sorted(state_list.values(), key=lambda state: state.name)
    return render_template("7-states_list.html", states=sorted_states)

@app.teardown_appcontext
def stop_session(None):
    """Clean-up session"""
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
