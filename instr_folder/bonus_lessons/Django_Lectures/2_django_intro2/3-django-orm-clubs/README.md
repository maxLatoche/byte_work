# MOAR ORM THANGS!!!

##### Description

* We're going to revisit the good old college days
* Remember when you could party all night and wake up in the morning with no hangover? 
* Remember when you could pack on as much food on your plate at the buffet style cafeteria and only gain five pounds?
* WELL NOW YOU'RE BACK
* Because you've been hired to build software to manage student clubs on a college campus.

##### Objectives

***Your Relationships (In Django...)***

* Design the schema in SQL designer, then in the Django ORM.

```
A student can have memberships to many clubs  
A club can have many students  
A student can have many interests  
A club can have many interests  
A student can have a title for each club they belong in  
```

***Making Queries***

* Create queries to show that your database has all of these relationships.
* Show all the students that belong to a given club, along with their titles.
* Show all of the students that have a given interest.
* Given a student, find the clubs that match their interests.

***NOTE***

* Remember if you are having trouble seeing the relationships in the shell use the `__str__` method in your tables. It'll help with easier reading

##### SAME OLD RESOURCES

* [Django's ORM Docs](https://docs.djangoproject.com/en/dev/topics/db/models/)  
* [Many to many example](https://docs.djangoproject.com/en/dev/topics/db/examples/many_to_many/)
