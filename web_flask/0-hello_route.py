#!/usr/bin/python3
"""A simple python flask script that listens on 0.0.0.0, port 5000"""

from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_HBNB():
    """Return 'Hello HBNB!' on root route"""
    return "Hello HBNB!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
