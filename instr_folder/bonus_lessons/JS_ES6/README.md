# JavaScript ES6

### Learning Objectives

***Students Will Be Able To...***

* Utilize const 
* Utilize let
* Utilize the spread operator

---
### Context

* Learn a new way to do some bad ass programming

---

### Lesson

#### Part 1 - Var / Hoisting / Declaration Review

***Hoisting***

* As we already know `var` is the keyword we use in JavaScript when declaring a variable. 
* When we declare a variable with `var`, that variable exists in the `function scope`
* Check out the below code in the `main.js` file. You may recognize from our `hoisting` example

```
var myFunc = function(){
	var a = 10;
	
	if (a === 100){
		var b = 20;
	}
	console.log(a)
	console.log(b)
}
myFunc()
```
* Woah how come it didn't give us an error? We never get to b.
* We mentioned `function scope` earlier. This is `hoisting`
* The `variable declaration` gets `hoisted` to the top of it's function scope
* But since we never get to the inside of the if statement, the variable never gets it's value assigned to it. 
* When the console.log is hit, it will be undefined

```
var myFunc = function(){
	var a = 10;
	var b;
	
	if (a === 100){
		var b = 20;
	}
	console.log(a)
	console.log(b)
}
myFunc()
```
***Declaration Part 1***

* Let's talk about another aspect of `var`
* What happens when we don't use `var` to declare our variables? 
* JavaScript will continue to loop through the local scope, enclosing scopes, and eventually global scope for that variable
* If it does not find what it's looking for it will create that variable in the global scope
* Let's expand the example above a little further

```
var myFunc = function(){
	var a = 10;
	
	if (a === 100){
		var b = 20;
	}
	c = 30;

	console.log(a)
	console.log(b)
}

myFunc();
console.log(c);
```
* Do not try to declare a variable without using `var` or `let` or `const`
* We do not want to pollute our global name space.

***Declaration Part 2***

* What happens if we try to declare a variable that already exists? 

```
var myFunc = function(){
	var a = 10;
	var a = 30;
	
	console.log(a)
}
```
* We now get 30
* This can be a problem if we have a large code base and are not organizing our variables well. 

#### Part 2 - let and const

***Differences between `var` vs `let and const`***

* `let` and `const` are ES6 keywords that allow us to declare variables in `block level scope`
* `block level scope` means the variables are staying in the scope of their code block
* variables declared with `let` and `const` are still `hoisted` but to the `block level`, NOT THE `function scope`
* Lets take the example above and use `const` and `let`

```
const myFunc = function(){
	let a = 10;
	
	if (a === 100){
		let b = 20;
	}
	console.log(a)
	console.log(b)
}
myFunc();
```
* Now we get a `ReferenceError: b is not defined`
* Another thing we get with ES6 `let` and `const` is protection from redeclaring an existing variable

```
let a = 10;
let a = 20;

console.log(a)
```
* We will get a `SyntaxError: Identifier 'a' has already been declared`
* We will get the same error with `const` as well

```
const a = 10;
const a = 20;

console.log(a)
```

***Five Minute Exercise***

* What will this code return?

```
let name = "Peter Parker";
let crime = true;

if (crime){
	let name = "Spider-man"
}
console.log(name);
```

* It will return "Peter Parker"
* We have two variables called `name` both in different scopes
* Remember `let` keeps our variable in the `block level scope` so when we call `let name = "Spider-man"` that is a variable inside the block scope of the if statement
* To get Spiderman we can `reassign` the value of the let name variable

```
let name = "Peter Parker";
let crime = true;

if (crime){
	name = "Spider-man"
}
console.log(name);
```

***Differences between `let` vs `const`***

* The difference between `let` and `const` comes down to their ability to be reassigned
* `const` declaration CANNOT be reassigned

```
const movie = {
	title: "Top Gun",
	year: 1986
}

movie = {
	name:"Jason",
	vision: "20/20"
}
```
* We get a `TypeError: Assignment to a constant variable`
* This does not mean the values cannot get reassigned

```
const movie = {
	title: "Top Gun",
	year: 1986
}

movie.title = "Kill Bill",
movie.year = 2003

console.log(movie)
```
* A variable declared with `let` can be reassigned
* You may choose to use `let` inside of a for loop if you are constantly reassigning the variable

```
const movies = [
	"The Man From Nowhere",
	"The Usual Suspects",
	"District 9",
	"John Wick",
	"The Raid",
	"Good Will Hunting"
]

for (let i = 0; i<movies.length; ++i){
	let temp = movies[i];
	console.log(temp);
}
```

#### Part 3 - JS String Templating

* With ES6 JavaScript now has STRING TEMPLATING!!!
* In Python we were able to accomplish this with the `%s` or the `{}` inside of a string and pass in values
* JavaScript now has that functionality as well
* Instead of using quotes, wrap your string in `backticks`
* Then write the variable you will enter into the string with `${}`

```
var name = "Jason"

console.log(`Hello ${name}`)
```

#### Part 4 - Arrow Functions

* Arrow functions allow us to write JavaScript functions that will not bind it's own `this` argument. 
* Arrow functions are always Anonymous
* When having nested functions you can might use the `.bind(this)` to ensure that the inner function's `this` argument has the same value as it's outer function.
* With Arrow functions, the inner function will not apply it's own value to the `this` argument, and therefore we do not need to bind anything

```
var x = document.querySelector('#clicker');


console.log(x)

// this will return the `ul` with an id of `clicker`
// x.addEventListener('click', function(event){
// 	console.log(this)
// })

// this will return the encompassing Window object
x.addEventListener('click', (event)=>{
	console.log(this)
})
```


#### Part 5 - Destructuring an Object

```
const favThings = {
	movies : ["John Wick", "The Usual Suspects", "The Raid", "Good Will Hunting"],
	tvShows : ["Scrubs", "True Detective", "Game of Thrones", "The Black Donnellys"],
	footballTeam : "New Orleans Saints",
	ufcFighter : "George St. Pierre"
}

const breakItDown = (obj) =>{
	const {movies, tvShows, footballTeam, ufcFighter} = obj;

	console.log(movies);
	console.log(tvShows);
	console.log(footballTeam);
	console.log(ufcFighter);
}

breakItDown(favThings);
```
