# What is THIS?!?!?!

### Learning Objectives
***Students will be able to...***

* How to use This

---
### Context

* Using `this` is an essential JS function that will make cleaner more organized code

---
### Lesson

##### Part 1 - This Intro

* `This` is a javascript statement which will reference the value of a single object  at a specific moment in time
* Not only does it reference the object but it will have the value of the object
* In the global scope `this` will refer to the window object
    * open the inspector and type this
    * We don't usually use `this` in the global space, but more for functions
* The value of `this` will be the value of the object that invokes the function where `this` is located

***Five Min Exercise***

* Make a html file and a main js file. 
* Hook up the main.js file and [jQuery](https://cdnjs.com/libraries/jquery/2.2.0)
* Inside your html file make the boilerplate template and create a button in the body that says "CLICK ME"
* Inside your JS file use document.ready
* Now use jquery to target the button and on click console.log `$(this)`
* What do you get?
    
##### Part 2 - More of This!

* this does NOT have a value until something invokes the function where it is defined. 
* Do not get it mixed up. `this` does not reference the function/object where it is defined. It will get it's value from the object that invokes it. 

```
var myThis = function(x){
        console.log(this)
}

$("button").on("click", myThis)
```

##### Part 3 - Bind / Call / Apply

* In the above example, we see that depending on where `this` is, and when it is being called we know it can pass objects into a function where we expect it to be something else. 
* Noticed what we did in the above example was a `named callback`
* What if we DID want to reference something inside of the callback function, and NOT the object value that invoked it
    * e.g. the myThis function instead of the button object
* That's where Bind / Call / Apply come in. I know what you're saying. "What the hell, these are methods, how are we going to use this on functions"
* Remember JS functions are just objects, and as we already know objects can have methods. Bind / Call / Apply are methods for our JS functions
* You will need to `bind` the value to to the object value you want so `this` will not target the invoking object. 

***Open Up Example called mainBind.js***

* Check out the other two methods when you get a chance by reading [JavaScript is Sexy Bind / Apply / Call Entry](http://javascriptissexy.com/javascript-apply-call-and-bind-methods-are-essential-for-javascript-professionals/)


#### Extra stuff

* Implicit Binding - When the function with `this` inside of it is invoked look to the left of the period 

```
var turtle = {
	name: "Raph",
	color: "Red",
	sayColor: function(){
		console.log(this.color)
	}
}
turtle.sayColor(); // "Red"
```
* That example wasn't dynamic enough? 

```
var sayColorMixin = function(turtle){
	turtle.sayColor = function(){
		console.log(this.color)
	}
}

var raph = {
	name: "Raph",
	color: "Red"
}

var leo = {
	name: "Leo",
	color: "Blue"
}

var mickey = {
	name: "Mickey",
	color: "Orange"
}

var donny = {
	name: "Donny",
	color: "Purple"
}

sayColorMixin(raph)
sayColorMixin(leo)
sayColorMixin(mickey)
sayColorMixin(donny)

raph.sayColor();		// "Red"
leo.sayColor();			// "Blue"
mickey.sayColor();		// "Orange"
donny.sayColor();		// "Purple"
```


* Explicit Binding - The three methods below help us to declare what `this` will be
	* Call - With `.call` you are immediately invoking the function, and you can pass in arguments one by one
	* Apply - With `.apply` you are immediately invoking the function, but you can pass in an argument such as a list and it will parse it for you
	* Bind - With `.bind` you are creating a brand new function which we can call later
* New Binding - New Binding is when we are using `this` to create new objects

```
var Car = function(make, model, color, year){
	this.make = make;
	this.model = model;
	this.color = color;
	this.year = year;
}

my_car = new Car("Bugatti", "Veyron", "Red", 2015)
```

* Window Binding - The overall object is the window object. From what we know about scope, JavaScript will keep looking upwards until it finds what you are asking for. If it does not it will assume you would want something new to be made.

```
var blah = function(){
	console.log(this.boom)
}

blah() // undefined
window.boom = "You should not be assigning things to the window object"
blah() // "You should not be assigning things to the window object"
```



