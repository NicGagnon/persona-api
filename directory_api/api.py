# Written by Nicolas Gagnon 2019
from directory_api import api, app


# app.run(host='0.0.0.0', port=80, debug=True)


@app.before_first_request
def create_tables():
    db.create_all()


# what the api endpoints will look like
"""
api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(UserRegister, '/register')
api.add_resource(Store, '/store/<string:name>')
api.add_resource(StoreList, '/stores')
"""

if __name__ == '__main__':
    from directory_api.database import db  # Avoid circular import
    db.init_app(app)
    app.run(debug=True)  # important to mention debug=True
