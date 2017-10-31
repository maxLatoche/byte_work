# ORM and Unix Introduction

### Learning Objectives
***Students Will Be Able To***

* Wrap SQL queries inside Python objects to make an ORM

---
### Context

* When working with back end technologies many frameworks come with a short hand so there's no need to write out SQL code from scratch.

---
### Lesson

##### Part 1 - What is an ORM

* ORM stands for Object Relational Mapper.
* This is a term for a programming practice where we can convert a type system to an object oriented language.
* What does this mean in English?
* This means we will be wrapping our SQL queries into Python methods. Now the rows in a table can be instances of a class.
* As mentioned in the Context of this lesson, many frameworks will have access to an "ORM" so the programmer does not have to write SQL queries from scratch.

***NOTE***

* Another example is the non relational database Mongo and it's (kind of)ORM framework Mongoose

##### Part 2 - ORM SELECT ALL SQL Example

* If you had a music application and wanted to search all artists in your database it may look something like below:

```
SELECT * FROM Artist;
```
* After building your ORM you will only need to invoke the method you created. It may look something like this:

```
Artist.all()
```
* This can be called at any time a user wants to search for ALL artists
* How might we do this if we wanted to actually have some where conditions? return a specific value?

```
SELECT * FROM Artist WHERE name = "Linkin Park";
```
* With an ORM this may look like:

```
Artist.filter(name = "Linkin Park")
```
* What if we had multiple conditions? What can we use for that?
* Our query based on multiple conditions might look like this:
```
Artist.filter(name = "Linkin Park", song_title = "Numb")
```
* `**kwargs` will be able to help you out here!

***NOTE***

* Your ORM should be able to be used in any application. (That's the whole point of making an ORM)
* Earlier we had an app with Artists so the ORM call was `Artists.all()`. However, we should be able to call `.all()` in any app we attach an ORM to. 
* If we had a movies app the call may be `Movies.all()`

##### Part 3 - @classmethod and @staticmethod

* Let's look at some example code to get started here:

```
class Date:

    day = 0
    month = 0
    year = 0

    def __init__(self, day=0, month=0, year=0):
        self.day = day
        self.month = month
        self.year = year
```
* We're creating a `Date` class that we'll use to make `Date` objects later.
* Now let's imagine I want to make objects of type `Date` by only passing along a `string`, like `"31-3-1984"`. One way I can do this is with a `@classmethod`. To my Date class, I'll add the following code:

```
    @classmethod
    def from_string(cls, date_as_string):
        day, month, year = map(int,  date_as_string.split('-'))
        date1 = cls(day, month, year)
        return date1

date2 = Date.from_string('11-09-2012')
```
* You'll notice a few things here:
* First, the first parameter of the `from_string` function is `cls`. This is a placeholder that's similar to `self`. In this case, it stands for the `Date` class.
* Second, you'll notice that we use `cls` in the expression, `date1 = cls(day, month, year)`. This lets us make a new object of type `Date`.
* Third, you'll see the last thing we do is call the `from_string` method on the `Date` class. This is where we use `@classmethods`.
* You can read an extended explanation here: [@classmethods and @staticmethods](http://stackoverflow.com/questions/12179271/python-classmethod-and-staticmethod-for-beginner).

##### Part 4 - Moar Python syntax that will help with baby ORM: `setattr()`, `hasattr()`, `class.__name__`

* `setattr()` - This is used to set an attribute to an instance of a class. It takes in three parameters. The object name, the attribute name, and the value. How might you use this with kwargs?
* Example:

```
cat = Cat()

setattr(cat, "weight", 10)

value = getattr(cat, "weight")
print(value)
# output will be 10
```

----------
* `hasattr()` - This will check for an attribute in a instance. It will take in two parameters. The name of the object and the property you're looking for
* Example:

```python
box = Box()

# Create a width attribute.
setattr(box, "width", 15)

# The attribute exists.
if hasattr(box, "width"):
    print(True)

# Delete the width attribute.
delattr(box, "width")

# Width no longer exists.
if not hasattr(box, "width"):
    print(False)

# Output will be...
True
False
```
* If you see documentation for `getattr()` we suggest using hasattr over that because getattr can return an error and make it seem like it does not exists at all.

----------
* `class.__name__` - This is used to get our class name as a string
* Let's look at an example. Imagine we start our babyorm.py file with the following code:

```
class Model:
    def __init__(self):
        pass

    @classmethod
    def all(cls):
        pass

class Users(Model):
    pass

class Stocks(Model):
    pass
```
* Now, we want the `all()` method within the `Model` class to be able to query either the Users SQL table or the Stocks SQL table. We could use some syntax that looks like this to get the name of the class that's invoking the `all()` method:
```
    @classmethod
    def all(cls):
        #get the table name from the name of the child class
        table_name = cls.__name__
```
* At this point, the table_name variable will contain the name of whatever class is invoking that method. So if we did `Users.all()`, then `table_name` would contain the value `"Users"`.


----------
* `**kwargs` - we already studied this. Keyword arguments!!! wooooo
