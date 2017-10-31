Hardcoded Login
===============

In this app, you'll be using Flasks's `session` object for the first
time. A *session* is a secure cookie used to store a user's login
information.

A *cookie* is an object in the HTTP header than can be used to pass
data between the client and the server.

Import Flask's `session` object and treat it as a dictionary.

Build an app with three routes:
* `/`
* `/login`
* `/logout`

This app will only have one user: ReignD33r.

Your `/` route will display a login form if ReignD33r is not logged
in, and a welcome greeting if ReignD33r is logged in.

Your `/login` route will accept a POST request from the login
form and check if
the username and password match ReignD33r's username and password,
which you will hard code. If the username and password match, set
`session['logged_in'] = True`.

The `/login` route will redirect to your index page.

The `/logout` route will set `session['logged_in'] = False`.

To use sessions, the app must have a secret key, which you set through
the `app.secret_key` property.

`app.secret_key = os.urandom(12)`

Remember, to use `os` you need to `import os`.
