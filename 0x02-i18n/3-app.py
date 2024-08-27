#!/usr/bin/env python3
"""
Flask application module that configures language and timezone settings
using Flask-Babel, and defines a basic index route for rendering a template.

Classes:
    Config: Contains configuration settings for the Flask application,
            including supported languages, default locale, and timezone.

Routes:
    /: Renders the index template.

Usage:
    Run this module directly to start the Flask web server.
"""

from flask import Flask, render_template, request
from flask_babel import Babel


class Config():
    """
    Config class for Flask app settings.
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False
babel = Babel(app)


@app.route('/')
def index() -> str:
    """
    index
    """
    return render_template('3-index.html')


@babel.localeselector
def get_locale() -> str:
    """
    Gets the locale from request
    """
    locale = request.accept_languages.best_match(app.config['LANGUAGES'])
    # print(f"Selected locale: {locale}")
    return locale


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
