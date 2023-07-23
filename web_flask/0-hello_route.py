#!/usr/bin/python3
"""
This scripts starts a flask app
"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_world():
    return 'Hello HBNB!'


if __name__ == '__main__':
    app.run("0.0.0.0", port=5000, debug=True)
