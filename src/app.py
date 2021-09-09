from flask import Flask, jsonify

from routes import create_routes

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return jsonify("The api is work")


create_routes(app)

if __name__ == '__main__':
    app.run()
