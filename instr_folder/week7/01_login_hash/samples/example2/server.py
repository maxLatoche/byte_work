from model import *

from flask import (
	Flask,
	render_template,
	redirect,
	session,
	request
)

from flask_bcrypt import Bcrypt

import os

app = Flask(__name__)

bcrypt = Bcrypt(app)


@app.route('/')
def index():
    un = ''
    print(session)

    if session.get('logged_in'):
        un = session.get('username')
        print(session)
        print(session.get('logged_in'))

    return render_template('index.html', username=un)

@app.route('/login', methods=["POST"])
def login():
    # get the values from the input elements by targeting their "name" attributes
    un = request.form.get('username')
    pw = request.form.get('password')

    # returns a has of the password after running it through bcrypt
    pw_hash = bcrypt.generate_password_hash(pw)
    print(pw_hash)
    # prints True of False after checking that password against the bcrypts hash
    # How might we use this check password method to check against a users password value in our databse
    print(bcrypt.check_password_hash(pw_hash, pw))


    if un == 'tom' and pw == 'cruise':
        # create a session with specific attributes
        session['logged_in'] = True
        session['username'] = 'tom'
        session['user_id'] = "SQL Primary Key"
        session['userhash'] = "hash their username"
    return redirect('/')
    # In this method we hard coded the user name and password. 
    # How might we use a models file to check the user input to our SQL database

@app.route('/logout')
def logout():
    # Check if session logged in is True and turn it to false
    if session.get('logged_in'):
        session['logged_in'] = False
        session['username'] = False
    return redirect('/')

if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    app.run(debug=True)