from flask import Flask
from flask_restful import Api
from config import Config

import markdown
import os

# Create an instance of flask
app = Flask(__name__)
app.config.from_object(Config)
api = Api(app)

basedir = os.path.abspath(os.path.dirname(__file__))


# App.route directs the output of the function directly below to the URL passed. "/" is the root address.
@app.route("/")
def index():
  """ Print out some documentation for testing """

  with open(basedir + '/README.md', 'r') as markdown_file:
    # Read the content of the files
    content = markdown_file.read()

    # Convert to HTML
    return markdown.markdown(content)




