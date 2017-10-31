'''
app.py

A hardcoded login app with sessions.
'''

# Import Flask

from flask import (
    Flask,
    redirect,
    session,
    request,
    render_template
    )
# The docs might say to use "flask.ext.bcrypt" that is deprecated. use "flask_bcrypt" instead
from flask_bcrypt import Bcrypt

import os

app = Flask(__name__)
bcrypt = Bcrypt(app)

# pw_hash = bcrypt.generate_password_hash('hunter2')
# bcrypt.check_password_hash(pw_hash, 'hunter2')

@app.route('/')
def index():
    un = ''
    if session.get('logged_in'):
        un = session.get('username')
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
