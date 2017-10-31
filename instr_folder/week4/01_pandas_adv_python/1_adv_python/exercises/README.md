# Advanced Python

##### Description

* There are multiple prompts in this README. 
* The goal of each prompt is to push you to practice some of the new Python tools we've learned today: generators, list comprehensions, kwargs, and ternary operators.
 
***NOTE***

* Don't forget you have access to Pythons built in methods. (`sort`, `reverse`, and the like)


##### Objective 1 - Evens

* Take an integer as an argument
* Return a list where all values are the even numbers up until the argument

##### Objective 2 - Vowels

* Take a string as an argument
* Use list comprehension to see if the string is a palindrome
* Palindrome is a word or phrase that is the same forward as it is backwards

##### Objective 3 - Reverse

* Take a string as an argument
* Return a list where all the values are the characters of the string in reverse

##### Objective 4 - Fibonacci

* Lets do fibonacci using Generators
* If you need a refresher the Fibonacci sequence is a sequence that starts with 0, and 1, and every following number is the sum of the previous two.

```
0,1,1,2,3,5,8,13,21
```
* Lets write a method that takes in a number as an argument and prints out all the numbers in the fibonacci sequece up to the input, USING GENERATORS

##### Objective 5 - FizzBuzz

* Lets do fizzbuzz using Generators
* If you need a refresher FizzBuzz is a programming exercise where if a number is:
    * Divisible by 3 print Fizz
    * Divisible by 5 print Buzz
    * Divisible by both 3 and 5 print FizzBuzz
    * Not divisible by 3 or 5 print the number itself

```
1,2,Fizz,4,Buzz,Fizz,7,8,Fizz,Buzz
```
* Write a method that will take in a number as an argument and print out all the numbers/fizzbuzz/ in that sequence, USING GENERATORS

##### Objective 6 - Random

* use the random library
* print out a random number from two given inputs
* Use A Generator

```
import random

def rand_num(a,b):
    pass
    
rand_num(34, 98)
```

##### Objective 7 - BONUS 

* Use the timeit module
* Write a function that will take in a number and print out all numbers from zero to input (Use Lists)
* Now do the same thing but with a Generator
* Time both functions and log the speed difference
