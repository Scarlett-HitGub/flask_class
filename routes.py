from flask.blueprints import Blueprint
# blueprint define un modulo
bp = Blueprint("flasked",__name__)

@bp.route("/")
def hello_world():
    user = {'username': 'eileen'}
    return '''
<html>
    <head> 
        <title>Microblog</title>
    </head>
    <body>
        <h1>Hi, ''' + user['username'] + '''
    </body>
</html>