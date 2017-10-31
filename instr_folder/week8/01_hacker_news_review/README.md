# Hacker News Clone

##### Description

* This exercise is to create your own [Hacker News](http://news.ycombinator.com) clone from scratch. 
* It is meant to incorporate many of the skills we learned this month.
* Feel free to work together for the planning / pseudo coding / wireframing
* HOWEVER, I would like for this prompt to be done solo on your own branches. 

##### Objectives

* Visit the hacker news links above
* Pseudo code / ERD / Wireframe / User Stories
* You will need at least three models
	* Posts
	* Users
	* Comments
* Make a `SIMPLE` user login, nothing complex
* Create a seed file so you can practice with some dummy data
	* The following Options are for Django. If you're doing it in Flask it'll be easier and faster to just write your own seed data in your createdb file
		* Option 1: [Faker](https://github.com/joke2k/faker) - a cool python package that allows you to generate dummy data
		* Option 2: Take a look at the seeds file from the debugging exercise in week 7 day 3
		* Option 3: Just open up the Django shell yourself and write a few users posts and comments in
* Think about when it is better to use AJAX
	* What part of your websites will we want to not refresh the page?
	* How many templates do you want your project to have?
	* Maybe we could use the `$.ajax` or `$.get` methods to grab our data faster
	* Remember AJAX is used here to pass data back and forth without having to re-render the page
	* Maybe use DOM manipulation to populate and empty certain divs. 
	* If you are making requests with an AJAX call and getting data back in the success function you might use `Mustache.js` templating instead of Vanilla JS DOM Manipulation.

##### Requirements

* You must have AJAX
* A User must be able to register and log in
* If a User logs in they should be able to see all post
* A User should be able to click on a post and view the comments for that post
* A User should be able to create a new post or a new comment on a post
* A user should be able to see all the post by them


##### Bonus - KEEP IT SIMPLE BEFORE YOU THINK ABOUT BONUSES

* You must use Mustache Templating
* Add comments onto comments
	* You can do this using Generic Relations
* Try using a PostgreSQL DB instead of SQLITE3 DB
* Upvotes and downvotes of articles





