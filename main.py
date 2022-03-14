from flask import Flask
from flask_restful import Api, Resource
import json

with open('valid.json') as deviceSchema:
    schema = json.load(deviceSchema)
##remove debug = true
app = Flask(__name__)
api = Api(app)
class Helloworld(Resource):
    def get(self):
        return schema

api.add_resource(Helloworld, "/")


if __name__ == "__main__":
	app.run(debug=True)
