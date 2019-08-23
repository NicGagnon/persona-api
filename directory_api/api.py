# Written by Nicolas Gagnon 2019
from directory_api import app

app.run(host='0.0.0.0', port=80, debug=True)

#todo list
# - Create database in the docker container and load in the fake_profile.zip
# - Unzip the fake_profiles


# GET /search/{username} Searches the data for the specific username
def findUser(user_id):
  pass

# GET /people Returns all people with pagination
def getAllUsers():
  pass

# DELETE /people/{username} Delete a person
def deleteUser(user_id):
  pass
