# Django CRUD Practice

##### Description

* This application will be a reenactment of the `todos` exercise you did earlier on in the course.
* It is intended to help you practice building CRUD applications
* Check out the resources below if you need some help
	- [Django Model Fields](https://docs.djangoproject.com/en/1.8/ref/models/fields/)
	- [Django URL Dispatcher](https://docs.djangoproject.com/en/1.8/topics/http/urls/ )
	- [HTTP Methods for Restful Services](http://www.restapitutorial.com/lessons/httpmethods.html)

##### Objectives

***Model your database***

- Make a todo model in `todos/models.py` that has the fields `task`, `created_at`, and `completed` using the appropriate model fields.
- Like yesterday your model should inherit from `models.Model`
- Once you have defined your model make your migrations, migrate your db, and run your server.
* Remember all the steps about making apps and models before you decide to make and migrate items

***Organize your URL routes***

Check out our **two** `urls.py` files: 
- `project/urls.py` routes all requests to `/todos` 
- `todos/urls.py` file in the todos app. 

* Yesterday we placed all of our urls in the `project/urls.py` file
* Today we will practice organizing our urls further but making them specific to our apps
* Here are some of the examples from the lecture. Feel free to open up the lecture notes for more in depth bullets:
* `todos/urls.py`

```
urlpatterns = [
	url(r'^create$', views.create, name="create"),
]
```
* `project/urls.py` 

```
from django.conf.urls import include, url

urlpatterns =[
	url(r'^todos/', include("todos.urls", namespace="todos")),
]
```

***Make a CREATE route***

* Make a new route in your `todos/urls.py` file. 
	* It will be a create route (like above) and lead to a create view
	
* Your form on `index.html` should look something like this:
```html
<form action="{% url 'todos:create' %}" method="POST">
	{% csrf_token %}
	<input name="task" type="text">
	...
</form>
```
* Keep in mind that depending on the request.method (i.e. GET or POST) our function based view will do one of two things. When the `request.method == 'GET'` will render the html page that has the empty `todo` form and when the `request.method == 'POST'` create a new `todo`. After creating a new `todo` the create view should redirect to the main page.

***Make a READ route***

* The user is now able to create new todo objects
* We should allow them to view a list of all the todo objects
* We should also allow them to view the details of just one todo
* Create a view, url, and html file
	* view function
	* html file
	* templating in the html
	* use Django's ORM
* Once you have the list populating how can we make every todo link to a new page that will display only that specific information
* Visit the [Django docs on URLs](https://docs.djangoproject.com/en/dev/topics/http/urls/#named-groups) and read about Named Groups.You will need to use these in order to do your database look up for a `todo`.
* It should look something like this (Make sure you know what this regex is doing!): 

```py
url(r'^(?P<todo_id>[0-9]+)/$', views.all, name='all'),
```
* Your `index.html` should look something like this:

```html
<div>
{% for todo in todos %}
	<p>{{ todo.name }}</p>
{% endfor %}
</div>
```

***UPDATE***

* Great now we want to  users to be able to update any of their todo objects
* We want them to view the detailed information inside of a form, and update that information
* Below is an example of what that form may look like:
 
```html
<form name="todos" action="{% url 'todos:update' %}" method="POST">
	{% csrf_token %}
	<input name="name" type="text" value="{{todo.name}}">
	...
</form>
```
* When a user submits this it should update the todo and redirect to the todo objects detailed view
	* Or if you think it's better UI to link them to the list view

***DELETE***

* Finally, make a route that deletes a `todo` from the database. You don't really need a new page for this - just a route and a redirect. Remember `DELETE` is an operation that manipulates the database and should only accept `POST` requests.
