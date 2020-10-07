from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return {'data': 'hello saurabh'}

    def post(self):
        some_json = request.get_json()
        return {'sent_data': some_json}

class Multiply(Resource):
    def get(self, num):
        return {'result': num*10}

api.add_resource(HelloWorld, '/new')
api.add_resource(Multiply, '/multiply/<int:num>')


if __name__ == '__main__':
    app.run()