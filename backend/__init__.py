from flask import Flask, jsonify, request, json, Blueprint, request, render_template
from flask_cors import CORS
from .controller.auth import auth


app = Flask(__name__, template_folder='../frontend/public')
app.config['TESTING'] = True
app.config['ENV'] = 'development'
app.config['DEBUG'] = True
app.register_blueprint(auth)

CORS(app)

@app.route("/")
def index():
    return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True)