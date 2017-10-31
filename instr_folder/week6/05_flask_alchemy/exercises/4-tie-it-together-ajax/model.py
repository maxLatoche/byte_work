'''
model.py
'''
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///thinkpads.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Person(db.Model):
    _id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), unique=True)
    thinkpads = db.relationship('ThinkPad',
                                backref='person',
                                lazy='dynamic')

    def __init__(self, name):
        self.name = name

class ThinkPad(db.Model):
    _id = db.Column(db.Integer, primary_key=True)
    serial = db.Column(db.Integer, unique=True)
    model = db.Column(db.String(10))
    person_id = db.Column(db.Integer, db.ForeignKey('person._id'))

    def __init__(self, serial, model, person_id):
        self.serial = serial
        self.model = model
        self.person_id = person_id

if __name__ == "__main__":
    db.drop_all()
    db.create_all()

    cody = Person('cody')
    db.session.add(cody)
    db.session.commit()
    
    cody = Person.query.filter_by(name='cody').first()
    X220 = ThinkPad(12345, 'X220', cody._id)
    T530 = ThinkPad(67890, 'T530', cody._id)
    db.session.add(X220)
    db.session.add(T530)
    db.session.commit()
