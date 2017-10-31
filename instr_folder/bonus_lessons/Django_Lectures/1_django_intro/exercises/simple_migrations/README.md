# Django ORM SIMPLE Migrations

##### Objectives

* Make a new virtual environment using `virtualenv env`
* Start your virtual environment using source
* In that environment `pip3 install django`
* start a django project called `project`
* start a project app called `app`
* Go into `app/models.py` and add the following

```
class Person(models.Model):
		first_name = models.CharField(max_length=30)
		last_name = models.CharField(max_length=30)
		birthday = models.DateField()
```
* Feel free to look at the [Django Models Docs](https://docs.djangoproject.com/en/dev/topics/db/models/) to add more/different views
* How do we connect our app to our project?
* How do we create the schema for our database? 
	* HINT: It rhymes with "my crate"

#### The Employee Model

* Create an employees model with the following fields:  

```py
first_name  
last_name  
email  
job_title  
salary  
birthday  
hired_date
```
* Once you've done that, let's test by entering the interactive shell:  

```py
$ python3 manage.py shell
>>> from app.models import Employee
```
Run a few queries such as Employees.objects.all() and see what it returns!

#### Extend employees

Let's now extend our employee model and add our very own instance methods that return the following information:

* How many years old they are
* How many years and days they have worked at the company  
* Their full name (i.e. first name + last name)

#### Validate your fields

* Validations are crucial to ensuring the data we are entering into our datbase are acceptable as descriptions of data and/or business logic. Read up on validators [at the Django Models Validation Docs](https://docs.djangoproject.com/en/dev/ref/models/instances/#validating-objects) and [here is a stack overflow explanation](http://stackoverflow.com/questions/12945339/is-this-the-way-to-validate-django-model-fields)

* After a week of entering data in our DB. Rak finds out that you didn't have any validations on your employee model, and now a 4 year old got hired! And she's making half a million a year! How could you let this happen?

* Validate that the employees are at least 18 years of age. Also we've got a hiring freeze on senior level personnel - make sure no new employees can be entered with a salary greater than 200k.

* Overwrite the clean method for your class so that it raises a ValidationError if any of the constraints are not met.

* Then overwrite the save function for the model like so:

```py
def save(self, *args, **kwargs):
		self.full_clean()
		super(Players, self).save(*args, **kwargs)  
```
* There's a slightly different way to do this when we get into the complete Django suite - so you can't trust everything you read online if you google past the two articles above. However, all validations use the clean method, and overwriting it as well as save() seems to be a common practice.

* Read about how clean and full_clean work. What does super do? Do not move on until you understand what is happening and have a general idea what the above stack overflow link is going on about.

#### Regex Validator

* Now using the regex re library (`import re`) add a validator condition to your clean method to ensure a valid email address.

* Note - there is a built in RegexValidator class in Django. Don't use it, it's specifically for forms. Use Python's built in library 're' to match regular expressions.

#### Bonus - seed your DB!

* When you are in a small development team, then everyone has to enter in some data. Rather than do this independently, it is better to write a script so that everyone has similar data, and so that everyone has useful and appropriate data, rather than junk test data. To do this, you will need to navigate to the seeds.py file in your project's root directory and add to the `add_employee` function.

***Hint***

* Let's make use of the `convenience get_or_create()`method for creating model instances. As we don’t want to create duplicates of the same entry, we can use `get_or_create()` to check if the entry exists in the database for us. If it doesn’t exist, the method creates it. This can remove a lot of repetitive code for us - rather than doing this laborious check ourselves, we can make use of code that does exactly this for us. As we mentioned previously, why reinvent the wheel if it’s already there?



* When you're finished, have some fun querying your DB. Practice the [Django ORM queries](https://docs.djangoproject.com/en/dev/topics/db/queries/), like objects.all, objects.filter, and objects.get.
