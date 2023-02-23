#!/usr/bin/env python3
"""
2. Get locale from request
"""
from flask import Flask, render_template, g, request
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


@babel.localeselector
def get_locale():
    """
     supported languages
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


app.config.from_object(Config)


@app.route("/", methods=['GET'])
def helloWorld():
    """
    Hello World
    """
    return render_template('2-index.html')
