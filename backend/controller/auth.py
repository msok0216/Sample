from flask import Blueprint, request, jsonify, render_template
from flask_api import status
from ..db import client
#security import
from bson.objectid import ObjectId
from flask_bcrypt import Bcrypt
from flask_jwt_extended import create_access_token

import os
import bcrypt
import jwt

auth = Blueprint('auth', __name__, template_folder="../../frontend/public")

# TODO look at flask-login

# auth = flask("__main__")
db = client.get_database('sample')
# add more security measures: serialization, send session id instead of actual inforamtion, encryption
# also add a server side validation method: marshmallow?
@auth.route('/login', methods=['POST'])
@auth.route('/googlelogin', methods=['POST'])
def login():
    result = ''
    if request.method == 'POST':
        request_json = request.json
        id_val = request_json['id']
        pwd_val = request_json['pwd']
        user = db.user.find_one({'id': id_val})
        if user:
            # argument order matters here
            if bcrypt.checkpw(bytes(pwd_val, encoding='utf-8'), bytes(user['pwd'], encoding='utf-8')):
                access_token = create_access_token(identity = {
                    'id': user['id'],
                    'name': user['name'],
                    'email': user['email']
                })
                result = jsonify({'token': access_token}), status.HTTP_202_ACCEPTED
            else:
                result = jsonify({'error': 'Invalid username and password'}), status.HTTP_401_UNAUTHORIZED
        else:
            result = jsonify({'result': 'No users found'}), status.HTTP_404_NOT_FOUND    
    return result

@auth.route('/signup', methods=['POST', 'GET'])
def signup():
    if request.method == 'POST':
        # args.get() is optional data, and args[] is required.
        # request.form is for POST, request.args is for GET
        # Try to improve the backend logic by using request.form or args instead in the future
        request_json = request.json
        name_val = request_json['name']
        id_val = request_json['id']
        pwd_val = request_json['pwd']
        pwd2_val = request_json['pwd2']
        email_val = request_json['email']
        if pwd_val == pwd2_val and email_val:
            hashed_pw = bcrypt.hashpw(bytes(pwd_val, encoding='utf-8'), os.environ.get('SALT').encode('utf-8'))
            new_user = {"name": name_val,
                        "id": id_val,
                        "pwd": hashed_pw.decode('utf-8'),
                        "email": email_val}
            db.get_collection('user').insert_one(new_user)
            user = db.get_collection('user').find_one({'id': id_val})
            return jsonify({"User Created" : user['id']}), status.HTTP_201_CREATED
    return jsonify({"error": "Invalid request"}), status.HTTP_400_BAD_REQUEST
