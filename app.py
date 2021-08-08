"""
This file contains URL routes for e-commerce API.
Author: Manika Arora
"""

import json
from core.checkout import checkout
from flask import Flask, request, make_response
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


# Checkout route
@app.route("/checkout", methods=['POST'])
def checkout_api():
    """
    This is the checkout API.
    """
    input_json = request.get_json()
    print("Input received...")

    # Function call for checkout action
    output = dict()
    output = checkout(input_json['id_list'])

    output = json.dumps(output)

    r = make_response(output)
    r.content_type = 'application/json'

    return r


if __name__ == '__main__':

    print("E-Commerce Server is Starting.")
    start_from_terminal(app)
