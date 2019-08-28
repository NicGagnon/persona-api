from flask_restful import Resource
from models.people import PeopleModel
import json


class People(Resource):

  # Delete specific person with username
  def delete(self, username):
    user = PeopleModel.find_by_username(username)
    if user:
      user.delete_from_db()
      return {'message': 'User has been deleted'}, 204
    return {'message': 'Not Found'}, 404


class PeopleData(Resource):

  def get(self):
    return {'people': [{"name and username": json.dumps(person)} for person in
                       PeopleModel.query.with_entities(PeopleModel.name, PeopleModel.username)]}, 200

