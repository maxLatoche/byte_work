# Real Estate API Consumption

#### Description

* Time to make use of that awesome Real Estate API
* We'll be building another project COMPLETELY SEPARATE from your API

#### Objectives

* You will be making a new application
* This project will be a Single Page application 
* It will have full CRUD access to your Real Estate API
* You will be making multiple ajax calls to the endpoints in your API
* Make sure to include:
	* jQuery CDN - for easy ajax calls
	* jQuery Cookies 
		* `<script src="http://cdnjs.cloudflare.com/ajax/libs/jquery-cookie/1.4.1/jquery.cookie.min.js"></script>`
* You can have two applications running at the same time as long as you change the ports
* Your API will run on port 5000 so make this app run on 3000 or 8000
```
app.run(127.0.0.1, 8000)
```

#### The Basics

* While we are handling it slightly differently, at the end of the day this is still a CRUD app. 
* All we are doing is Creating, Reading, Updating and Deleting. You have faced this simple problem before, let's focus on implementation.
* This is a single page application. That means that the page will never reload and never redirect. We're going to use jQuery and AJAX to get from the server, post to the server, and update the HTML on the page when appropriate.

#### Structure

* We're going to load all the HTML once, the first time the user hits the page. 
* Create a new server.py file
* The index route will load your HTML file
* Hook up jQuery to your HTML with a cdn, or if you downloaded it...
* You're also going to need to link your own JS file and CSS file from static files.

#### User Flow

* When the user hits the site they should see a form
* They can look at all listings
* Search specific listings
* create a new listing
* Apply the user token to the api calls. 
* For this assignment you can use one token for your ajax calls

##### WORK FLOW

* Work on this project together for Friday
* You can work seperately over the weekend or continue working together.
* PSEUDO CODE / USER STORIES / WIRE FRAME
	* How many buttons should there be?
	* How will the listings appear?
	* Where will they go on the page?
* Make one repository to work off of
	* Invite me to the repo
	* Utilize Git issues
 
##### HINTS

* Don't forget about event delegation. Callbacks, Events, and the like. 
* You will need to watch out for CORS. 
* Use JSONP to serialize your data in the ajax call.
 
##### Luxury Goals

* Maybe use some `modals` in your html and css to produce cool forms
* If you finish early take a stab at using Mustache.js to render your data. 
* [Mustache](https://github.com/janl/mustache.js) is a front-end templating engine, much like Django's engine. This way we don't have to write lots of HTML.
* Plan out your DOM, and try using some CSS to style things
* Plan your DOM carefully, and do at least _some_ CSS styling.
