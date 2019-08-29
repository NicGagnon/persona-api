import json
import unittest
import os

from scripts import app
from config import basedir, TEST_API_DATABASE, TEST_JSON_PATH
from scripts.database import db, load_database


class MyTestCase(unittest.TestCase):
  #execute before each test
  def setUp(self):
    with app.app_context():
      app.config['TESTING'] = True
      app.config['WTF_CSRF_ENABLED'] = False
      app.config['DEBUG'] = False
      app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, TEST_API_DATABASE)
      db.init_app(app)
      self.app = app.test_client()
      load_database(TEST_JSON_PATH, TEST_API_DATABASE)
      db.create_all()
      self.assertEqual(app.debug, False)

  # executed after each test
  def tearDown(self):
    with app.app_context():
      db.drop_all()
      db.session.commit()

  def test_main_page(self):
    with app.app_context():
      response = self.app.get('/', follow_redirects=True)
      self.assertEqual(200, response.status_code)

  def test_search_page(self):
    with app.app_context():
      response = self.app.get('/search', follow_redirects=True)
      self.assertEqual(200, response.status_code)

  def test_found_username(self):
    with app.app_context():
      response = self.app.get('/search/mauriceharris', follow_redirects=True)
      json_data = json.loads(response.data.decode('utf-8'))
      self.assertEqual(200, response.status_code)
      self.assertIn('Success', json_data['message'])

  def test_look_nonexistent_username(self):
    with app.app_context():
      response = self.app.get('/search/foobar', follow_redirects=True)
      self.assertEqual(404, response.status_code)

  def test_no_username(self):
    with app.app_context():
      response = self.app.get('/search/', follow_redirects=True)
      self.assertEqual(404, response.status_code)

  def test_people_page(self):
    with app.app_context():
      response = self.app.get('/people', follow_redirects=True)
      self.assertEqual(200, response.status_code)

  def test_delete_person(self):
    with app.app_context():
      response = self.app.delete('/people/smithhazel', follow_redirects=True)
      self.assertEqual(204, response.status_code)

  def test_delete_nonexistent_person(self):
    with app.app_context():
      response = self.app.delete('/people/foobar', follow_redirects=True)
      self.assertEqual(404, response.status_code)

  def test_delete_already_deleted_person(self):
    with app.app_context():
      response = self.app.delete('/people/smithhazel', follow_redirects=True)
      self.assertEqual(204, response.status_code)
      response = self.app.delete('/people/smithhazel', follow_redirects=True)
      self.assertEqual(404, response.status_code)

  def test_search_for_deleted_person(self):
    with app.app_context():
      response = self.app.delete('/people/smithhazel', follow_redirects=True)
      self.assertEqual(204, response.status_code)
      response = self.app.get('/search/smithhazel', follow_redirects=True)
      self.assertEqual(404, response.status_code)

if __name__ == '__main__':
    unittest.main()
