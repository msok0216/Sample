from flask import Blueprint, request, jsonify, render_template
auth = Blueprint('auth', __name__, template_folder="../../frontend/public")

# auth = flask("__main__")

list = []
@auth.route('/login', methods=['GET'])
@auth.route('/googlelogin', methods=['GET'])
def login():
    if request.method == 'GET':
        if request.form['id'] in list:
            return jsonify({"token": "yeeyee"})
    return jsonify({"error": "yeet"})
        


@auth.route('/signup', methods=['POST'])
def signup():
    return jsonify({"error": "error message"})