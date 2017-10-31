'''
controller.py

Simple login with a database.
'''
from flask import Flask, session, redirect
from model import *

@app.route('/')
def index():
    return 'You can not yet log in.'

@app.route('/login', methods=['POST'])
def login():
    return redirect('/')

@app.route('/logout')
def logout():
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)
