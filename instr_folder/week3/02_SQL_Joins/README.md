# Relational DB's / SQL Joins

### Learning Objectives
***Students will be able to...***

* Make SQL JOIN queries to grab data from multiple tables

---
### Context

* Advanced SQL Queries that allow us to pull data from multiple tables all at once without making multiple queries

---
### Lesson

##### Part 1 - Multiple Tables / Database Normalization

* Remember the music example from the first day of SQL? Draw out your example
	* Three tables
	* Artists, Songs, Albums
* In the music example the table `Albums` would have the foreign keys to both the artists and songs tables.

***Five Min Exercise***

* What are some pros and cons to having your database formatted this way?

***Database Normalization***

* This ERD follows the principles of [Database Normalization](https://en.wikipedia.org/wiki/Database_normalization)
* We are organizing our data to minimize redundancy
* It allows us to have more consistent data
* Normalizing a database involves taking one large table and breaking it up into smaller tables.
* Then use foreign keys to reference each other.

***Example***

* With the music database above, if we had it all on one table (also known as a flat table) then we would have to update everything just to insert one item
* With multiple tables we may only have to edit the songs table if a artist comes out with a new song. Or the albums table if there's a new album that consists of songs that already exists in the database.
* Less redundancies

***The One Bad Thing***

* We are using more memory to store all this data and build all these relationships

---

##### Part 2 - Exercise createdb / seed

***Five Min Exercise***

* Make a createdb file and a seed file.
* createdb file will have
	* two tables: `buildings` `residents`
	* Buildings will have three columns: `name`, `city`, `build_year`
	* residents will have three columns: `first_name`, `last_name`, `rent`
	* which table should have the foriegn key?

* seed your database with the following information

```
BUILDINGS =[
	["Empire State", "New York", 1930],
	["Bradbury", "Los Angeles", 1893],
	["White House", "Washington D.C.", 1800],
]

RESIDENTS = [
	["Jay", "Z", 100000],
	["Kobe", "Bryant", 90000],
	["Barack", "Obama", 50000],
]
```


---
***ANSWER***

CREATEDB FILE

```
import sqlite3

db = sqlite3.connect('livingdb')

cursor = db.cursor()

cursor.execute('''
	CREATE TABLE buildings(
		id INTEGER PRIMARY KEY AUTOINCREMENT,
		name TEXT,
		city TEXT,
		build_year INTEGER
	);
''')

cursor.execute('''
	CREATE TABLE residents(
		id INTEGER PRIMARY KEY AUTOINCREMENT,
		first_name TEXT,
		last_name TEXT,
		rent INTEGER,
		building_id INTEGER,
		FOREIGN KEY(building_id) REFERENCES buildings(id)
	);
''')

db.commit()
db.close()
```

SEED FILE

```
import sqlite3

db = 'livingdb'

BUILDINGS =[
    ["Empire State", "New York", 1930],
    ["Bradbury", "Los Angeles", 1893],
    ["White House", "Washington D.C.", 1800],
]

RESIDENTS = [
    ["Jay", "Z", 100000, 1],
    ["Kobe", "Bryant", 90000, 2],
    ["Barack", "Obama", 50000, 3],
]
conn = sqlite3.connect(db)
c = conn.cursor()

print("Destroying old data")
c.execute("DELETE FROM buildings")
c.execute("DELETE FROM residents")

for building in BUILDINGS:
    c.execute("""
        INSERT INTO buildings ("name", "city", "build_year") VALUES (?, ?, ?)""",(building[0], building[1], building[2]))

conn.commit()

for resident in RESIDENTS:
    c.execute("""
        INSERT INTO residents ("first_name", "last_name", "rent", "building_id") VALUES (?, ?, ?, ?)""",(resident[0], resident[1], resident[2], resident[3]))

conn.commit()

c.close()
```

##### Part 3 - JOIN and INNER JOIN

* Now let's take the data from the two tables and order their results the way we want them.
* A Join can be performed whenever we have a relation between two tables.
* A Join allows us to query two tables and return a combined value/values
* Lets open our new database using sqlite3 in the terminal and go through an example of the `JOIN` syntax below:

```
SELECT residents.first_name, buildings.name
FROM residents
JOIN buildings
ON residents.building_id=buildings.id;
```
* INNER JOIN is the most commonly used join.
* There are others but for the purposes of this course we will not be exploring them

![](http://www.securesolutions.no/wp-content/uploads/2014/07/joins-1.jpg)

##### Part 4 - Querying a parent/child foreign key

* Let's say we want to find all the residents of the 'Empire State' building. Here's how we can 'follow' the foreign key relationship from parent to child:

```
SELECT residents.first_name, residents.last_name, buildings.name
FROM residents, buildings
WHERE residents.building_id=buildings.id AND buildings.name='Empire State';
```

##### Part 5 - Inheritance Hint

* For your `bank_software` exercise you might have to use `inheritance`. 
* Take a look at our notes from week one and week two if you need a review
* Also check out this blog for a better understanding [Jesshamrick introduction to classes and inheritance in python](http://www.jesshamrick.com/2011/05/18/an-introduction-to-classes-and-inheritance-in-python/).


#### Resources

[SQL Quick Reference](http://www.w3schools.com/sql/sql_quickref.asp)
[SQL Inner Join Reference](http://www.w3schools.com/sql/sql_join_inner.asp)
[Blog about Inheritance](http://www.jesshamrick.com/2011/05/18/an-introduction-to-classes-and-inheritance-in-python/)
