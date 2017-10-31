from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///simple.db'

db = SQLAlchemy(app)

class User(db.Model):

	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(50), unique=True)
	password = db.Column(db.String(50))

	def __init__(self, username, password):
		self.username = username
		self.password = password

if __name__ == "__main__":
	db.drop_all()
	db.create_all()

	u1 = User('tom', 'cruise')
	u2 = User('val', 'kilmer')

	db.session.add_all([u1,u2])

	db.session.commit()

	print("created database and shit")
	