#!/usr/bin/python3
"""
    script that starts a Flask web application:
    Your web application must be listening on 0.0.0.0, port 5000
    Routes
    /: display “Hello HBNB!”
    /hbnb: display “HBNB”
    /c/<text>: display “C ” followed by the value of the
    text variable (replace underscore _ symbols with a space )
"""
from flask import Flask
from markupsafe import escape


app = Flask(__name__)


@app.route("/")
def say_hello():
    return "Hello HBNB!"


@app.route("/hbnb")
def say_hbnb():
    return "HBNB"


@app.route("/c/<text>")
def say_name(text):
    escaped_string = escape(text)
    result = escaped_string.replace("_", " ")
    return f"C {result}"


if __name__ == "__main__":
    app.run("0.0.0.0", port=5000, debug=True)
