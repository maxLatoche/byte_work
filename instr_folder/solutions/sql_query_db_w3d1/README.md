## QUERY PRACTICE

##### Description

* Practice makes perfect
* You have been given a database file in this repo called `sitemetrics.db`
* All the work for this exercise will be done in the terminal. That's right, we're taking a break from python files. 

##### Objective

* Open the database file using the sqlite3 command in your terminal. 
* Answer the following questions in this markdown and push your answers to your OWN GITHUB BRANCH

-------------
##### How many people are from California?  
SELECT COUNT(*) FROM users WHERE state = "CA";
14
##### Who has the most page views? How many do they have, and where are they from?
SELECT name,city,state,MAX(page_views) FROM users;
Edison Mcintyre|Mauriceville|ME|19937

##### Who has the least page views? How many do they have and where are they from?
SELECT name,city,state,Min(page_views) FROM users;
Hattie Ross|Hubbard|MA|16

##### Who are the most recent visitors to the site?(at least 3)
SELECT name  FROM users ORDER BY last_visit LIMIT 3;
Woodrow Duffy
Jake Monroe
Ofelia Crabtree

##### Who was the first visitor?
SELECT name  FROM users ORDER BY last_visit;
Woodrow Duffy

##### Who has an email address with the domain 'horse.edu'?
SELECT name FROM users WHERE email like '%horse.edu';
Fern Byers
Valentine Gonzales

##### How many people are from the city Graford?
SELECT COUNT(*) FROM users WHERE city = 'Graford';
3

##### What are the names of all the cities that start with the letter V, in alphabetical order?
SELECT DISTINCT city FROM users WHERE city like "V%" ORDER BY city;
Valley View
Van
Vega
Victoria

##### What are the names and home cities for people searched for the word "drain"?
SELECT DISTINCT name,city FROM users,user_searches,search_terms WHERE users.id = user_searches.user_id AND user_searches.term_id = 201;
Nelly Beach|Graford
Penelope Stein|Runaway Bay
Tisha Gill|Bausell and Ellis
Rolando Crowley|Buda

##### How many times was "trousers" a search term?
SELECT COUNT(*) FROM user_searches,search_terms WHERE user_searches.term_id = 496 AND search_terms.word = "trousers";
2

##### What were the search terms used by visitors who last visited on August 22 2014?
SELECT DISTINCT word FROM search_terms, users WHERE users.last_visit = "2014-08-22";

##### What was the most frequently used search term by people from Idaho?
SELECT word, COUNT(word) as counter FROM search_terms,users,user_searches WHERE users.state = 'ID' AND user_searches.term_id = search_terms.id ORDER BY counter DESC;
collar

##### What is the name of user 391, and what are his search terms?
SELECT DISTINCT name,word FROM users,user_searches,search_terms WHERE users.id = 391;