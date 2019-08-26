from scripts.database import db


class WebsiteModel(db.Model):
  __tablename__ = 'website'

  id = db.Column(db.Integer, primary_key=True)
  url = db.Column(db.String(128))
  user_id = db.Column(db.String(64), db.ForeignKey('people.id'))

  def __init__(self, url, user_id):
    self.url = url
    self.user_id = user_id

  def save_to_db(self):
      db.session.add(self)
      db.session.commit()

  def delete_from_db(self):
    db.session.delete(self)
    db.session.commit()

  def __repr__(self):
    return '<Website {}>'.format(self.url)
