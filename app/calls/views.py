from flask import Blueprint, request, jsonify
from app.database import DB

app = Blueprint('calls', __name__, url_prefix='/calls')
collection = 'calls'


@app.route('/', methods=('POST', 'GET'))
def index():
    if request.method == 'GET':
        query = {}
        data = DB.find_one(collection, query)
        return jsonify(data), 200

    data = request.get_json()
    if request.method == 'POST':
        if data.get('uuid', None):
            DB.insert(collection, data)
            return jsonify({'ok': True, 'message': 'Call created successfully!'})
        else:
            return jsonify({'ok': False, 'message': 'Bad request parameters!'})

