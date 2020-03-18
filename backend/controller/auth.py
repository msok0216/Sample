from flask import Blueprint, request, jsonify, render_template
from flask_api import status
from ..db import client
import dns
auth = Blueprint('auth', __name__, template_folder="../../frontend/public")

# auth = flask("__main__")
db = client.get_database('sample')
# add more security measures: serialization, send session id instead of actual inforamtion, encryption
# also add a server side validation method: marshmallow?
@auth.route('/login', methods=['POST'])
@auth.route('/googlelogin', methods=['POST'])
def login():
    if request.method == 'POST':
        request_json = request.json
        id_val = request_json['id']
        pwd_val = request_json['pwd']
        user_doc = db.user.find_one({'id': id_val})
        if not user_doc or user_doc('pwd') != pwd_val:
            return jsonify({"error": "User doesn't exist"}), status.HTTP_404_NOT_FOUND
        return jsonify({"success": "user data is successfully retrieved"}), status.HTTP_202_ACCEPTED
    return jsonify({"error": "Invalid request"}), status.HTTP_400_BAD_REQUEST
        


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
            new_user = {"name": name_val,
                        "id": id_val,
                        "pwd": pwd_val,
                        "email": email_val}
            db.get_collection('user').insert_one(new_user)
            return jsonify({"User Created" : "Success"}), status.HTTP_201_CREATED
    return jsonify({"error": "Invalid request"}), status.HTTP_400_BAD_REQUEST
