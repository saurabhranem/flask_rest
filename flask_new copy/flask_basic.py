from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/hello')
def hello():
    return jsonify({"data": "Hello, World!"})


@app.route('/new', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        some_json = request.get_json()
        return jsonify({'you sent': some_json}), 201
    else:
        return jsonify({"about": "hello saurabh"}), 201


@app.route('/multiply/<int:num>', methods=['GET'])
def multiply(num):
    return jsonify({'data': num*10})


if __name__ == '__main__':
    app.run()
