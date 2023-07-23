#!/usr/bin/python3
"""
Write a script that starts a Flask web application:
Routes:
/: display “Hello HBNB!”
/hbnb: display “HBNB”
"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def say_hello():
    return "Hello HBNB!"


@app.route("/hbnb")
def say_hbnb():
    return "HBNB"


if __name__ == "__main__":
    app.run("0.0.0.0", port=5000, debug=True)
