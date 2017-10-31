# Advanced Python Techniques

### Learning Objectives
***Students Will be Able To***

* Use List Comprehensions with a imported csv file
* Use Python Generators to look through a iterable
* Use Kwargs as a Python parameter to print out unknown amount of arguments
* Use Ternary Operators in place of if/else

---
### Context

* We're going to get into some deeper Python understanding. This will help you code  the upcoming assignments

---
### Lesson

##### Part 1 - Ternary Operator

* A ternary operator is a single line if else statement. 
* Because it is one line we try to keep this very simple with only two expresssions and a condition to run on true and a condition to run on false
* In JavaScript this looks like 

```
condition ? expression1 : expression2
```
* In Python 

```
expression1 if condition else expression2
```

***Five Min Exercise***

* Take a few minutes to google some examples if you need to
* Write a ternary operator to 
	* print "I Like Turtles" if a variable "turtle" was set to True
	* print "Standing is good for you" if a variable "healthy" is yes

##### Part 2 - List Comprehensions

* Python comes with the ability to give us a list with one line of code
* List Comprehensions allow us to build a list of values by filtering through an iterable. 
	* We know that iterables are any data types / data structures that can be looped through. (strings, lists, tuples, and the like)
* The syntax for a list comprehension will look like this:

```
[ expression for item in list if conditional ]
```
* The expression is what you want to do to each item
* The for loop is... the for loop
* The conditional is an optional parameter. 
* Let's print out a list of all the numbers from 1 to 20

```
num_list = [num for num in range(20)]

// [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
```

***Five Min Exercise***

* Write a method that will take in a string as an argument
* Use a list comprehension that will return a list with all the values being vowels
* Print out the number of vowels from the string that was inputed

***Answer***

```
def vowels(str):
  vowels = "aeiou"
  return [char for char in str if char in vowels]
```


##### Part 3 - Generators - Controllers - Class Methods

***Five Min Exercise*** 

* Write out a method that will take in the number, and prints out all the numbers starting at 1, up to the number, multiplied by two.
* Now explain every step from invoking that method to seeing the results of that method

```
def double(x):
	pass
	
double(10)
```

---

* What happens if we want to do a very large number? 100? 1000? 100000000? 
* It would take a much longer time to run right? 
* Here's where we start using Generators
* Usually when we use functions we don't play around with the output until it is finished running. 
* Think about the previous exercise. We appended them all in a list and then doubled them through a loop. This takes an immense amount of memory, especially if we use larger numbers.
* Generators allow us to define and utlize a function that can suspend itself, send back a value for us to manipulate, and then resume where it left off

```
def double(x):
	for num in range(x):
		yield num*2
		
for blah in double(10):
	print(blah)
```

* When we invoke a function with a `yield` statement inside we are receiving a `generator object` 
* This generator object does not hold any values in memory, it is used to define how the program will navigate through the generator
* Now we can use the methods `next()` and `iter()`

***Five Min Exercise***

* use the random library
* print out a random number from two given inputs

```
import random

def rand_num(a,b):
	pass
	
rand_num(34, 98)
```

##### Part 4 - Args and Kwargs

* Python Args and Kwargs allow us to pass in an undefined/unknown number of arguments in a method/function
	* Remember when the function is created we can set "parameters" to it
	* When the function is invoked we pass in "arguments"

***Args***

* Args are used to send in a non-keyword variable length argument list to a function
* What does this mean in English? 
* We can use this operation with the syntax `*arg`
	* `arg` can be anything this is just a placeholder
	* We could easily say `*names`

```
def people(*arg):
	for element in arg:
		print(element)
		
people("Ice Cube", "Easy-E", "Dr. Dre", "MC Ren")

// "Ice Cube"
// "Easy-E"
// "Dr. Dre"
// "MC Ren"
```

***Kwargs***

* Kwargs stand for Keyword Arguments. They act almost the same as Args
* If you had a named argument with a key, you can use kwargs
* They are some funky Python syntax. I have not seen kwargs used in another language other than Python. Nonetheless it can be very useful in some use cases. 
* `**kwargs` allow us to pass in an unknown amount of arguments to a method as long as they are key:value pairs. Hence why we call them "keyword arguments" 

```
names = {"first_name":"Volder", "last_name": "Mort"}

def hello(**kwargs):
	if len(kwargs) > 0:
		for key,value in kwargs.items():
			print("Your {x} is {y}".format(x = key, y = value))

hello(**names)
```

* Also, checkout .keys(), .values(), and .items() methods for dictionaries if you haven't seen them yet!

***Five Min Exercise***

* Create a dictionary for character stats like your RPG game
* Now use a method that takes in kwargs to print out those stats to the terminal

##### Resources

* [Python Tips Args and Kwargs](http://pythontips.com/2013/08/04/args-and-kwargs-in-python-explained/)
* [Python Wiki Generators](https://wiki.python.org/moin/Generators)