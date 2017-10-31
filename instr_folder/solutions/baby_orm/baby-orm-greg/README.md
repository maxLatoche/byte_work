Baby ORM - Querying
===================

Are you ready for this? Today we're going to build the first half of our own ORM, or Object-relational mapper. Read more about ORM [here](http://en.wikipedia.org/wiki/Object-relational_mapping)

This is to prepare you for how you will be interacting with the DB in Django and many other web frameworks. This will also be your first foray in to meta-programming - as in code that writes code for you. 

To put it simply, the ORM treats a table in our SQL database like a Python class, and each row in that table can be an instance of that class. While we have been building classes for our database to provide an easy to use interface, this takes it one step further and gives uniform database methods to every model class.

For example, to get all rows from the Users table:  

In SQL:  
		SELECT * FROM Users;

In Baby ORM:  
		Users.all()

To get all users named Greg:  

In SQL:  
		SELECT * FROM Users WHERE name = 'Greg';

In Baby ORM:  
		Users.filter(name="Greg")

Get the idea?

###Round 1: Create your Model class that all other models will inherit from

We've already created the skeleton you will need in orm_class.py. Don't touch the methods yet - just initialize the Model class. 

Remember we want any class, with any attributes to be able to inherit from this class.

You will need to use **kwargs, which allows you to pass any number of arguments and the class or function will treat it like a dictionary. 

You will also need to use the setattr()function.

Google these for further explanation.

Test all your methods against babyorm.db - there is data in the Users table and Stocks table. Check out the create_db.py file to see the schema - but don't run it or you'll have to pull again.

###Round 2: Write your all() method

The all() class method should return all rows in the database for a table whose name matches the class. The rows should be instances of the class - not just sqlite's return value. 

In a class method, the keyword "self" refers to the class. It is the same as writing the class name.

You'll want to look up how to get the name of the class, and how to get the column names from sqlite cursor.

###Round 3: Write your get() method

Finally we start doing some heavy lifting. get() should take a condition as an argument and return just 1 row as an object from that table. Limit the return to 1 in SQL, not in your program.

###Round 4: Write your filter() method

Like get(), filter should also take a condition as an argument. However it should return all rows that match the condition as objects from that table. 
