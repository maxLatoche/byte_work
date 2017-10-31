# Make a Real Estate API and Database

##### Description

* You've decided to leave your life of crime and help make America Great Again. What's the best way to do that? Real Estate!
* In this assignment we're going to make an API for Real Estate Listings
* Like many web APIs, we will not be rendering HTML. 
* We will be creating a web based interface that allows users to interact and perform CRUD operations with our DB
* This interaction will be done using HTTP requests (GET or POST) and our clients will be expecting to send or receive `JSON`.
* In an API routes/urls are known as `endpoints`
* These `endpoints` are the entry points to the database resources
* We will be following `RESTful` practices when building this API

##### Objective 1

* You will have two Models: `Agents`, `Listings`. 
* The Agents model will have:
	* `first_name`
	* `last_name`
	* `email`
	* `phone`
	* `company`
	* `token` - our pseudo api key we're giving the agent. We will do this by using the UUID library
* The Listings model will have: 
	* `City`
	* `State`
	* `Price`
	* `Square Feet`
	* `Number of Bedrooms`
	* `Number of Bathrooms`
	* `Amenities`
	* `Description`
	* `Date Listed`
	* `Rental or Purcased`
	* `Available or Sold`
	
***Hints***

* What library do we have to control date and time? These may also be specific model fields.
* Don't forget about the `boolean` data type
* Feel free to add more fields if you'd like
* We might want to hash our passwords
* 

##### Objective 2

* All agents should be able to see all listings and search specific listings.
* They should be able to search by the different parameters
* Each agent will be assigned a random key on creation that must be passed with every request. 
	* This will require the use of a `UUID`
	* This is our version of a "API KEY"
* We're going to use a [*Universally unique identifier*](https://en.wikipedia.org/wiki/Universally_unique_identifier) and pythons [UUID module](https://docs.python.org/3/library/uuid.html#uuid.UUID) to create unique identifiers. Here's how to make that key:

```
    from uuid import uuid4
    key = uuid4().hex
```

* When a user makes a request it may look something like this:

```
GET http://mytodolist.com/todos/<user_token>/
```

##### Objective 3

* RESTful, RESTful, RESTful
* We are making a RESTful API. 
* Our GET and POST routes should be organized
* Remember they can target the same endpoint, but what we return from each will and should be competely different.

***GET ROUTES***

* An agent should be able to hit endpoints that will get them all listings, or listings by:
	* price range?
	* City / State?
	* Bedroom Number
	* Bathroom Number
	* Square Feet
	* Rental or purchased
	* Sold or Available
	* Date Listed
* You should be able to use and test these in your browser. All errors due to user submission (bad key, incorrect endpoint) should return a 404 status code to the client.
* `HINT` - Many of these endpoints may look the same, what if we used args and kwargs?


***POST ROUTES***

* To make a proper POST request, you are going to `curl` from your terminal and send in the data to the server.  You will need to pass in the user token as below:

```     
curl -X POST "http://127.0.0.1:8000/todos/register" -d '{"password": "fluffy_bunny", "username": "jeff"}'
```
* Create an endpoint that allows an agent to add a new listing to the database with the users token
* Create an endpoint that marks a listing as sold or available (only if the token matches).
* Create an endpoint that updates a listing (only if the token matches). 
* Create an endpoint that deletes a given listing (only if the token matches).

##### IMPORTANT NOTES!!!!!

* Instead of using curl, this would be a great time to utilize that Postman Extension you downloaded earlier. 
* Trust me when I tell you POSTMAN will save you years of headaches vs curl requests
* All responses must be sent as `JSON Responses`
