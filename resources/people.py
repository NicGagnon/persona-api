from flask_restful import Resource, reqparse
from models.people import People


class People(Resource):

  def get(self):
    # todo Returns all people with pagination
    pass

  def delete(self, username):
    # todo Delete a person
    pass
