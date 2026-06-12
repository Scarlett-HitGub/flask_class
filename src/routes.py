from flask.blueprints import Blueprint
from flask import render_template
from src.forms import LoginForm

# blueprint define un modulo
bp = Blueprint("flasked", __name__, template_folder="../templates")


@bp.route("/")
@bp.route("/index")
def index():
    user = {"username": "eileen"}
    posts = [
        {"author": {"username": "Scarlett"}, "body": "Beautiful day in Punguiland!"},
        {"author": {"username": "Kote"}, "body": "The Mario movie was freaking flip!"},
    ]
    return render_template("index.html", title="Home", user=user, posts=posts)


@bp.route("/login")
def login():
    form = LoginForm()
    return render_templates('login.html',  title='Sign In', form=form)
