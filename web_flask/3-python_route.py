#!/usr/bin/python3
"""
 This script starts a Flask web application:
 The web application must be listening on 0.0.0.0, port 5000
 Routes:
      /: display “Hello HBNB!”
      /hbnb: display “HBNB”
      /c/<text>: display “C ”, followed by the value of the
      text variable (replace underscore _ symbols with a space )
      /python/(<text>): display “Python ”,
      followed by the value of the text variable
      (replace underscore _ symbols with a space )
      The default value of text is “is cool”
"""
from flask import Flask
from markupsafe import escape


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def say_hello():
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def say_hbnb():
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def say_name(text):
    escaped_text = escape(text)
    result = escaped_text.replace("_", " ")
    return f"C {result}"


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def replace_text(text="is cool"):
    escaped_text = escape(text)
    result = escaped_text.replace("_", " ")
    return f"Python {result}"


if __name__ == "__main__":
    app.run("0.0.0.0", port=5000, debug=False)
