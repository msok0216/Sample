from flask import Blueprint, request, jsonify, render_template
from flask_api import status
from ..db import client
auth = Blueprint('auth', __name__, template_folder="../../frontend/public")

# auth = flask("__main__")
db = client.sample
# add more security measures: serialization, send session id instead of actual inforamtion, encryption
# also add a server side validation method: marshmallow?
@auth.route('/login', methods=['POST'])
@auth.route('/googlelogin', methods=['POST'])
def login():
    if request.method == 'POST':
        id_val = request.form.get('id')
        pwd_val = request.form.get('pwd')
        user_doc = db.user.find_one({'id': id_val})
        if not user_doc or user_doc('pwd') != pwd_val:
            return jsonify({"error": "User doesn't exist"}), status.HTTP_404_NOT_FOUND
        return jsonify({"success": "user data is successfully retrieved"}), status.HTTP_202_ACCEPTED
    return jsonify({"error": "Invalid request"}), status.HTTP_400_BAD_REQUEST
        


@auth.route('/signup', methods=['POST'])
def signup():
    if request.method == 'POST':
        name_val = request.form.get('name')
        id_val = request.form.get('id')
        pwd_val = request.form.get('pwd')
        pwd2_val = request.form.get('pwd2')
        email_val = request.form.get('email')
        if pwd_val == pwd2_val and email_val:
            new_user = {"name": name_val,
                        "id": id_val,
                        "pwd": pwd_val,
                        "email": email_val}
            new_user_id = db.user.insert_one(new_user)
            return jsonify({"User Created": new_user_id}), status.HTTP_201_CREATED
        return jsonify({"error": "invalid data"}), status.HTTP_400_BAD_REQUEST
    return jsonify({"error": "Invalid request"}), status.HTTP_202_ACCEPTED
