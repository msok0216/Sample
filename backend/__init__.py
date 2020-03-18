from flask import Flask, jsonify, request, json, Blueprint, request, render_template
from flask_cors import CORS
from .controller.auth import auth
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
import os


app = Flask(__name__, template_folder='../frontend/public')
app.config['TESTING'] = True
app.config['ENV'] = 'development'
app.config['DEBUG'] = True
app.config['JWT_SECRET_KEY'] = os.environ.get('SECRET_KEY')
app.register_blueprint(auth)

bcrypt = Bcrypt(app)
jwt = JWTManager(app)
CORS(app)

@app.route("/")
def index():
    return render_template("index.html")


if __name__ == '__main__':
    app.debug = True
    app.run(debug=True)