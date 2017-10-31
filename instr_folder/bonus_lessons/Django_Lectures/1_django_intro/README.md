# Django Intro

### Learning Objectives
***Students will be able to...***

* How the internet works
* Install pip3 and Django
* Start a Django project and some apps
* Use basic regex commands

---

### Context

* Learn about the internet and how we can start putting things on it

---

### Lesson

##### Part 1 - What happens when I type Google.com into the browser and press enter?

* [Github Link](https://www.google.com/webhp?sourceid=chrome-instant&ion=1&espv=2&ie=UTF-8#q=what%20happens%20when%20you%20type%20google.com%20into%20the%20web%20browser)
* Browser parsing text
* Request
* HSTS list
* DNS
* HTTP / HTTPS
* Response

##### Part 2 - PIP Package Manager

***What is Pip***

* Pip is the package manager for Python
	* brew is the package manager for Macs
	* apt-get is the package manager for linux
	* npm is the package manager for node
	* and the list goes on
* We will be using `pip3` 
* pip3 is used as the package manager for python 3+

***Common Pip3 Commands***

* install pip3 - Everybody already has it
* install a package
	* `pip3 install name_of_package`
* upgrade a package
	* `pip3 install name_of_package --upgrade`
* uninstall a package
	* `pip3 uninstall name_of_package`
* view all packages installed
	* `pip3 freeze`
	* When working on a project you may see a `requirements.txt` file
	* This file will hold all the information of the kinds of packages a specific project is using
* Let's install virtual environment package and the newest version of django
* `pip3 install virtualenv`
* `pip3 install django-toolbelt`
	* `pip3 install django` OR `pip3 install django==1.9`
* 
	* if you leave off the version you will get the latest version
	* if you download an old version you can just upgrade that package
* NOTE!!!
	* Pip installs things to a folder on your computer. It's not pulling from some cloud spot online every day.
	* That is why pip and pip3 are different, or any other package manager for that matter
* `which` command
	* check out the which command
	* `which python3` will show you the path to the python 3 files

##### Part 3 - Starting Django / Code Along

***Common Commands***

* `django-admin startproject project_name`
	* Normally is `django-admin.py startproject project_name` if you just have django installed
	* We have django toolbelt installed so we can hold off on the `.py`

***Start a project***

* Now lets start our own project. Make a folder called `blog` and cd inside of it
* use django to start the blog
* Start a project
	* `django-admin.py startproject blog`
* change directory into the blog and take a look at the files
	* `settings.py` - This file contains the settings for our application. We have such things as:
		* `import os` and `BASE_DIR`== Django creates certain paths dynamically for you to use depending on what operating system you are on and where your files are
		* `Installed Apps` - What are the default apps that Django comes with. When we make new apps we will have to include them here
			* `django.contrib.admin` - allows us to user the superuser admin page
			* `django.contrib.auth` - authentication for users 
	* Database settings - Django comes with sqlite3 as default. We will use Postgres later on in the course
	* `urls.py` - The overall hub of all the urls you will have throughout building your project
	* `manage.py` - This file is used to call multiple commands in the terminal 
* Take a look at what you got so far
	* `python3 manage.py runserver`
	* `127.0.0.1:8000`

***Migrations***

* We have to make sure our database and django are all connected properly
* Using `manage.py` we can run a command called `migrate`
* `python3 manage.py makemigrations`
* `python3 manage.py migrate`
* Make migrations will make new files in your computer, we'll take a look at them later when we have to migrate a new application
	* These are used as blueprints to what your migrate should be doing

***Start an App***

* Apps vs Projects
	* Apps belong to a project
	* Projects contain multiple apps
* Apps are little components that build up the project as a whole
* Lets create an app for our project
	* `python3 manage.py startapp posts`
* posts is the name of our new app. 
* What files did we get with out new app
	* `admin.py` - don't touch for now
	* `tests.py` - don't touch for now
	* `models.py` - Just like the `Models in MVC pattern`
	* `views.py` - Help us organize what templates will be targeted during what request
	
***Using Models and Apps***

* We'll have to create a model class to use

```
from django.db import models

class Post(models.Model):
	title = models.CharField(max_length =120)
	content = models.TextField()
	# updated will auto update 
	updated = models.DateTimeField(auto_now=True, auto_now_add=False)
	# Timestamp will save and set one time
	timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

	
	def __str__(self):
		return self.title
```
* There are many different fields you can utilize in the models
	* [Django Docs to see different Fields we can use in Models](https://docs.djangoproject.com/en/1.9/ref/models/fields/)
* Then we have to connect this app to the `settings.py` file

```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'posts',
]
``` 
* Whenever we make a new app we'll have to make migrations and migrate.
	* `python3 manage.py makemigrations` - tells django we made changes to our models
	* `python3 manage.py migrate` - tells django to apply those changes to our database

***CRUD / HTTP VERBS***

* Review all your knowledge

***Five Min Exercise***

* All students must go to the whiteboard and draw out a table
* Each column represents the following
	* What CRUD stands for
	* What does it mean in SQL
	* What does it mean as HTTP VERBS
	* What does it mean in English

***Function Based Views***

* There are two types of views you will see in Django tutorials. They are Function Based Views and Class Based Views
* For today we will be looking at using Function Based Views and writing our views as functions
* `views.py` - is a file you will see in each of your apps
	* They do NOT hold templates or any html files
	* They take a request and turn it into a response
	* There are many ways to send a response
		* HttpResponse
		* render()
* Let's write a function that will return us something from the `views.py` file
* Import HttpResponse from django.http so we can send back a string

```
from django.http import HttpResponse
from django.shortcuts import render

def posts_home(request):

	return HttpResponse("<h1>HELLO WORLD</h1>")
```

***Request Response Cycle and `urls.py`***

* The view is useless unless we have something that talks to it
* SAVE US Request Response Cycle!!!!
* Remember when we create a view, it will handle a request and return a response.
* However how do we know what request goes to what view? 
* We do this with our urlpatterns
* URL patterns will map the request to where it needs to go
* Let's hardcode your post_home view into the urls.py

```
from posts import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # You can also import views
    url(r'^posts/$', views.post_home),
]
```

##### Part 4 - Render a template

* What if we want to render something more than just a string? Such as an HTML form
* Let's create a `templates` folder inside of the project `blog` and then an `index.html` folder inside of it
* Now we can change our view to use render instead of `HttpResponse`

```
def post_home(request):
	return render(request, "index.html",{})
```
* There is an empty dictionary for a reason. This is because we had nothing to pass into the template.
* For more dynamic information we can pass in dictionaries

```
def post_home(request):
	context = {
		"title": "Hello World"
	}
	return render(request, "index.html", context)
```
* Now we can alter the template we just made to take in the context.
* In your HTML use templating to bring in dynamic data

```
	<h1>{{title}}</h1>
```

***Your homework will consist of passing information back and forth to the views and templates. Think about how you will do this if you wanted to create a variable and store it in the context***

##### Part 5 - HTML forms

* In the view we're going to start using the form tag
* If you look at other Django tutorials you may see something called a Model Form. We'll take a look at those later. 
* For today's exercises you'll only need to know about how the HTML form works

```
	<form method="POST" action="">{%csrf_token%}

		{{ form.as_p }}

		<input type="submit" value="Create Post"/>
	</form>
```
* method - HTML forms are by default a GET method
	* HTML forms only take POST or GET
* What is POST vs GET
* Action - What url will this form be hitting
* csrf = cross site request forgery. We need security to validate data
* Django provides csrf token by default
	* `{%csrf_token%}`

##### Part 5 - Django ORM

* We built a `baby orm` in phase one. 
* Now we will be using Django's ORM
* I'm going to show you the different orm methods in the shell
* Open the shell 
	* `py manage.py shell` - 
		* Opens a python repl with regards to Django. 
		* Also connects to your DB so you can updated it in real time.
	* `py manage.py dbshell`
		* Opens the shell for database queries
* Import your models to use them
	* `>>> from posts.models import Post`
* Make a all query
	* `>>> Post.objects.all()`
* Make a filter query
	* `>>> Post.objects.filter(title="abc")`
	* `>>> Post.objects.filter(title__icontains="abc")`
* Create a new post
	* `>>> Post.objects.create(title="New Post", content="New Content")`
	* These are real time and actual instances of the class that have been entered into the Database. If we query the DB again you will see your new posts
	* `>>> Post.objects.all()`
* Assign your query set to a variable and loop through them.

```
queryset = Post.objects.all()

for obj in queryset:
	print(obj.title)
	print(obj.id)
	print(obj.pk)
```
* Think about how we can use these methods in the views.py. 
* Maybe assign their return values to a variable? 
