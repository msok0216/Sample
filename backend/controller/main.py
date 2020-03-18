from flask import Blueprint, request, jsonify, render_template
from flask_api import status
from ..db import client
main = Blueprint('auth', __name__, template_folder="../../frontend/public")


db = client.sample

@main.route('/forum', methods=['POST', 'GET'])
def forum():
    if request.method == 'POST':
        return jsonify({'ee': 'aa'})
    elif request.method == 'GET':
        return jsonify({'ya': 'ya'})
    return jsonify({"error": "invalid request"}), status.HTTP_400_BAD_REQUEST