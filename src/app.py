from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return jsonify("The api is work")


if __name__ == '__main__':
    app.run()
