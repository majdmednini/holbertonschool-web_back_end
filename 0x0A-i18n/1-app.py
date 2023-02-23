#!/usr/bin/env python3
"""
1. Basic Babel setup
"""
from flask import Flask, render_template
from flask_babel import Babel
app = Flask(__name__)
babel = Babel(app)


class Config(object):
    """
    config
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


@app.route("/", methods=['GET'])
def helloWorld():
    """
    Hello World
    """
    return render_template('1-index.html')
