#!/usr/bin/python3
from flask import Flask
from flask import url_for

app = Flask(__name__)

@app.route('/')
def index():
    return "index page"

@app.route('/login')
def login():
    return "login"


@app.route('/user/<username>')
def profile():
    return f"username: {username}"


with app.test_request_context():
    print(url_for('index'))
    print(url_for('login'))
    print(url_for('login', next='/'))
    print(url_for('profile', username='B B'))

if __name__ == "__main__":
    app.run("0.0.0.0", port=5000, debug=True)
