# Master List Of Questions For Monday Tech Talks

---

### Instructions

* If you are a TA managing this README please make sure to keep it updated every week with the new questions. 
* These questions are meant to cover programming topics that may or may not be in the Byte curriculum, but also serve as possible interview questions. 
* Every student will be given a question on Friday and they will have to present on that topic for five minutes on Monday morning.
* Please make sure to update the corresponding ***weekly_cs README*** for `EACH COHORT STUDENT REPOSITORY`
* All TA's are expected to coordinate with each other as to who will be updating each cohort repository, and who will be distributing the questions. 

---

### Questions

## Python

* Choose five of the built in functions from the list below. Explain what the function does, provide at least one example of the use of the function.

```
zip
type
sorted (bonus question: what is the difference between sort and sorted?) 
slice
setattr and getattr
ord
char
set
map
iter
```
* What is a function? What is a method? What is the difference (if any) between a function and a method?
* What is an expression? What is a statement? What is the difference (if any) between the two?
* What is scope? Why is it important? How does python inheritance work?
* Is python a static or dynamic language? Weakly or strongly typed? Why is this important. What are the benefits of a static language?
* What is a class? What is an object? What is the difference between a class and an object?
* What are modules? Provide an example.
* What happens when you call ```__init__```?
* What is self? Why do all classes and methods need self?
* What is if __name__ == "__main__"?' What is it's purpose?
* What are instant methods and class methods? How are instant and class methods used and how are they different from one another?
* Lamdba - What is lambda? What does it do and why do we use it?
* Boolean Mask - What is it? Where is it used? What is it good for? 
* Magic Methods - What is it? How are they used in Python? Give some examples.
* Garbage Collector - What is the utility of pythons garbage collector? How does it work? What is a reference cycle? What does the Python garbage collector do to these?
* Threading - What is multi threading? Why do we use it? Is python multi threaded or single threaded?
* Hash Table - What is a hash table? What are the pros and cons? Why would we use a hash table over an list/array?
* Cython - What is Cython? What do people use Cython for? Why is numpy so fast? What are major differences between C and Python? In terms of software development what is a JIT compiler? What are the advantages and disadvantages and how can we use the concept in python?
* Monkey Patching - What is Monkey patching? When would we use it?
* Is Python called-by-value or call-by-reference? (Also known as pass by value vs pass by reference) Explain.
* How do you avoid cyclical imports in Python? How can you do this without using imports in functions?
* Explain the DataFrame memory usage in Pandas. Provide an example
* How do you handle data that was created on a machine with a different byte order than the one you're using to run Python? Provide an example
* How do you iterate over rows in a DataFrame in Pandas? Provide at least two ways to solve the question.
* How do you filter the DataFrame row of pandas if you're looking for exact matches? How do you filter if you have partial matches or substrings you're looking for?
* What is GIL? Why/How is it used?
* virtual environment
    * What is this
    * What is it good for
    * How do we use it
* What are the functions "help()" and "dir()" for
    * how do we use it

## CSS 

* Floats - What is it? How do you clear floats and what are the problems with floats?
* Explain CSS Specificity? Does the way we apply our CSS matter? How do ID's and Classes fit in this topic?
* Explain the different CSS Positions. What are they? How do they interact with each other
* What are CSS Grids? How can we us them? 
* What is Flexbox? When did it come out? How is this used?

## JavaScript

* What kind of inheritance does Javascript use? 
* What is a callback? What is a closure? 
* What is hoisting?
* What is 'this' in javascript?
* Explain the javascript event loop.
* What is event delegation? What is event bubbling?
* What are JavaScript Promises?
* What are the main JavaScript Design Patters?
* How do we use Prototypal inheritance? Provide Examples.
* What is Universal / Isomorphic JavaScript? 
* What is the virtual DOM?
* Is JavaScript single threaded or multi threaded? What does that mean? 
* What is the history of JavaScript?

## HTML / CSS

* What are semantic HTML elements? How are they related to Tim Berners-Lee's vision of a "semantic web?"
* How did the "Beijing doctrine" accelerate the standardization of-- what are now referred to as-- CSS modules? What can we learn, as full-stack developers, from the CSS Working Group's decision to progress from the monolithic specification, which is expressed in CSS2.1, to the modular nature of "CSS3?"
* What is a "flash of unstyled content?" Describe the way a website is rendered by a browser engine.
* What is SASS? How do we use it? What is it good for? Examples?

## Databases 

* What are the differences between a relational database and a non relational database? Why would we use one over the other? What is an ORM what is an ODM?
* List and explain the different types of JOIN clauses in SQL (inner, left, right, full)
* Assuming that there are at least 10 records in the employee table, write and explain a SQL query to find the 10th highest employee salary from an Employee table. 
* What does UNION do? What is the difference between UNION and UNION ALL? Bonus: Write a SQL query using UNION ALL (not UNION) that uses the WHERE clause to eliminate duplicates. 
* What is the major difference between Truncate and Delete in SQL?When do we use truncate? When do we use delete?
* What is normalization? What is denormalization? Bonus: What are the different normalization forms?

## Web 

* HTTP - What are HTTP Status Codes? Give examples of some of each 100, 200, 300, 400, and 500 status codes
* IP / TCP / HTTP are they connected, how do they work?
* HTTP2 - What's new between HTTP2 vs HTTP

## Django/Flask 

* How does middlwares work in Django? Provide an example and explanation 
* What's the difference between select_related and prefetch_related in Django? When do we use one over the other? 
* What is a Thread-Local object in Flask? Provide an example
* What is Flask Sijax? How do you use it? 

## Servers

* Requests - What are request methods? Give some examples
* Load Balancing - What is load balancing? Why is it important?
* What is the difference between UDP and TCP? Why do we use one over the other?
* SSH - What is SSH? How does it work? 

## Algorithms and Problem Solving

* Big O - What is Big O notation and why is it important?

*Johnson Algorithm (a two-part question intended for two students):*

* Bellman-Ford: Write the algorithm in Python3 (hereafter: your solution) and prepare an explanation, of Bellman-Ford, that includes answers to the following questions:
* Who was Richard Bellman? Who was Lester Ford? Who was Edward Moore?
* What could an animated illustration of the Bellman-Ford algorithm look like? Be prepared to illustrate (vis. rep.) your solution on a whiteboard without an aide.
* When was the algorithm published?
* Where did Richard Bellman work? Where did Lester Ford work? Where did Edward Moore work? Where were they born? What secondary schools did they attend? What universities did they attend?
* Why is this algorithm important? What is its relationship to the Johnson algorithm?
* Dijkstra: Write the algorithm in Python3 (hereafter: your solution) and prepare an explanation, of Dijkstra, that includes answers to the following questions:
* Who was Edsger Dijkstra?
* What could an animated illustration of the Dijkstra algorithm look like? Be prepared to illustrate (vis. rep.) your solution on a whiteboard without an aide.
* When was the algorithm published?
* Where did Edsger Dijkstra work? Where was he born? What secondary school did he attend? Where university did he attend?
* Why is this algorithm important? What is its relationship to the Johnson algorithm?
* Stack - Explain and provide an example of the average case and worst case time complexity for insertion and deletion in a stack 
* Queue - Explain and provide an example of the average case and worst case time complexity for insertion and deletion in a queue
* Hash Table - Explain and provide an example of the average case and worst case time complexity for insertion and deletion in a hash table
* Quick Sort - Explain and provide an example of quick sort. What is the best and worst case time complexity of quick sort? 
* Merge Sort - Explain and provide an example of merge sort. What is the best and worst case time complexity of merge sort?
* Bubble Sort - Explain and provide an example of bubble sort. What is the best and worst case time complexity of bubble sort?
* Insertion Sort - Explain and provide an example of insertion sort. What is the best and worst case time complexity of insertion sort?
* Heap Sort - Explain and provide an example of heap sort. What is the best and worst case time complexity of heap sort?
* Write a function that uses memoization to save calculation time for a recursive fibonacci function.
* Write a function that will take in a number and print out 0 to that number but print every new value out in 3 second intervals. Explain both your function and the reasoning you used to solve the question.
* What is the output of the following code in JS? Explain why.
``` 
var y = 1;
  if (function f(){}) {
    y += typeof f;
  }
  console.log(y);
```
* What is the output of the following code in JS? Explain why.
```
var trees = ["xyz","xxxx","test","ryan","apple"];
delete trees[3];
console.log(trees.length);
```
* Write a `blah` function that will return the following outputs:
```
console.log(blah(2)(3)(4)); // output : 24 
console.log(blah(4)(3)(4)); // output : 48
```
* Show and explain at least *3* ways to empty the following array:
``` 
var arrayList =  ['a','b','c','d','e','f'];
```


## Unix 

* Bash - What is bash? 
* What’s the difference between bash, .bashrc and .bash_profile? 
	* What are environmental variables
	* Can we use these to store API keys
	* If we can how can we access those keys
	* What else can we do with our Bash_profile
* Explain the use of “#!/bin/bash”. Where is this used? Why is it used? 
* Curl - What is curl? What is the difference between curl and Wget?
* Explain the following commands:

```
    * cat (what happens when cat commands are combined with redirection (> or >>))
    * tac
    * rev
    * chmod/chattr
    * man/info
    * chown
```

## Misc

* What are the advantages and disadvantages of using a MVC model?
* What is docker? What is a virtual machine? Why do people use docker over virtual machines like VMware?
* Open Source Licensing - What are some different types of open source licensing? Give some examples.
* Pass by Value vs Pass by Reference - What does it mean when a language is pass by value vs pass by reference? Which is Python, which is javascript?
* OOP - What is Object Oriented Programming? What is Functional Programming? Why would you use one over the other?
* Bit manipulation - What is it? How does it work?
* How do game consoles, like the playstation or xbox, differ from conventional computers like laptops or desktops?
* How do single-board computers, like the raspberry pi, differ from conventional computers like laptops or desktops?
* What is homebrew? How is homebrew implemented? List some other examples of package managers
* Provide an overview of the steps for setting up a portfolio page on digital ocean.
* What’s the difference between progressive enhancement and graceful degradation?
* CDNS
    * what are they
    * how do we use it
