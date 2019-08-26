# Written by Nicolas Gagnon 2019
from scripts import api, app


@app.before_first_request
def create_tables():
    db.create_all()


# what the api endpoints will look like
"""
api.add_resource(People, '/people/<string:username')
api.add_resource(PeopleList, '/people')
api.add_resource(User, '/search/<string:username>')
api.add_resource(UserData, '/search')

"""

if __name__ == '__main__':
    from scripts.database import db  # Avoid circular import
    db.init_app(app)
    app.run(host='0.0.0.0', port=80, debug=True)  # important to mention debug=True
