# Django Model Forms

### Learning Objectives
***Students will be able to...***

* Use Django Model Forms

---
### Context

* Continuing to become Full Stack Developers

---
### Lesson

##### Part 1 - Model Forms

* So we've been building out HTML forms from scratch.
* It was great to learn about GET, POST, and Action
* Today we will be learning about Model Forms
* Django allows us to render HTML forms using Model fields

***The six bullets of Model Forms***

* [Taken from pydanny](http://www.pydanny.com/core-concepts-django-modelforms.html)
	* Model forms render Model fields as HTML
	* Model forms select validators based off Model field definitions
	* Model forms don't have the display/change all available fields
	* Model forms save dictionaries to SQL tables
	* forms are just python constructs
	* forms validate python dictionaries


##### Part 2 - My Whiskey Blog Steps

* Create folder. `mkdir whiskey_blog`
* Change directory into folder. `cd whiskey_blog`
* Set up your `Virtual Environment`
	* Create your virtual environment. `virtualenv env`
	* Start your virtual environment. `source ./env/bin/activate`
	* You should see (env) at the front of your path in the terminal
	* Install Django with pip3. `pip3 install django`
	* Creating a Virtual environment is important to ensuring the requirements of different projects and separated. If you had a personal project running on Django 1.9, but had a group project working in Django 1.8, the virtual environments would ensure they do not mix up.
* Create your project folder. `django-admin.py startproject project`
* Change directory into project. `cd project`
	* We want to stick with the naming convention of `project` so we know which directory has our `settings.py` file and which directors are `apps`
* Create your app called posts. `python3 manage.py startapp posts`
* Add `posts` to the installed apps of your `settings.py` file

##### Part 3 - Post Model

* Set up your Post Model

```
from django.db import models
from django.core.urlresolvers import reverse
from django.core.exceptions import ValidationError
from .validators import *

class Post(models.Model):
	brand = models.CharField(max_length = 50, validators=[min_validation])
	brand_type = models.CharField(max_length = 80, validators=[min_validation])
	description = models.TextField(validators=[min_validation])
	price = models.DecimalField(max_digits = 6, decimal_places = 2)
	brand_email = models.EmailField(max_length = 50, blank=True)

	def __str__(self):
		return self.brand
		# return "{} {}".format(self.brand, self.brand_type)

	def get_absolute_url(self):
		
		return reverse("posts:detail", kwargs={"id":self.id})
```
##### Part 4 - Set up your URL.PY FileSSSSS

* Create a `urls.py` file inside the `posts` app and add the following `Function Based Views`

```
from django.conf.urls import url
from django.contrib import admin

###########################################################################
##########	URL Patterns Function Based Views		###############
###########################################################################

from .views import(
	posts_list,
	posts_create,
	posts_detail,
	posts_update,
	posts_delete,
	)

urlpatterns = [
	url(r'^$', posts_list, name='list'),
	url(r'^create$', posts_create, name='create'),
	url(r'^(?P<id>\d+)/$', posts_detail, name='detail'),
	url(r'^(?P<id>\d+)/update$', posts_update, name='update'),
	url(r'^(?P<id>\d+)/delete$', posts_delete, name='delete'),
]
```
* Your project level `urls.py` file should look like this

```
from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^posts/', include("posts.urls", namespace="posts")),
]

```

##### Part 5 - Setting up FUNCTION BASED VIEWS

* Now create our `Function Based Views` in the `views.py` file in the `posts` app

```
from django.shortcuts import render

def posts_list(req):
	whiskey_list = Post.objects.all()
	context = {
		"whiskey_list" : whiskey_list,
	}
	return render(req, "posts/list.html", context)

def posts_create(req):
	create_form = PostForm(req.POST or None)

	if create_form.is_valid():
		instance = create_form.save(commit=False)
		instance.save()
		return redirect(instance)
	context = {
		"create":create_form,
	}
	return render(req, "posts/create.html", context)

def posts_detail(req, id=None):
	whiskey = get_object_or_404(Post, id=id)
	print(whiskey.id)
	context = {
		"whiskey": whiskey
	}
	return render(req, "posts/detail.html", context)

def posts_update(req, id=None):

	whiskey = get_object_or_404(Post, id=id)

	update_form = PostForm(req.POST or None, instance = whiskey)
	print(update_form)
	if update_form.is_valid():
		instance = update_form.save()
		return redirect(instance)
	context = {
		"whiskey": update_form,
	}
	return render(req, "posts/update.html", context)
	
def posts_delete(req, id=None):

	instance=get_object_or_404(Post, id=id)
	instance.delete()
	return redirect('posts:list', permanent=True)

```

##### Part 6 - More Updates to Settings.py

* Lets update our settings file to look in the Base Directory for a static folder, a templates folder, and add the session engine

```
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, "templates"),],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```

* And at the bottom of your `settings.py` folder

```

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
    # '/var/www/static/',
]

# Sessions
# Added Manually

SESSION_ENGINE = "django.contrib.sessions.backends.signed_cookies"

```

##### Part 7 - Building your Template Files and Directories

* Now create two directories. `static` and `templates` in the same level as your `manage.py` file
* Inside of the base templates folder create a `base.html` file and add the following

```
{% load staticfiles %}

<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<link rel="stylesheet" href="{% static "style.css" %}">
	<title>Document</title>
</head>
<body>
	<h1>THIS IS THE NEW BASENESS SONNNNNNNN</h1>

		<div class=container>
			{% block content %}

			{% endblock content %}
		</div>

</body>
</html>
```
* In the static folder add a `style.css` file and just add something to make sure it's connected

```
h1{
	color: red;
	font-size: 2em;
	text-decoration: underline;
}
```
* Now lets add a templates folder inside of our `posts` app. Called `templates` AND inside of that folder create another folder called `posts`. The path should look like this `project/posts/templates/posts`. Inside of this directory create four html files. 
	* `create.html`
	* `detail.html`
	* `list.html`
	* `update.html`
* The following code is below
* CREATE.HTML

```
{% extends "base.html" %}
	
	{% block content %}
	
		<form action="" method="POST">{% csrf_token %}
			{{create}}

			<input type="submit" value="Create New Whiskey">
		</form>

	{% endblock content %}
```
* DETAIL.HTML

```
{% extends "base.html" %}

	{% block content %}

		<h4>{{whiskey.brand}}</h4>
		<h4>{{whiskey.brand_type}}</h4>
		<h4>{{whiskey.price}}</h4>
		<h4>{{whiskey.description}}</h4>
		


		<form action="{% url 'posts:update' whiskey.id %}">
			<input type="submit" value="UPDATE THIS WHISKEY">
		</form>

		<form action="{% url 'posts:delete' whiskey.id %}">
			<input type="submit" value="Delete this entry">
		</form>


		<form action="{% url 'posts:list' %}">
			<input type="submit" value="Back to list">
		</form>

	{% endblock content%}

```
* LIST.HTML

```
{% extends "base.html" %}

{% block content %}

	<form action="{% url 'posts:create' %}">
			<input type="submit" value="Add a new entry">
	</form>
	

	{% for whiskey in whiskey_list %}
		<ul>
			<h3><a href="{{whiskey.id}}">{{whiskey.brand}}</a></h3>
			<li>{{whiskey.brand_type}}</li>	
			<li>{{whiskey.price}}</li>
			<p>{{whiskey.description}}</p>
		</ul>

	{% endfor %}

{% endblock content %}
```
* UPDATE.HTML

```
{% extends "base.html" %}

	{% block content %}

		<form method="POST" action="">{% csrf_token %}

			<h4>{{ whiskey.brand.label_tag }}</h4>
			{{ whiskey.brand }}

			<h4>{{ whiskey.brand_type.label_tag }}</h4>
			{{ whiskey.brand_type }}

			<h4>{{ whiskey.price.label_tag }}</h4>
			{{ whiskey.price }}

			<h4>{{ whiskey.description.label_tag }}</h4>
			{{ whiskey.description }}


			<input type="submit" value="Update This Whiskey">
		</form>
	
	{% endblock content %}

```

##### Part 8 - Tell Django you want to use the Models to build out forms

* Now lets create a file `forms.py` inside of our `posts` app

```
from django import forms
from .models import Post

class PostForm(forms.ModelForm):
	
	class Meta:
		model = Post
		fields = [
			"brand",
			"brand_type",
			"description",
			"price",
			"brand_email"
		]
```






































