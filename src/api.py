# Written by Nicolas Gagnon 2019
from src import app

app.run(host='0.0.0.0', port=80, debug=True)

#todo list
# - GET /search/{username} Searches the data for the specific username
# - GET /people Returns all people with pagination
# - DELETE /people/{username} Delete a person


def findUser(user_id):
  pass

def getAllUsers():
  pass

def deleteUser(user_id):
  pass
