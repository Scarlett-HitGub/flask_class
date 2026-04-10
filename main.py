from flask import Flask
from dotenv import load_dotenv


def create_app() -> Flask:
    app = Flask(__name__)

    from flask_class.routes import bp as flasked_bp
    app.register_blueprint(flasked_bp)
    app.config["TEMPLATES_AUTO_RELOAD"] = True

    return app


if __name__ == "__main__":
    flask_app = create_app()
    flask_app.run()
