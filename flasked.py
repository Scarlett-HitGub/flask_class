from flask.blueprints import Blueprint
# blueprint define un modulo
bp = Blueprint("flasked",__name__)

@bp.route("/")
def hello_world():
    return "<p>Hello, World!</p>"