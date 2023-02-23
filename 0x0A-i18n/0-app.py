#!/usr/bin/env python3
"""
0. Basic Flask app
"""
from flask import Flask, render_template
from flask_babel import Babel
app = Flask(__name__)
babel = Babel(app)


class Config(object):
    """
    config
    """
    LANGUAGES = ['en', 'es']


@app.route("/", methods=['GET'])
def helloWorld():
    """
    Hello World
    """
    return render_template('0-index.html')
