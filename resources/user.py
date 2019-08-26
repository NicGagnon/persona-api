from flask_restful import Resource, reqparse
from models.user import UserModel


class User(Resource):

  def get(self):
    # todo Searches the data for the specific username
    pass

  def delete(self, username):
    # todo Delete a user's data
    pass


class UserData(Resource):

  def put(self):
    # add all user data
    pass
