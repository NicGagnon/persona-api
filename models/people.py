from scripts.database import db

# SQLalchemy Model for each person in the database
class PeopleModel(db.Model):
  __tablename__ = 'people'

  index = db.Column(db.Integer, primary_key=True, autoincrement=True)
  job = db.Column(db.String(64))
  company = db.Column(db.String(64))
  ssn = db.Column(db.String(64), unique=True)
  residence = db.Column(db.String(128))
  current_location = db.Column(db.PickleType)
  blood_group = db.Column(db.String(128))
  website = db.Column(db.PickleType)
  username = db.Column(db.String(64), unique=True)
  name = db.Column(db.String(64))
  sex = db.Column(db.String(8))
  address = db.Column(db.String(128))
  mail = db.Column(db.String(64))
  birthdate = db.Column(db.String(64))

  def __init__(self, job, company, ssn, residence, location, blood_group, website, username, name, sex, address, mail,
               birthdate):
    self.job = job
    self.company = company
    self.ssn = ssn
    self.residence = residence
    self.location = location
    self.blood_group = blood_group
    self.website = website
    self.username = username
    self.name = name
    self.sex = sex
    self.address = address
    self.mail = mail
    self.birthdate = birthdate

  def save_to_db(self):
    db.session.add(self)
    db.session.commit()

  def delete_from_db(self):
    db.session.delete(self)
    db.session.commit()


  # Jsonify an instance of the PeopleModel
  def json(self):
    return {
      'job': self.job,
      'company': self.company,
      'ssn': self.ssn,
      'residence': self.residence,
      'current_location': self.current_location,
      'blood_group': self.blood_group,
      'website': self.website,
      'username': self.username,
      'name': self.name,
      'sex': self.sex,
      'address': self.address,
      'mail': self.mail,
      'birthdate': self.birthdate
    }

  @classmethod
  def find_by_username(cls, username):
    return cls.query.filter_by(username=username).first()

  def __repr__(self):
    return '<User {}>'.format(self.username)
