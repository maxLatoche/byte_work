Customer Signup
===============

* You've been hired by Time Warner Cable to fix their internal tools- maybe now they can finally focus on delivering us reliable internet! Godspeed son, we're all depending on you.
* Your task is to build a terminal app that allows their customers to sign up for service. Once logged in they should be able to create and update their personal information.

###Requirements

* A user should be able to create an account, with only a username and password.
* After they sign up and log in, they should be able to add / update their personal information. A user should have a:
	* first and last name
	* date of birth
	* many phone numbers
	* many addresses

###Recommendations

* Use sqlite3 and save all the information to a sqlite3 file. You are to write SQL for this challenge. 
	* If you completed the BabyORM assignment you `CANNOT` use it for this assessment. You must write your SQL code from scratch and keep them inside functions/methods.
* Make a create file and seed file that will populate your database with Dummy data for you to test the user functionality.
* There should never be any null columns in your database.
* Build this app using the MVC pattern.

### PLAN PLAN PLAN!

* `Draw out your ERDs` - You should plan out your tables and your databases. Think about the requirements and how many tables you will need. How about foreign keys.
* `Start Small` - Have the finished product in your head but start small! 
* `Test Everything` - Remember do not write a million functions at once. Write one function, test it by printing out your data/result to make sure it works, then move on to the next function 

### BONUS

* Add a user in your database with "admin" privileges 
* An admin is just a user but with some extra privleges. An admin can update anybody's information, including their own. 
* It is recommended that you build out all of the user functionality first. 
	* Add admin functionality afterwards. 
	* If your code is extensible, modular and properly object oriented, this should be very easy.

