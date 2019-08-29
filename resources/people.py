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
  # Return pagination of names and usernames
  # todo still need to implement pagination functionality, SQLalchemy has built in pagination,
  #  but doesn't work with tuple returned from .with_entities
  def get(self):
    names = [json.dumps(person).strip('[]""') for person in PeopleModel.query.with_entities(PeopleModel.name)]
    usernames = [json.dumps(person).strip('[]""') for person in PeopleModel.query.with_entities(PeopleModel.username)]
    peopledata = []
    for index in range(len(names)):
      peopledata.append({"name": names[index], "username": usernames[index]})
    return {"data": peopledata}, 200

