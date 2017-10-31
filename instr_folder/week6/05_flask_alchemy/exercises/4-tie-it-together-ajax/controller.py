from flask import Flask, render_template, jsonify
from model import *

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///thinkpads.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

@app.route('/')
def index():
    persons = Person.query.all()
    return render_template(
                        'home.html',
                        persons=persons)

@app.route('/person/<person_id>')
def person_pads(person_id):
    person = Person.query.filter_by(_id=person_id).first()
    # pads = ThinkPad.query.filter_by(person_id=person._id).all()
    pads = person.thinkpads.all()
    return render_template(
                        'detail.html',
                        person=person,
                        pads=pads,
                        )

@app.route('/add-person', methods=['POST'])
def add_person():
    return jsonify(persons='lots of people')

@app.route('/add-thinkpad', methods=['POST'])
def add_pad():
    return jsonify(success=True)

if __name__ == "__main__":
    app.run(debug=True)
