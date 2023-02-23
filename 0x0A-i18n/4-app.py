#!/usr/bin/env python3
"""
4. Force locale with URL parameter
"""
from flask import Flask, render_template, g, request
from flask_babel import Babel
app = Flask(__name__)
babel = Babel(app)


class Config(object):
    """
    language config
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


@babel.localeselector
def get_locale():
    """
    supported languages
    """
    locale = request.args.get("locale")
    if locale in Config.LANGUAGES:
        return locale

    return request.accept_languages.best_match(app.config['LANGUAGES'])


app.config.from_object(Config)


@app.route("/", methods=['GET'])
def helloWorld():
    """
    Hello World
    """
    return render_template('3-index.html')
