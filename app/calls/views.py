import os
from flask import Blueprint, request, jsonify, flash, redirect
from app.database import DB
from werkzeug.utils import secure_filename
from json import loads

app = Blueprint('calls', __name__, url_prefix='/calls')
collection = 'calls'
UPLOAD_FOLDER = './app/calls/uploads/'


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


@app.route('/upload', methods=('POST',))
def upload():
    if request.method == 'POST':
        if 'file' not in request.files:
            print('file not in req')
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('No selected file')
            print('file name blank')
            return redirect(request.url)
        if file:
            filename = secure_filename(file.filename)
            file.save(os.path.join(UPLOAD_FOLDER, filename))
            DB.insert_many(collection,
                           [loads(line.replace('.', '_'), ) for line in open(os.path.join(UPLOAD_FOLDER,
                                                                                          filename), 'r')])
            return jsonify({'ok': True, 'message': 'File uploaded successfully!'})

