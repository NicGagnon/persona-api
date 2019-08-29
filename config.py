# Config file for database
#
import os

# Configuration variables to facilitate future refactoring or scaling
PROFILE_ZIP_PATH = '/fake_profiles.zip'
PROFILE_JSON_PATH = '/fake_profiles.json'
API_DATABASE = 'api.db'
TEST_API_DATABASE = 'test.db'
TEST_JSON_PATH = '/tests/test_profiles.json'
basedir = os.path.abspath(os.path.dirname(__file__))


# Configuration for SQLalchemy database
class Config(object):
  SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'api.db')
  SQLALCHEMY_TRACK_MODIFICATIONS = False
