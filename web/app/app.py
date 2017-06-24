import os
from flask import Flask

DB_USER = os.environ['DB_USER']
DB_PASS = os.environ['DB_PASS']
DB_SERVICE = os.environ['DB_SERVICE']
DB_PORT = os.environ['DB_PORT']
DB_NAME = os.environ['DB_NAME']


def create_app():
    """
    Create a Flask application using the app factory pattern.
    :return: Flask app
    """
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object('config.settings')
    app.config.from_pyfile('settings.py', silent=True)

    @app.route('/')
    def home():
        return 'postgresql://{0}:{1}@{2}:{3}/{4}'.format(
            DB_USER, DB_PASS, DB_SERVICE, DB_PORT, DB_NAME
        )

    return app
