#!/usr/bin/python3
""" a script that starts a Flask web application """
from flask import Flask
from markupsafe import escape

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """ method display hello HBNB"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ method display hbnb"""
    return 'HBNB'


@app.route("/c/<text>", strict_slashes=False)
def hello_text(text):
    """ method return the text entered by the user """
    sptext = text.replace('_', ' ')
    return f"C {escape(sptext)}"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
