from flask import Flask
from flask_cors import CORS
from .controller import auth

app = Flask("__main__")
CORS(app)

app.register_blueprint(auth)