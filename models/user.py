from directory_api import db

class User(db.Model):
  __tablename__ = 'user'

  id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  job = db.Column(db.String(64))
  company = db.Column(db.String(64))
  ssn = db.Column(db.String(64), unique=True)
  residence = db.Column(db.String(128))
  current_location = db.relationship('Location', cascade="all,delete", backref=db.backref('user_location', lazy='joined'), lazy='dynamic')
  blood_group = db.Column(db.String(128))
  website = db.relationship('Website', cascade="all,delete", backref=db.backref('owner', lazy='joined'), lazy='dynamic')
  username = db.Column(db.String(64), unique=True)
  name = db.Column(db.String(64))
  sex = db.Column(db.String(8))
  address = db.Column(db.String(128))
  mail = db.Column(db.String(64))
  birthdate = db.Column(db.String(64))

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
    db.session.add(self)
    db.session.commit()

  @classmethod
  def find_by_username(cls, username):
    return cls.query.filter_by(username=username).first()

  @classmethod
  def find_by_id(cls, _id):
    return cls.query.filter_by(id=_id).first()

  def __repr__(self):
    return '<User {}>'.format(self.username)
