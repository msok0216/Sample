from flask import Blueprint, request, jsonify, render_template
auth = Blueprint('auth', __name__)

# auth = flask("__main__")

@auth.route('/login', methods=['GET'])
@auth.route('/googlelogin', methods=['GET'])
def login():
    if request.method == 'GET':
        return render_template("index.html")
    return render_template("index.html")
        


# @auth.route('/signup', methods=['POST'])