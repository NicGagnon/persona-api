# Contains just the name of the people

from scripts.database import db

class PeopleModel(db.Model):
  __tablename__ = 'people'

  id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  name = db.Column(db.String(64))
  username = db.Column(db.String(64))

  def __init__(self, name, username):
    self.name = name
    self.username = username
