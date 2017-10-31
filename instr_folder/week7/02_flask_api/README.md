# Building a RESTful API


### Learning Objectives
***Students will be able to...***

* Build a RESTful API
 
---
### Context

* Continuing to become Full Stack Developers

---

### Lesson

##### Part 1 - What is an API?

* API - stands for application program interface
* Technically everything is an API
* However 99% of the time when API's are being discussed people are most likely talking about Web APIs
* These will take in a request and serve data to you in JSON format
* You may remember the homeworks involving the `OMDB API` or the `MarkIt API`
* We made a `request` and got data back in the form of `JSON`
* APIs should be built with a RESTful design

##### Part 4 - What is REST?

* What the hell is a RESTful API?

***Five Min Exercise***

* As a group, write on the board what CRUD is, and the four main HTTP verbs
	* Bonus if you can name all 8 HTTP verbs
* Research RESTful API structure. We will come back to discuss

***REST***

* REST stands for Representational State Transfer
* Building an RESTful API involves organizing your endpoints in an organized format with their respective HTTP Verbs
* What is the difference between 

```
GET localhost:8000/
GET localhost:8000/create
POST localhost:8000/create
GET localhost:8000/update/1
PUT localhost:8000/update/1
DELETE localhost:8000/1
```
* A RESTful framework will map to the FOUR MAIN CRUD operations in HTTP:
	* `GET`, `POST`, `PUT`, `DELETE`
* Notice we can have the same endpoint for two different operations. This is because they will be responding with different things 

##### Part 5 - JSON vs. XML

* We've discussed this earlier in the course but a brief overview
* Both JSON and XML are file formats.
	* XML is an older file format and is used with many older languages
	* You may find it used many times in large organizations such as Universities, or Banks. This is because their entire system is running on older technologies
	* JSON is the ideal file format for dealing with API's or even making APIs
	* JSON looks like a dictionary and we can navigate it as such
* Speaking of JSON, this is what we will be doing in our API assignments

##### Part 6 - CORS

* Cross Origin Resource Sharing.
* Allow requests that are not from this port to access the API.
* Without allowing CORS your server file will not accept any requests that are foreign to it. 
* Lucky for us, it's a easy hook up in flask with the `flask-cors` package

```
pip3 install flask-cors
```
* In your server file enter the following

```
from flask import Flask
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)

@app.route("/")
def helloWorld():
  return "Hello, cross-origin-world!"
```
* Check out the docs for more info. [Flask-Cors Documentation](https://flask-cors.readthedocs.io/en/latest/)



##### Resources

* Here are resources regarding REST, CSRF tokens, and curl. (A bash command that you will be using for the homework)
* [Tutorial Point for HTTP Request](http://www.tutorialspoint.com/http/http_requests.htm)
* [Andrew Havens Beginners Guide to Creating a REST API](http://www.andrewhavens.com/posts/20/beginners-guide-to-creating-a-rest-api/)
* [Miguel Grinberg Design a RESTful API with Python and Flask](http://blog.miguelgrinberg.com/post/designing-a-restful-api-with-python-and-flask)
* [What exactly is RESTful programming?](http://stackoverflow.com/questions/671118/what-exactly-is-restful-programming)
- [Representational State Transfer Wiki](https://en.wikipedia.org/wiki/Representational_state_transfer)
- [CSRF Exemption for APIs](http://stackoverflow.com/questions/10741339/do-csrf-attack-worries-apply-to-apis)
- [curl](http://superuser.com/questions/149329/what-is-the-curl-command-line-syntax-to-do-a-post-request) - in case you're crazy and don't want to use `POSTMAN`
