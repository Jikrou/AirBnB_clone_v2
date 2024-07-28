#!/usr/bin/python3
""" a script that starts a Flask web application """
from flask import Flask, request
from markupsafe import escape

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """ display hello hbnb"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ display hbnb """
    return 'HBNB'


@app.route("/c/<text>", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def hello_text(text):
    """ method display the texy entered by the user """
    sptext = text.replace('_', ' ')
    if 'c' in request.url:
        return f"C {escape(sptext)}"
    elif 'python' in request.url:
        return f"Python {escape(sptext)}"


@app.route('/python/', strict_slashes=False)
def pyool():
    return 'Python is cool'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
