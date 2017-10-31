# Employees AND Departments

##### Description

* In yesterdays assignment we got practice with Django but building out an an app with employees.
* Today we will expand on that concept BUT in a new project
* This is more practice with Django's ORM and database relationships
* So make a new virtual environment, start a new project, and get ready for the prompt below

##### Objectives

***Database and the One to Many Relationship***

* Using the Django ORM, create tables with these values and relationships:

```
An employee has a name and a birthdate.  
An employee belongs to a department.

A department has a name and a budget.  
A department has many employees.
```
* Don't forget to makemigrations and migrate your db.

***Build out the rest***

* Now we've got some additional requirements.

```
An employee can be a manager.  
A manager has a team of employees.  
Employees can belong to multiple teams.  
An employee can be in multiple departments.  
```
* Remember after each change you should make migrations and migrate then to test the new code. If you are having trouble seeing the relationships, think about adding a `__str__` method to each of your tables, so that you get easier to read feedback.  

##### Resources

* [Django's ORM Docs](https://docs.djangoproject.com/en/dev/topics/db/models/)  
* [Many to many example](https://docs.djangoproject.com/en/dev/topics/db/examples/many_to_many/)
