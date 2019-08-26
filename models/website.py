from directory_api import database


class Website(database.Model):
  __tablename__ = 'website'

  id = database.Column(database.Integer, primary_key=True)
  url = database.Column(database.String(128))
  user_id = database.Column(database.String(64), database.ForeignKey('user.id'))

  def __init__(self, url, user_id):
    self.url = url
    self.user_id = user_id

  def save_to_db(self):
      database.session.add(self)
      database.session.commit()

  def delete_from_db(self):
    database.session.delete(self)
    database.session.commit()

  def __repr__(self):
    return '<Website {}>'.format(self.url)
