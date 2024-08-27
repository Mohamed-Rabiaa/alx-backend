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

from flask import Flask, render_template, request, g
from flask_babel import Babel
from typing import Dict, Union


class Config:
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

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}

@app.route('/')
def index() -> str:
    """
    index
    """
    return render_template('5-index.html')


@babel.localeselector
def get_locale() -> str:
    """
    Gets the locale from request
    """
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


def get_user() -> Union[Dict, None]:
    """
    Retrieves the user information based on the login_as query parameter.
    """
    id = request.args.get('login_as')
    if id is None:
        return None
    try:
        user_id = int(id)
    except ValueError:
        return None
    return users.get(int(user_id))


@app.before_request
def before_request() -> None:
    """
    Sets the user globally available during the request lifecycle.
    """
    g.user = get_user()
    

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
