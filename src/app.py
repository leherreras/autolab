from flask import Flask, jsonify

from routes import create_routes
from utils.conn_db import conn

app = Flask(__name__)
db = conn(app)


@app.route('/')
def hello_world():  # put application's code here
    return jsonify("The api is work")


create_routes(app)

if __name__ == '__main__':
    db.create_all()
    app.run()
