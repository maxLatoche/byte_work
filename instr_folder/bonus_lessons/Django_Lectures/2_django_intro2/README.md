# Django Intro PART DOS

### Learning Objectives
***Students will be able to...***

* Using url template tags
* Making django orm relations (Creation/Access)
* Using Request Object to Obtain Form Data
---

### Context

* Continuing to become Full Stack Developers

---

### Lesson

##### Part 1 - URLS In Depth

* Yesterday we placed all our urls in the `project/urls.py` file
* Now we will be looking at how to organize our urls to include endpoints specific to our application.
* Let's start by making a `urls.py` file inside our app
	* Show off our post/blog app
	* Our `app/urls.py` file will contain urls that may look like this
	
```
urlpatterns = [
	url(r'^create$', views.create, name="create"),
]
```
* The url function can be broken down into the following parameters
	* `url( <pattern>, <view function>, name="<url alias>")`
* The first two parameters are required
	* The url pattern
	* The function we are looking for in the `views.py`
	* The third parameter is a keyword argument using `"name"`
		* name allows us to target this specific urlpattern later on in our app
* Now we'll have to chang what the `projects/urls.py` file will say

```
from django.conf.urls import include, url

urlpatterns =[
	url(r'^todos/', include("todos.urls", namespace="todos")),
]
```
* There is a function called include in this example that has the following syntax
	* `include(<app/urls>,namespace="<name of url file>")`
* notice we had to import the `include` function from `django.conf.urls`
* include allows us to connect to all the urlpatterns in a specific app, it will take in two arguments
	* the first argument will be the app url location
	* the second argument is what will be the `namespace` that will indicate those application urls are being targeted
* The todos/urls.py file is pure Python code and is a simple mapping between URL patterns (regular expressions) to Django Views (Functions/Classes). Separating our urls into project/urls and app/urls keeps our app modular. 

***Set up settings file***

* Start to make your view functions target their specific templates
* settings.py -- BASE_DIR
	* base directory where manage.py is
	* os is a python module that will solve the path issues between operating systems
	* In DATABASES we see `os.path.join(BASE_DIR, database) - Example of how we do * not have a hardcoded filepath
* Setting up templates
* Go to settings.py
* Scroll to TEMPLATES
* Change the DIRS to have the base dir and templates
	* `'DIRS': [os.path.join(BASE_DIR, 'templates')],`

***Why go through all this trouble***

* It is important to organize your urls so we do not have anything overlap as our projects grow in size.
* Imagine a project for a blog
	* You may have several apps
		* posts
		* comments
		* users
	* Each of these apps have their own create url pattern and create view
	* We want to be able to use the name create because it's very descriptive
	* We give each app url pattern a namespace so Django doesn't get confused when we want to create something

***redirect and template***

* We can also utilize `namespace:name` in a redirect function or a url template tag
* redirect function
	* Find example in post blog app
* url template tag
	* `{% url 'namespace:name' %}`


##### Part 2 - DJANGO REQUESTS

***Five Min Exercise***

* open up the deaf grandpa app and print out the requests in the HTML form
* Lets talk about this for a few minutes

***Pseudo explain***

* wsgi - The thing that's listening for requests. Turns it into a python object and send it django project
* This object will contain the request information
* request.POST is a variable inside this wsgi object. (The information from the body when a form with method POST is sent)
* The querystring is placed in the request.GET attribute. 

##### Part 3 - Models Take Two

***Five Min Exercise***

* Go to the whiteboard and diagram the different DB relationships
* How might you represent membership? (pick one of the three examples or come up with your own)
	* membership to a gym
	* membership to a club
	* membership to a store

***Lesson Continue***

* Review of Database Relations
	* One to One
	* One to Many
	* Many to Many
* How do you represent membership?
* Django ORM has magic
	* Django Foreign key
	* Django has the ability to inverse lookup a relation
* Django Docs Tutorial, look at fields that will help with
	* Many to Many
	* One to Many / Foreign Key
* 1 App with two models. connect them in the models file
	* models.foreignkey takes parameter, it will be the class of the other model.
	* This shit figures out the id of the other table by itself
* Example:

```
class Employee(models.Model):
    name = models.CharField(max_length=30)
    birthday = models.DateField()

class Department(models.Model):
    name = models.CharField(max_length=30)
    budget = models.DecimalField(max_digits=15,decimal_places=2)
    employees = models.ManyToManyField(Employee)

class Manager(models.Model):
    employee = models.ForeignKey(Employee)

class Team(models.Model):
    name = models.CharField(max_length=30)
    manager = models.ForeignKey(Manager)
    employees = models.ManyToManyField(Employee)
```



