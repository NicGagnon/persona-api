from scripts.database import db


class Location(db.Model):
  __tablename__ = 'location'

  id = db.Column(db.Integer, primary_key=True)
  lat = db.Column(db.Integer)
  lon = db.Column(db.Integer)
  user_id = db.Column(db.String(64), db.ForeignKey('people.id'))

  def __init__(self, lat, lon, user_id):
    self.lat = lat
    self.lon = lon
    self.user_id = user_id

  def __repr__(self):
    return '<Location: Lat {}, Lon {}>'.format(self.lat, self.lon)
