# Jason Ng's Phase 1 Review

* Build a Pokemon Team Building Application using the pokemon api here. [http://pokeapi.co/](http://pokeapi.co/)
* Users should be able to create an account
* Users should be able to log into their account
* Users should be able to search for pokemon
* Users should be able to save a pokemon on their team
* Users should be able to see the pokemon they saved

##### Objective 0

* Plan your table using the [schema designer](http://ondras.zarovi.cz/sql/demo/)
* Draw out your MVC design pattern
* Make sure to read the docs and test the endpoints in the browser before continuing

##### Objective 1

* Create and Seed
* You should have two tables. A User table and a Pokemon table
* The Pokemon table can have a foreign key to relate that row to the users table

***NOTE***

* If you REALLY wanted to expand on this, how would you go about handling this many to many relationship better?
	* Many users can have many pokemon
	* Many pokemon can be a part of many Users teams
* Maybe a third separate relational table? This can be a luxury goal for later

##### Objective 2

* Build out a login system in the terminal application with the MVC Design Pattern
* We've done this before. What do we have to save to our Users table? 
* Can a user create an account?
* Can a user logs into an account?

***NOTE***

* When a user is authenticated what kind of information should we keep inside our controller. We're planning for the saving of a favorite pokemon. For that we'll have to stick something in the Foreign Key column of the Pokemon table

##### Objective 3

* Now that we have users logged in properly how can we allow them to search for pokemon? 
* Does this API allow us to search by id, name, ability, type, attack, etc. 

##### Objective 4

* If a user has selected a specific pokemon they should have the option to save that pokemon to their team

##### Objective 5

* A user should be able to see their own pokemon team

***NOTE***

* Take it a step further. A person can only have five pokemon on their team at a time. But they can collect more than five. 
* How can we allow them to move a users pokemon between their "team" and their "collection"


---


# Jeff Maxims Phase 1 review

#####Things you CAN do to review

 1. Participate in our class Jeopardy! [https://docs.google.com/presentation/d/1UGnrd8FM9U7kOlJnzgJMTSlVmIsE1jXLdexvOdSH_3s/edit?usp=sharing](https://docs.google.com/presentation/d/1UGnrd8FM9U7kOlJnzgJMTSlVmIsE1jXLdexvOdSH_3s/edit?usp=sharing)
 2. Look in the parking lot
     3. You'll see the syllabus here. Use the syllabus to review the exercises we've done and the concepts we've covered. Think about which exercises you need to review and which concepts you need more practice with.
     4. Practice vocabulary terms that you've learned the last month
     5. Make some small apps and test codes. Test them. Maybe use pudb or pdb.
