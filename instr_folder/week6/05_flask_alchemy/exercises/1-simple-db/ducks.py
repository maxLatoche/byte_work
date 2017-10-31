'''
ducks.py

A model for ducks!
'''
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ducks.db'

# You can ignore this line if you want to. It suppresses a warning.
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Define your database table as a Python class.
class Duck(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    pass

if __name__ == "__main__":
    space = Duck('Space Cash', 'green', 55)
    kevin = Duck('Kevin', 'orange', 24)
    leeroy = Duck('LeeRoy', 'camo', 60)

    db.session.add(space)
    db.session.add(kevin)
    db.session.add(leeroy)
    db.session.commit()

    print('query all ducks', User.query.all())
    print('filter for leeroy', User.query.filter_by(name='leeroy').first())
