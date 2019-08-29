import json
import os
import pandas as pd
import zipfile

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, PickleType, create_engine
from config import basedir

# Create instance of the db
db = SQLAlchemy()


# Unzip data to local directory
def unzip_data(zip_path):
  with zipfile.ZipFile(basedir + zip_path, 'r') as zip_ref:
    zip_ref.extractall(basedir)


# Load JSON to sqlite database and set datatypes
def load_database(data_path, db_name):
  # Create link with the database
  engine = create_engine('sqlite:///' + os.path.join(basedir, db_name), echo=False)

  # Load users from json file to the SQLite Database
  with open(basedir + data_path) as data_file:
    d = json.load(data_file)

    # Using Pandas Dataframe for easier data manipulation
    # Pickletype to convert lists (location, website) to binary arrays
    df = pd.DataFrame(data=d)
    df.to_sql('people', con=engine, if_exists="replace",
              dtype={"job": String, "company": String, "ssn": String, "residence": String,
                     "current_location": PickleType, "blood_group": String, "website": PickleType,
                     "username": String, "name": String, "sex": String, "address": String, "mail": String,
                     "birthdate": String})
