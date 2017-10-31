'''
model.py

A User class with a password.
'''
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), unique=True)
    password = db.Column(db.String(30))

    def __init__(self, u, p):
        self.username = u
        self.password = p

if __name__ == "__main__":
    db.drop_all()
    db.create_all()

    k = User('kevin', 'duck')
    s = User('space', 'cash')
    g = User('gandalf', 'ring')

    db.session.add(k)
    db.session.add(s)
    db.session.add(g)

    db.session.commit()
