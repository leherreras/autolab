import codecs
import os

from flask import Flask, jsonify
from flask_login import LoginManager
from werkzeug.exceptions import HTTPException

from routes import create_routes
from utils.conn_db import conn

# Start app flask
app = Flask(__name__)

# Secret key app
app.secret_key = codecs.encode(os.urandom(32), 'hex')

# Start login manager
login_manager = LoginManager()
login_manager.init_app(app)

# Create DB connection
db = conn(app)

# create all routes
create_routes(app)


@app.errorhandler(HTTPException)
def handle_exception(e):
    """Return JSON instead of HTML for HTTP errors."""
    # start with the correct headers and status code from the error
    # response = e.get_response()
    # replace the body with JSON
    data = {
        "code": e.code,
        "name": e.name,
        "description": e.description,
    }
    return jsonify(data), e.code



@app.route('/')
def hello_world():
    return jsonify("The api is work")


if __name__ == '__main__':
    app.run()
