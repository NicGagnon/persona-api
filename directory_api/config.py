# Config file for database
#
import os
from directory_api import app

basedir = os.path.dirname(app.root_path)


class Config(object):
  SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
  SQLALCHEMY_TRACK_MODIFICATIONS = False
