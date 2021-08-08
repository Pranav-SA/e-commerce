"""
This file contains URL routes for e-commerce API.
Author: Manika Arora
"""

from flask import Flask
app = Flask(__name__)


def start_from_terminal(app):
    """
    :param app: Flask application object.
    Parse command line options and start the server.
    """
    app.run()


def get_app():
    return app


# Basic route
@app.route("/")
def home():
    return "Welcome to e-commerce sample API."

# Add Checkout route


if __name__ == '__main__':

    print("E-Commerce Server is Starting.")
    start_from_terminal(app)
