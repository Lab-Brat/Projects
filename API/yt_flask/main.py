from flask import Flask
from flask_restful import Api, Resource, reqparse

# initialize Flask application and an API
app = Flask(__name__)
api = Api(app)

# names = {"yara": {"age": 24, "gender": "male"},
#          "vasya": {"age": 25, "gender": "female"}}

# class TestString(Resource):
#     def get(self, name):
#         return names[name]

# registering TestString as a resourse for testing
# api.add_resource(TestString, "/testing/<string:name>")
# <> defines a parameter to be passed in to Request

video_args = reqparse.RequestParser()
video_args.add_argument("name", type=str, help="Name of the video")
video_args.add_argument("views", type=int, help="Views of the video")
video_args.add_argument("likes", type=int, help="Likes of the video")

videos = {2: {"name": "Vasya", "views": 3333333, "likes": 300}}

class Video(Resource):
    def get(self, video_id):
        return videos[video_id]

    def put(self, video_id):
        args = video_args.parse_args()
        videos[video_id] = args
        return videos[video_id], 201

api.add_resource(Video, "/video/<int:video_id>")

if __name__ == "__main__":
    # start server & Flask application
    app.run(debug=True) # when testing debug=True
