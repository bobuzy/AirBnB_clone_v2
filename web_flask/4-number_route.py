#!/usr/bin/python3
"""A simple python flask script that listens on 0.0.0.0, port 5000"""

from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_HBNB():
    """Return 'Hello HBNB!' on root route"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def HBNB():
    """Return 'HBNB' on '/hbnb' route"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def hello_c(text):
    """Return 'C' with whatever text passed in the sub-route"""
    return "C " + text.replace("_", " ")


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def hello_python(text="is cool"):
    """Return 'python' with the value of text"""
    return "Python " + text.replace("_", " ")


@app.route("/number/<int:n>")
def is_number(n):
    """Return 'n is a number', if n is an integer"""
    return "{} is a number".format(n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
