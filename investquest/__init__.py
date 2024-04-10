from flask import Flask


def create_app(test_confic = None):
    app = Flask(__name__)
    app.secret_key = 'truunbsdfsfg'

    from . import investquest
    app.register_blueprint(investquest.bp)

    return app
