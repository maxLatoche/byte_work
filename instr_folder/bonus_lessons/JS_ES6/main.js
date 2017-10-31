// var myFunc = function(){
// 	var a = 10;
// 	var a = 50;	
// 	// var b;

// 	if (a === 100){
// 		var b = 20;
// 	}

// 	c = 30;

// 	console.log(a)
// 	console.log(b)
// }

// myFunc();
// console.log(c);

// const myFunc = function(){
// 	let a = 10;
	
// 	if (a === 100){
// 		let b = 20;
// 	}
// 	c = 30;

// 	console.log(a)
// 	console.log(b)
// }

// myFunc();
// console.log(c);

// const a = 10;
// const a = 20;

// console.log(a)

// let name = "Peter Parker";
// let crime = true;

// if (crime){
// 	name = "Spider-man"
// }
// console.log(name);


// const movie = {
// 	title: "Top Gun",
// 	year: 1986
// }

// movie = {
// 	name:"Jason",
// 	vision: "20/20"
// }

// const movie = {
// 	title: "Top Gun",
// 	year: 1986
// }

// movie.title = "Kill Bill",
// movie.year = 2003

// console.log(movie)

// const movies = [
// 	"The Man From Nowhere",
// 	"The Usual Suspects",
// 	"District 9",
// 	"John Wick",
// 	"The Raid",
// 	"Good Will Hunting"
// ]

// for (let i = 0; i<movies.length; ++i){
// 	let temp = movies[i];
// 	console.log(temp);
// }


// const favThings = {
// 	movies : ["John Wick", "The Usual Suspects", "The Raid", "Good Will Hunting"],
// 	tvShows : ["Scrubs", "True Detective", "Game of Thrones", "The Black Donnellys"],
// 	footballTeam : "New Orleans Saints",
// 	ufcFighter : "George St. Pierre"
// }



// const breakItDown = (obj) =>{
// 	const {
// 		movies, 
// 		tvShows, 
// 		footballTeam, 
// 		ufcFighter
// 	} = obj;

// 	console.log(movies);
// 	console.log(tvShows);
// 	console.log(footballTeam);
// 	console.log(ufcFighter);
// }

// breakItDown(favThings);

var x = document.querySelector('#clicker');


console.log(x)

// x.addEventListener('click', function(event){
// 	console.log(this)
// })

x.addEventListener('click', (event)=>{
	console.log(this)
})







