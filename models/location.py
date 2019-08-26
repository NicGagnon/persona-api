from directory_api import database


class Location(database.Model):
  __tablename__ = 'location'

  id = database.Column(database.Integer, primary_key=True)
  lat = database.Column(database.Integer)
  lon = database.Column(database.Integer)
  user_id = database.Column(database.String(64), database.ForeignKey('user.id'))

  def __init__(self, lat, lon, user_id):
    self.lat = lat
    self.lon = lon
    self.user_id = user_id

  def __repr__(self):
    return '<Location: Lat {}, Lon {}>'.format(self.lat, self.lon)
