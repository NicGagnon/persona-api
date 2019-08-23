from flask import Flask
import markdown
import os
from config import Config
from flask_sqlalchemy import SQLAlchemy

# Create an instance of flask
app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
basedir = os.path.dirname(app.root_path)


# from app import routes, models

# App.route directs the output of the function directly below to the URL passed. "/" is the root address.
@app.route("/")
def index():
  """ Print out some documentation for testing """

  with open(basedir + '/README.md', 'r') as markdown_file:
    # Read the content of the files
    content = markdown_file.read()

    # Convert to HTML
    return markdown.markdown(content)
