from flask import Blueprint, request, jsonify, render_template
from flask_user import login_required
from flask_api import status
from ..db import client
main = Blueprint('auth', __name__, template_folder="../../frontend/public")


db = client.get_database('sample')

@main.route('/forum', methods=['POST', 'GET'])
def forum():
    if request.method == 'POST':
        # create a new post, add it to the front of the list and return it(or maybe handle it on the front end)
        return jsonify({'ee': 'aa'})
    elif request.method == 'GET':
        # sort posts by timeframe and return the list
        documents = db.forum.find({})
        list = []
        list.extend(documents)
        return list
    return jsonify({"error": "invalid request"}), status.HTTP_400_BAD_REQUEST

@main.route('/message/<int:id>', methods=['GET', 'POST', 'DELETE'])
# @login_required
def message(id):
    auth_header = request.headers.get('Authorization')
    access_token = auth_header.split(" ")[1]

    if access_token:
        messages = db.forum.find({"id": id})
        if not messages:
            return None, status.HTTP_204_NO_CONTENT
        return messages

@main.route('/profile/<int:id>', methods=['GET', 'POST', 'DELETE'])
# @login_required
def profile(id):
    auth_header = request.headers.get('Authorization')
    access_token = auth_header.split(" ")[1]

    if access_token:

