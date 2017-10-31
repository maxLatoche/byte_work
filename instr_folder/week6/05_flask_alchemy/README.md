# Flask-SQLAlchemy ORM

### Learning Objectives
***Students will be able to...***

* Apply a SQL ORM to our Flask server

---

### Context

* We want to build apps with persistent data

---

### Lesson

##### Part 1 - ORM Review

* ORM stands for `object relational mapper` 
* It converts data between incompatible type systems. 
* In the case of SQLAlchemy it will take make SQL queries using Python objects
* No longer will you have to write raw SQL
* You can simply call the corresponding method from the SQLAlchemy library

##### Part 2 - Installation and Setup

* Lets install it using pip3

```
pip3 install flask_sqlalchemy
```

Setting up a SQLAlchemy database requires a few steps. In your `models.py` file

1. import SQLAlchemy into your app - `from flask_sqlalchemy import SQLAlchemy`
2. configure your app to use a SQLite database - `app.config['SQLAlCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'`
3. create a database object from your app - `db = SQLAlchemy(app)`

* The `app.config` dictionary is a general-purpose place to store configuration variables used by the framework, the extensions, or the application itself. 
* Configuration values can be added to the app.config object using the standard dictionary syntax or with object methods that can import configuration values from files or the environment.

##### Part 3 - db.Model

* Any class inheriting from `db.Model` will receive the convenience methods and properties of the SQLALchemy ORM.
* Class properties are defined as subclasses of the `db` object.
* [This documentation is *very* helpful.](http://flask-sqlalchemy.pocoo.org/2.1/models/)

```
class User(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(80), unique=True)
  email = db.Column(db.String(120), unique=True)
```

##### db.create_all()

* The `.create_all()` method will build SQL tables from your class definitions. 
* You'll generally use this method in a file separate from your app called `createdb.py`.

##### db.session

* The `.session` property is the object containing the methods used to actually insert rows into the database, or remove them, and commit the changes.
* For now, we're only concerned with `db.session.add()` and `db.session.commit()`.
* Soon, we will learn about a completely different kind of session. Plant in your head today that `db.session` is not the only place we use the word "session".

##### .query

* Classes inheriting from `db.Model` get a .query method for free that is used to gather data from your database.
* [Useful documentation is here.](http://flask-sqlalchemy.pocoo.org/2.1/queries/)

##### Render_template

* For us to tell Flask how to render different html files create a `templates` folder. 
* In here we will have our different html files.
* In our server file we will import `render_template` from flask
* Inside of our routes we will return that html file using `render_template`
* Our file structure will look like this

```
- app
	- static
		- main.js
	- templates
		- index.html
		- login.html
	- server.py
```
* Now our flask server may look like this

```
from flask import Flask, render_template, jsonify

@app.route('/')
def index():
    persons = Person.query.all()
    return render_template(
                        'home.html',
                        persons=persons)
```
* Notice that we used "render_template" without having to specify `template/home.html`
* `render_template` will know to look for a folder called `templates` for these html files


