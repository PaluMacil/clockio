from flask import Flask


def create_app():
    app = Flask(__name__)
    from .services import main as main_blueprint
    app.register_blueprint(main_blueprint, url_prefix='/sub/alarm/alarm.io')

    return app


if __name__ == '__main__':
    create_app().run(debug=True)
