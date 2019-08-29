from flask import Flask
from flask_restful import Api
from config import Config, basedir, PROFILE_ZIP_PATH, PROFILE_JSON_PATH, API_DATABASE
from resources.people import PeopleData, People
from resources.search import Search, SearchData
from scripts.database import db, load_database, unzip_data

import markdown


# Create an instance of flask
app = Flask(__name__)
app.config.from_object(Config)

# Unzip file, load json to database and initiate the database
unzip_data(PROFILE_ZIP_PATH)
load_database(PROFILE_JSON_PATH, API_DATABASE)
db.init_app(app)

# Create an instance of flask Restful
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


# API endpoints
api.add_resource(PeopleData, '/people')
api.add_resource(People, '/people/<string:username>')
api.add_resource(Search, '/search/<string:username>')
api.add_resource(SearchData, '/search')
