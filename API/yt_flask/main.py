from flask import Flask
from flask_restful import Api, Resource

# initialize Flask application and an API
app = Flask(__name__)
api = Api(app)

class TestString(Resource):
    def get(self):
        return {"data": "This is working just fine!"}

# registering TestString as a resourse for testing
api.add_resource(TestString, "/testing")

if __name__ == "__main__":
    # start server & Flask application
    app.run(debug=True) # when testing debug=True
