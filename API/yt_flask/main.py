from flask import Flask
from flask_restful import Api, Resource, reqparse, abort
from flask_sqlalchemy import SQLAlchemy

# initialize Flask application and an API
app = Flask(__name__)
api = Api(app)

# parse all needed arguments
video_args = reqparse.RequestParser()
video_args.add_argument("name", type=str, help="Name of the video")
video_args.add_argument("views", type=int, help="Views of the video")
video_args.add_argument("likes", type=int, help="Likes of the video")

videos = {}

class ID_Status():
    """
    Provide functionality to query whether video_id exists
    in the database already or not.
    """
    def no_id(self, vid_id):
        if vid_id not in videos:
            abort(404, message="video_id not found")
        else:
            print('video_if found! Sending requested data...')

    def exist_id(self, vid_id):
        if vid_id in videos:
            abort(409, message="video_id already exists")

class Video(Resource):
    """
    A Resource that handles 3 types of requests, namely:
       1) get:    recieves video_id as input, checks if it
                  exists in a videos or not, then outputs it;
       2) put:    recieves video_id as input. parses arguments,
                  then adds id and arguments to videos;
       3) delete: recieves video_id as input, checks if it
                  exists in a videos or not, then deletes it;
    """
    def get(self, video_id):
        get_status = ID_Status()
        get_status.no_id(video_id)
        return videos[video_id]

    def put(self, video_id):
        args = video_args.parse_args()
        videos[video_id] = args
        return videos[video_id], 201

    def delete(self, video_id):
        get_status = ID_Status()
        get_status.exist_id(video_id)
        del videos[video_id]
        return 'deletion successful', 204

# registering Video as Resource
api.add_resource(Video, "/video/<int:video_id>")

if __name__ == "__main__":
    # start server & Flask application
    app.run(debug=True) # when testing debug=True
