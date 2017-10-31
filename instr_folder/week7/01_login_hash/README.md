# Database Security!!!

### Learning Objectives
***Students will be able to...***

* Use sessions to keep users logged in
* Use Bcrypt to hash passwords

---
### Context

* Continuing to become Full Stack Developers

---
### Lesson

##### Part 1 - Review

* What is Front End Programming? 
	* HTML / CSS / JS / AJAX / jQuery / Materialize
	* How the user interacts with the web page
	* How the user can send data to a server 
	* How does the website look
	* Single Page App vs Multi Page App
* What is Back End Programming
	* Python / Flask / Django 
	* How to build a server
	* Server accepts requests and returns responses
	* Return JSON, HTML, Templates, XML
	* How to build a database
	* How to talk to a database

##### Part 2 - Password Hashing

* We NEVER want to store the users actual passwords in our databse. 
* This is bad security!!!!!!!
* Before we send any passwords to our database we want to `hash` it.
* Password hashing means to take in user input for a password and run it through an algorithm where the output results in an extremely long string of seemingly random characters and numbers
* The idea is when a user enters their password, it will go through the process of this algorithm and if the output matches the hash in the database the user is verified
* We will be using Bcrypt to hash our passwords. 
* Bcrypt is a password hashing library that can be utilized in various back end frameworks. `Flask` / `Django` / `Express` / `Sinatra` / `Rails` and the like
* Make sure you print out the hashed password to see if it worked. 
* The check password method will return `True` or `False`
* The below is code of the included sample

```
pw = request.form.get('password')
pw_hash = bcrypt.generate_password_hash(pw)
print(pw_hash)
print(bcrypt.check_password_hash(pw_hash, pw))
```

***SIDE NOTE***

* Make sure you are importing the library `flask_bcrypt` and not just `bcrypt`. The bcrypt library can still work, but we want to use the `flask_bcrypt` one as it gives us the methods from the example above
* If you lost your password and a company emails your exact password back, instead of verification/ask for a new one, then they are storing your password as is in their database. That's some insecure shit, don't use their service again.

##### Part 3 - User Sessions

* Sessions allow us to store data between requests on either the client or server side. 
* Do we want to store data on the server side? **`NO!!!!!`**
* We want our server to be `"stateless"`
	* We do not want to store any information on our server. 
* So how can we allow users to stay logged in even when they close their browser?
* We'll be using sessions to accomplish this
* Sessions are part of the request object.
* Flask comes with sessions built in so we just have to import it

```
from flask import ( Flask, sessions )
```
* When we accept a request we can just call `session.get()`
* We can set up our session by just calling it like the object it is
* Here's an example from the sample code provided

```
        session['logged_in'] = True
        session['username'] = 'tom'
```