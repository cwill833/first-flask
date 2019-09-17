from flask import Flask

app = Flask(__name__)

app.config['SQLALCHEMY_DATA_URI'] = 'sqllite:///Users/chriswilliams/Desktop/Dev/flask/first_flask/database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False