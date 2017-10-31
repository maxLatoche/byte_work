A Flask App with SQL
====================

Today you face your greatest challenge!

Build a two page application using Flask with the following
*routes*:
* `/` - renders the homepage
* `/person/<primary_key_id>` - renders a page with the details of a
  person and their ThinkPads
* `/add-person`  - processes a form to add a person to the database
  and returns the new full list of persons as a JSON response
* `/add-thinkpad` - processes a form to add a thinkpad to the database and
  associate it with a person and returns a JSON response only
  detailing the success of the operation

Your home page will have a list of all persons, a form to enter a new
person, and a form to enter a ThinkPad.

You will use:
  * SQLAlchemy
  * forms
  * GET and POST requests
  * `$.ajax()`
  * templates
  * routes
  * variable rules
  * hopefully some CSS

All of this... ***FROM SCRATCH***.

Some sample code is included. Feel free to delete or alter any or all
of it.

If you finish, make it pretty!
If you get bored before you finish, make it pretty.
