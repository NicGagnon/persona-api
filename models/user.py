from directory_api import database

class User(database.Model):
  __tablename__ = 'user'

  id = database.Column(database.Integer, primary_key=True, autoincrement=True)
  job = database.Column(database.String(64))
  company = database.Column(database.String(64))
  ssn = database.Column(database.String(64), unique=True)
  residence = database.Column(database.String(128))
  current_location = database.relationship('Location', cascade="all,delete", backref=database.backref('user_location', lazy='joined'), lazy='dynamic')
  blood_group = database.Column(database.String(128))
  website = database.relationship('Website', cascade="all,delete", backref=database.backref('owner', lazy='joined'), lazy='dynamic')
  username = database.Column(database.String(64), unique=True)
  name = database.Column(database.String(64))
  sex = database.Column(database.String(8))
  address = database.Column(database.String(128))
  mail = database.Column(database.String(64))
  birthdate = database.Column(database.String(64))

  def __init__(self, job, company, ssn, residence, blood_group, username, name, sex, address, mail, birthdate):
    self.job = job
    self.company = company
    self.ssn = ssn
    self.residence = residence
    self.blood_group = blood_group
    self.username = username
    self.name = name
    self.sex = sex
    self.address = address
    self.mail = mail
    self.birthdate = birthdate

  def save_to_db(self):
    database.session.add(self)
    database.session.commit()

  @classmethod
  def find_by_username(cls, username):
    return cls.query.filter_by(username=username).first()

  @classmethod
  def find_by_id(cls, _id):
    return cls.query.filter_by(id=_id).first()

  def __repr__(self):
    return '<User {}>'.format(self.username)
