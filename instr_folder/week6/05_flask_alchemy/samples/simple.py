'''
alch1.py

A simple example of a web app using SQLAlchemy.
'''
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Define the path to your database.
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///simple.db'

# You can ignore this line if you want to. It suppresses a warning.
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Create a database object from the SQLAlchemy class.
db = SQLAlchemy(app)

# Define your database table as a Python class.
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)

    def __init__(self, username, email):
        self.username = username
        self.email = email

if __name__ == "__main__":
    db.drop_all()
    db.create_all()

    admin = User('admin', 'admin@example.com')
    kevin = User('kevin', 'kevin@ducks.com')

    db.session.add(admin)
    db.session.add(kevin)

    db.session.commit()

    print('query all users', User.query.all())
    print('filter for kevin', User.query.filter_by(username='kevin').first())
