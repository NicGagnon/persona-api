from flask import Flask
from flask_restful import Api
from config import Config, basedir
from resources.people import PeopleData, People
from resources.search import Search, SearchData
from scripts.database import db

import markdown

# Create an instance of flask
app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)
api = Api(app)


@app.before_first_request
def create_tables():
  db.create_all()


# App.route directs the output of the function directly below to the URL passed. "/" is the root address.
@app.route("/")
def index():
  """ Print out some documentation for testing """

  with open(basedir + '/README.md', 'r') as markdown_file:
    # Read the content of the files
    content = markdown_file.read()

    # Convert to HTML
    return markdown.markdown(content)


api.add_resource(PeopleData, '/people')
api.add_resource(People, '/people/<string:username>')
api.add_resource(Search, '/search/<string:username>')
# api.add_resource(SearchData, '/search')
