# Baby ORM

* Today you will be building your own ORM. Or at least part of it.
* Check out the [ORM Wiki](http://en.wikipedia.org/wiki/Object-relational_mapping)

##### Objective 1

* Create a model class that all the other models will inherit from
* Take a look at the orm_class.py file we included
* You will need to use `**kwargs` for some of these methods
* You will also need the `setattr()` function. Check out the [documentation](https://docs.python.org/3/library/functions.html#setattr)
	* Instead of having a value be self.something we want to set it to name.something

##### Objective 2

* Complete the `all()` method
* This method should return all rows in the database whose name matches the class
* The rows should be instances of the class, not just sqlite3's return value.
* A user can enter anything they want so how will we target the correct class/table
* Test your answers with the provided `babyorm.db`
* You might be asking why do we need to target the class name. Well what if we have multiple tables? Every table has their own class.

##### Objective 3

* Write your `get()` method
* This method will take in a condition and return 1 row from the table
* How can you limit the results to 1 row in SQL?

##### Objective 4

* Write your `filter()` method
* This method will take in a condition and return multiple rows from the table


***HINTS***

* Use the following
	* setattr()
		* This takes in three arguments, you can use `self` for the first argument
* kwargs
	* Remember these are keyword arguments, what can we use these for if the user is searching for things?
* How do you get the class name? What does the below mean

```
cls.__name__
```

