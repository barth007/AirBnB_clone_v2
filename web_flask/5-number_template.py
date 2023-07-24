#!/usr/bin/python3
"""
   Write a script that starts a Flask web application:
   Your web application must be listening on 0.0.0.0, port 5000
   Routes:
   /: display “Hello HBNB!”
   /hbnb: display “HBNB”
   /c/<text>: display “C ”, followed by the value
   of the text variable (replace underscore _ symbols with a space )
   /python/(<text>): display “Python ”, followed by the value
   of the text variable (replace underscore _ symbols with a space )
   The default value of text is “is cool”
    /number/<n>: display “n is a number” only if n is an integer
    /number_template/<n>: display a HTML page only if n is an integer:
    H1 tag: “Number: n” inside the tag BODY
"""
from flask import Flask
from flask import escape
from flask import render_template


app = Flask(__name__)


@app.route('/', strict_slashes=True)
def hello_hbnb():
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def say_hbnh():
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_replace(text):
    escaped_text = escape(text)
    result = escaped_text.replace("_", " ")
    return f"C {result}"


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_replace(text="is cool"):
    escaped_text = escape(text)
    result = escaped_text.replace("_", " ")
    return f"python {result}"


@app.route('/number/<int:n>', strict_slashes=False)
def number_url(n):
    result = escape(n)
    return f"{result} is a number"


@app.route('/number_template/<int:n>', strict_slashes=False)
def render_html(n):
    return render_template('5-number.html', n=n)


if __name__ == "__main__":
    app.run("0.0.0.0", port=5000, debug=True)
