import json
import os
import pandas as pd

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, PickleType, create_engine
from config import basedir

db = SQLAlchemy()


def load_database():
  engine = create_engine('sqlite:///' + os.path.join(basedir, 'api.db'), echo=False)
  with open(basedir + '/fake_profiles.json') as data_file:
    d = json.load(data_file)
    df = pd.DataFrame(data=d)
    df.to_sql('people', con=engine, if_exists="replace",
              dtype={"job": String, "company": String, "ssn": String, "residence": String,
                     "current_location": PickleType, "blood_group": String, "website": PickleType,
                     "username": String, "name": String, "sex": String, "address": String, "mail": String,
                     "birthdate": String})


if __name__ == '__main__':
  load_database()
