from flask import Flask
from dotenv import load_dotenv


def create_app() -> Flask:
    app = Flask(__name__)

    from src.routes import bp as flasked_bp
    app.register_blueprint(flasked_bp)
    app.config["TEMPLATES_AUTO_RELOAD"] = True

    return app

def load_dotenv(
    dotenv_path: StrPath | None = None,
    stream: IO[str] | None = None,
    verbose: bool = False,
    override: bool = False,
    interpolate: bool = True,
    encoding: str | None = "utf-8"
) -> bool

if __name__ == "__main__":
    flask_app = create_app()
    flask_app.run()
