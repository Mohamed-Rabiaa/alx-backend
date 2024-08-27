#!/usr/bin/env python3
"""
Basic Flask application module that defines a single index route
for rendering a template.

Routes:
    /: Renders the '0-index.html' template.

Usage:
    Run this module directly to start the Flask web server.
"""


from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    """
    index route
    """
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
