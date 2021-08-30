
# Python API Jaime
from flask import Flask, request
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps
import praw
from flask import jsonify

db_connect = create_engine('sqlite:///chinook.db')
app = Flask(__name__)
api = Api(app)


class Url(Resource):
    def get(self):
        submissions = []
        r = request.args.get("r")
        return_list = []
        try:
            reddit = praw.Reddit(
                client_id="ZgIn80LRllJHToi3lzZ61A",
                client_secret="gaFXaVGpKEMwdPgvBl0wQWbaOBG5zA",
                user_agent="DeptAPI",
            )
            submissions = reddit.subreddit(r).hot(limit=5)
            for s in submissions:
                return_list.append(s.title)
        except Exception as e:
            print(str(e))

        return return_list

# Navigate to http://127.0.0.1:5002/reddit.com?r=<subredit>


api.add_resource(Url, '/reddit.com')  # Route_1


if __name__ == '__main__':
    app.run(port='5002')
