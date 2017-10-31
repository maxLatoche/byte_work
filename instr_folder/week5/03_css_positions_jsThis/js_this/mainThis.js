$(document).ready(function(){

	// example 1

	// $("button").on("click", function(){
	// 	debugger;
	// 	console.log(this)
	// 	//What will it look like if I use the below example instead?
	// 	console.log($(this))
	// })

	// // example 2

	// console.log(this)

	// example 3

	// var myThis = function(){
	// 	console.log(this)
	// }

	// $("button").on("click", myThis)


	// example 4
	// var Car = function(make, model, color, year){
	// 	this.make = make;
	// 	this.model = model;
	// 	this.color = color;
	// 	this.year = year
	// };

	// var bugatti = new Car("Bugatti", "Veyron", "red", 2013)

	// console.log(bugatti)
	// console.log(bugatti.color)

	var turtle = {
    name: "Raph",
    color: "Red",
    sayColor: function(){
      console.log(this.color)
	  }
	}
	turtle.sayColor();

});