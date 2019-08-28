# Written by Nicolas Gagnon 2019

from scripts import app

app.run(host='0.0.0.0', port=80, debug=True)  # important to mention debug=True




"""
api.add_resource(User, '/search/<string:username>')
api.add_resource(UserData, '/search')

"""



