Deaf Grandpa
============

Welcome to your first foray into web programming! Also, say hi to your deaf old Grandpa!

Well, don't say *'hi'*. Say *'HI GRANDPA'*. He can't hear so well.

If you speak in lower case to Grandpa, he should respond with *'What, I can't hear you Sonny!*

If you speak in all upper case, he should repeat what you said and then insult you with something funny.

Run the server to see what is already there in action. `python3 manage.py runserver`

This small exercise should go down like this:

#### The Main Page

We have the main page, where there is a form that will let you say something to grandpa. That is already built for you.

You will need to extend it so grandpa can say something back.

There are three components to this main page:

The "View": In Django, controller functions are called "views". It makes sense, because they control which variables and data the user gets to see in the template. You'll find this in `deafgrandpa/views.py`

The "Template": This is the .html file that is rendered on the page. It can be sent a dictionary from the view when rendered. You'll find this in `deafgrandpa/templates/deafgrandpa/*.html`

The URL dispatch: This is where the routing is done - it receives requests and tries to match the urls using regex. Take a look at `deafgrandpa/urls.py`

#### The Form Submission

If you look at the form, it has an action and a method. The action is `/say`, and the method is POST. So we will need to post data to `/say`.

Create a route in urls.py that will go to `/say`, and create the corresponding function in `views.py`.

All view functions take the request as an argument. It holds a lot of data about the user and their actions - do some sandboxing.

You will find the data the user sent in a dictionary stored at `request.POST`.

We don't want to render on a POST route - we want to redirect back to a GET. POSTs are only for sending data to server - GETs are for retrieving. [Read more about GET and POST](http://www.w3schools.com/tags/ref_httpmethods.asp).

So redirect back to the index route, with a [query string](http://en.wikipedia.org/wiki/Query_string) attached. Something like:
```
return redirect('/?grandpasays=I can't hear you Sonny!')
```
#### Back to the Main Page

Figure out how to get the contents of this query string and pass it into the rendered template. You will find resources on render and redirect below. The Django documentation is less accessible than we would all like, so read carefully.

#### Resources

[Django URL Dispatcher](https://docs.djangoproject.com/en/dev/topics/http/urls/)  
[Writing Views](https://docs.djangoproject.com/en/dev/topics/http/views/)  
[Render and Redirect](https://docs.djangoproject.com/en/dev/topics/http/shortcuts/)
