from flask.blueprints import Blueprint
from flask import render_template
# blueprint define un modulo
bp = Blueprint("flasked",__name__,template_folder="./templates")

@bp.route("/")
def index():
    user = {'username': 'eileen'}
    post = [
        {
            'author': {'username': 'Eileen'},
            'body': 'Beautiful day in Punguiland!'
        }, 
        {
            'author': {'username': 'Kote'},
            'body': 'The Mario movie was freaking flip!'
        },
    ]
    return render_template('index.html', user=user)