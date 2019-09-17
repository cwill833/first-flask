from flask import Flask

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Users/chriswilliams/Desktop/Dev/flask/first_flask/database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False