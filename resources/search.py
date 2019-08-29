from flask_restful import Resource
from models.people import PeopleModel
from scripts.database import db

class Search(Resource):
  # Returns specific person with username
  def get(self, username):
    user = PeopleModel.find_by_username(username)
    if user:
      return {'message': 'Success', 'data': user.json()}, 200
    return {'message': 'User does not exist'}, 404



class SearchData(Resource):
  # Function returns full data for all user in pagination
  def get(self):
    return {'people': [person.json() for person in PeopleModel.query.paginate(1, 20, False).items]}, 200
