#!/usr/bin/env python3

from flask import Flask, url_for
from markupsafe import escape

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return 'HBNB'


@app.route("/c/<text>", strict_slashes=False)
def hello_c(text):
    sptext = text.replace('_', ' ')
    return f"C {escape(sptext)}!"

@app.route('/python/', strict_slashes=False)
def pyool():
    return 'Python is cool!'

@app.route("/python/<text>", strict_slashes=False)
def pyCool(text):
    sptext = text.replace('_', ' ')
    return f"Python {escape(sptext)}!"



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port='5000')
