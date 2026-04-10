from flask.blueprints import Blueprint
from flask import render_template
# blueprint define un modulo
bp = Blueprint("flasked",__name__)

@bp.route("/")
def index():
    user = {'username': 'eileen'}
    return render_template('index.html', title='Home', user=user)