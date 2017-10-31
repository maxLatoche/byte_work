# Phase 2 Assessment - Mini Twitter!

* For your assessment today we'll be building our own mini version of Twitter.
* There will be `AT MOST TWO` pages. 
	* A user login page
	* A Tweets page
	* You can build this all as Single Page Application. 
* The Tweets page will have AJAX calls that will get new data and utilize DOM manipulation to render them on the page. 
* I've posted the user stories below 
* You can build this in either Flask or Django. Whichever you feel more comfortable with. 
* This may sound like a lot or it may sound confusing. Take your time to plan your application. We care more about the quality of your code than how large your code base is. 
* Good luck and feel free to ask questions for clarity.

#### User Stories

* Users should be able to register for an account
* Users should be able to log in 
	* Don't worry about sessions. Assume the user is not closing the window and opening it
	* Don't worry about password hashing
	* Both sessions and password hashing can be considered luxury goals
* After logging in Users should be able to see all the posts
* Users can make their own post that appear on a personal page
* Users can click a repost button on a post that is not theirs. 
	* It will automatically take that post and put it on their personal page. The page should not reload when the repost button is clicked.

#### Planning

* PLAN OUT YOUR APPLICATION!!!
* Planning lowers the time it takes to develop an app. 
* What will your endpoints be?
	* What endpoint will render an HTML file?
	* What endpoint will send back JSON data?
* How might your database look like?
	* We'll have at least two models, one for Users and one for posts
	* THINK about this idea of reposting. If a user clicks a repost how will that look in the database? 
* What will your templates look like?
* You can use any templating engine you want for rendering incoming JSON
	* Jinja
	* Mustache
	* Django Default

***NOTE!***

* Remember if you create a element dynamically after the page has loaded, you need to attach the proper event listener to that element if it needs an event. Or target the parent element. `HINT: Event Delegation` 
* Remember forms have some `DEFAULT` functionality

#### Luxury Goals

* Add User Sessions
* Add Password Hashing for User Login
* Make things look pretty - Honestly your app could look like crap, I just want it to work. If it works then feel free to make it look like better crap.
* Use Mustache.js for templating - Again, Mustache.js isn't needed but if you've tried it recently and you understand it, it can help with showing data dynamically
* Use `hashtags` to tag keywords - Really hard luxury goal
* Add a search bar that can search for those keywords

