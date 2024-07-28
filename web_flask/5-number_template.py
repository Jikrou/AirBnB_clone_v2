#!/usr/bin/env python3
""" a script that starts a Flask web application"""
from flask import Flask, request, render_template
from markupsafe import escape

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """ return hello hbnb"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ return hbnb """
    return 'HBNB'


@app.route("/c/<text>", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def hello_text(text):
    """ return the text entered by the user """
    sptext = text.replace('_', ' ')
    if 'c' in request.url:
        return f"C {escape(sptext)}"
    elif 'python' in request.url:
        return f"Python {escape(sptext)}"


@app.route('/python/', strict_slashes=False)
def pyool():
    """ return python is cool """
    return 'Python is cool'


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """return a number"""
    return f"{escape(n)} is a number"


@app.route("/number_template/<int:n>", strict_slashes=False)
def html_template(n):
    """ return the number in a html page """
    return render_template('5-number.html', n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
