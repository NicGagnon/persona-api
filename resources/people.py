from flask_restful import Resource
from models.people import PeopleModel


class People(Resource):

  def get(self, username):
    # todo Returns specific person with username
    pass

  def delete(self, username):
    # todo Delete specific person with username
    pass


class PeopleList(Resource):

  def get(self):
    # todo Returns all people with pagination
    pass



