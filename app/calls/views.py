from flask import Blueprint

app = Blueprint('calls', __name__, url_prefix='/calls')


@app.route('/', methods=('POST',))
def index():
    return 'Hello, World'
