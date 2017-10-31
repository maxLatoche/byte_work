# React JS Introduction!!!!

### Learning Objectives
***Students will be able to...***

---

### Context

* Learning a Front End Library

---

### Lesson

#### Part 1 - What is React?

* React is a JavaScript View Library created by Facebook
* It allows us to write code quickly and in an organized manner
* React encourages us to write declarative, functional code

***Note***

* You should practice writing functional / declarative / ES6 code as much as possible.
* Many React tutorials will be given in this syntax.
* It will be much easier to follow along with them if you don't have to worry about understanding ES6 and built in Pure Functions

#### Part 2 - One Way Data Binding vs Two Way Data Binding

***Two Way Data Binding***

* Some frameworks use Two Way Data Binding. For Example Angular 1
* This means that there is a connection between the HTML and the component it is connected to
* Angular users "watchers" and sets up "directives" that will keep a watch on changes in the HTML and the Component.
* If one changes than that change will be reflected in the other.

***One Way Data Binding***

* React uses One Way Data Binding. 
* The HTML does not have the ability to change the component it is connected to
* Updates to the data can occur through event listeners
* The DOM or the Virtual DOM is completely controlled by the logic inside of the component

***NOTE***

* Angular 2 has dropped two way data binding
* [https://www.themarketingtechnologist.co/introduction-to-data-binding-in-angular-2-versus-angular-1/](https://www.themarketingtechnologist.co/introduction-to-data-binding-in-angular-2-versus-angular-1/)
* Feel free to read that on your own time. For now lets get back to React

#### Part 3 - Virtual DOM

* React utilizes a Virtual DOM. 
* Instead of manipulating the actual DOM we are just playing around with JavaScript Objects that are a representation of that DOM. 
* Once we're done "playing around" with these objects we can render them to the actual DOM. 
* React assesses what needs to be changed in the DOM and will update that tree accordingly and efficiently
* This Virtual DOM makes things easier and faster:
	* Instead of performing multiple DOM changes we are creating a copy to our needs and then making one change. 
	* Since everything is just a JS object they are easier to remove/drop into each other. 

#### Part 4 - JSX

* From [http://buildwithreact.com/tutorial/jsx](http://buildwithreact.com/tutorial/jsx)
	* JSX is a preprocessor step that adds XML syntax to JavaScript. 
	* You can definitely use React without JSX but JSX makes React a lot more elegant.
* When creating React Components you may see HTML syntax inside of our render and return statments.
* Example:

```
function HomeComponent(props){
	return(
		<div className="container" style={styles.centering}>
			<h1>This Is Your Movie App!</h1>
			<div className="row">
		    <form className="col s10 offset-s2 m4 offset-m4">
		    	<input 
		    		placeholder="Enter Movie or TV Show Title" 
		    		type="text"
		    		className="validate"/>
		    	<input 
		    		type="submit"
		    		hidden/>
		    </form>
		  </div>
		</div>
	)
}
module.exports = HomeComponent;
```

#### Part 5 - React Components

* Components are the JavaScript Objects that will represent the Virtual DOM
* We will break these up into two types of components
	* Container Components 
	* Presentational Components
* Container Components - Hold the logic and state of that component
* Presentational Component - Are stateless and contain the styling of that component
* Components can be kept small
* Components can be imported and exported anywhere within the app
* Therefore they are extremely reusable

#### Part 6 - State vs. Props

* If we keep our logic in one place and the styling in another place how do the two talk to each other?
* `State and Props` - These are the meat and potatoes of React, or if you're vegetarian, lettuce and tomatoes. 
* State - An immutable object of information that represents the data for that container and what is available to be passed down to the sub components
* `Props` - This represents the data/functions that can be sent to a component. The component can use this data to populate it's JSX Virtual DOM Elements or add event listeners to the Virtual DOM Elements
* To change state use the `this.setState` function. We will see and example of this in the following branches
* When creating and passing functions that will handle events best practice is to use `"handle"` when creating the event listener and `"on"` when passing it as a prop
	* This helps us, and other programmers to understand where the event listener is being created. 
* Lets take a look at the code below:

```
function HomeComponent(props){
	console.log(props)
	return(
		<div className="container" style={styles.centering}>
			<h1>This Is Your Movie App!</h1>
			<div>
		    <form 
		    	onSubmit = {props.onUserSubmit}>
		    	<input 
		    		placeholder="Enter Movie or TV Show Title" 
		    		type="text"/>
		    	<input 
		    		type="submit"
		    		hidden/>
		    </form>
		  </div>

		  <h2>The name from our props is {props.name}</h2>
		</div>
	)
}

const HomeContainer = React.createClass({
	getInitialState(){
		return {
			search: true,
			movieTitle: "",
			yourName: "Jason"
		}
	},
	handleUserSubmit(event){
		event.preventDefault();

		console.log(event.target)
		console.log($(event.target).find("input:text").val())
	},
	render(){
		console.log(this.state);
		return(
			<HomeComponent 
				data = {this.state}
				name = {this.state.yourName}
				onUserSubmit = {this.handleUserSubmit}/>
		)
	}
})

render(
	<HomeContainer/>,
	document.getElementById('app')
)
```
* The `render` method at the bottom comes from the library `ReactDOM` and will take in two parameters
	* `HomeContainer` is the JSX container that will be passed in
	* `document.getElementById('app')` - will target the element in the HTML file that the JS object will be rendered into. 
* HomeContainer - This is our Container class holding all of our state and logic. State is immutable and will represent data that can be passed to all child components as props.
* HomeComponent - This is our `Stateless Presentational Component` holding no logic and will accept the data given to it by the HomeContainer. We can then use this data to be rendered inside the JSX elements. 