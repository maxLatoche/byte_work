# Login Application

* Now we'll be combining all of the skills you have learned to build a full fledged login application. 
* A user should be able to go to the home route and choose between login or register. 
* If they log in a request should be made to the server file that will check the database and to see if the input is valid
* If they register, a request should be made to the server to make that user in the database IF that username is not already taken

### Process

* Create your database
* Create a models file to talk to the database
* Create a server file that will talk to the models file
* Decide on what your routes will be. 
* Decide on the template/templates you will use
* How will the request be sent to the routes
* What will your flask server respond with? 

### Hints

* You will use:
  * SQLAlchemy
  * forms
  * GET and POST requests
  * templates
  * routes
  * variable rules
* Make sure you do `ONE METHOD AT A TIME!!!!`
	* One model, make sure it touches your controller/server file 
	* One route that will accept one request and return one response. 
	* Then move on to the next thing
	
### Luxury Goals

* Add CSS
* Make this Single Page, using AJAX and DOM Manipulation. 
