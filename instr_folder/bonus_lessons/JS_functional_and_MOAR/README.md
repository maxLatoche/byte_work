# Functional JavaScript AND MOAR!!!

### Learning Objectives

***Students Will Be Able To...***

* Utilize the following methods
	* .reduce()
	* .map()
	* .filter()
* Utilize .sort

---
### Context

* Learn a new way to do some bad ass programming

---

### Lesson

#### Part 0 - Imperative vs. Declarative Programming!!!

* You will find many articles trying to explain Imperative vs. Declarative programming
* Many of them will say "Imperative is How and Declarative is What"
* All of them will give silly examples like:
	* Imperative is going to a wedding and the hostess tells you to walk forward ten paces, make a left, walk five paces, make a right, and thats your table. 
	* Declarative - You're at table 8.
* In terms of programming, imperative is writing your code in such a way you are telling the computer HOW to do something. 
* For example, writing a for loop that will multiply everything in an array by two

```
var nums = [1,2,3,4,5]

for (var i = 0; i<x.length; i++){
	console.log(nums[i]*2)
}
```
* In a declarative manner we will tell our code WHAT we want done.

```
nums.map(function(number){
	return number*2
})
```
* In the second code we are using the built in `.map` function to give us back an array with all values multiplied by 2

#### Part 1 - Functional Programming

* We want to write code with zero side effects
* This means our functions should return brand new objects, never mutating the original data
* This is also known as writing a "Pure Function"
* Three main methods of JavaScript that do this are `.map()`, `.filter()`, and `.reduce()`
* `.sort()` is added in here because it is a handy function that you should learn but it is NOT A PURE FUNCTION

***NOTE***

* Frameworks and Libraries such as Angular and React encourage programmers to write code in a functional way and a declarative way. 

#### Part 2 - `.map()`

* `.map()` is similar to a `forEach()` function
* It will apply a callback to each value inside of the array
* map will then return an array
* Notes
	* The amount of input elements will be equal to the amount of output elements
	* Your callback inside of map should not mutate the original data structure
	* Your map callback should not change the state outside of the function
* **Example:** - Lets take an array of numbers and double each value using `.map()`

```
var nums = [1,2,3,4,5];

var double = nums.map(function(num){
	return num*2
})

console.log(nums); 		// [1,2,3,4,5]
console.log(double); 	// [2,4,6,8,10]
```

#### Part 3 - `.filter()`

* `.filter()` will return a new array of all the values that pass the test of the callback
* Example: Get an array that will return only the even numbers

```
var nums = [12,234,43,31,62,7,2,3,8,5,4];

var even = nums.filter(function(num){
	return num%2 === 0
})

console.log(nums) 	// [ 12, 234, 43, 31, 62, 7, 2, 3, 8, 5, 4 ]
console.log(even) 	// [ 12, 234, 62, 2, 8, 4 ]
```

#### Part 4 - `.reduce()`

* `.reduce()` can be used to combine the values in an array
* It will take two arguments, the first is a callback, the second is the "starting value"
* For each item in the array, the callback will be invoked and you can add it to the "total value" or "starting value"
* You will return a new "total value" 

```
var nums = [12,234,43,31,62,7,2,3,8,5,4];

var sum = nums.reduce(function(total, num){
	return total + num
}, 0)

console.log(sum)	// 411
```

***Five Minute Exercise***

* What if we wanted to sum up a value inside an array of objects
* Take the object below and sum the pages

```
var books = [
	{title: "Enders Game", pages: 352},
	{title: "Harry Potter 1", pages: 482},
	{title: "Where's Waldo", pages: 132},
	{title: "Game of Thrones", pages: 870},
	{title: "Warhammer 40k", pages: 602},
]
```

#### Part 5 - `.sort()` (NOT A PURE FUNCTION)

* `.sort()` will sort an array IN PLACE!!! 
* This is NOT a pure function 
* SORT WILL MUTATE THE ORIGINAL DATA STRUCTURE
* I am throwing this in this lecture because it is extremely handy

```
var x = [3,5,1,6,2,7]

var y = x.sort()

y === [1,2,3,5,6,7]
x === [1,2,3,5,6,7]
```
* Lets say we want to choose how to sort our array, ascending or descending
* Ascending order: The sort function will return 1 if the first argument is greater than the second
* Descdening order: The sort function will return -1 if the first argument is less than the second

```
var x = [3,5,1,6,2,7]

x.sort(function(a,b){
	if (a > b){
		return 1
	}
	if (b > a){
		return -1
	}
	return 0
})
```
***Five Minute Exercise***

* What if we were assessing an array of objects?
* Take the object below and sort it by pages

```
var books = [
	{title: "Enders Game", pages: 352},
	{title: "Harry Potter 1", pages: 482},
	{title: "Where's Waldo", pages: 132},
	{title: "Game of Thrones", pages: 870},
	{title: "Warhammer 40k", pages: 602},
]
```