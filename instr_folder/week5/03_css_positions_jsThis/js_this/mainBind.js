$(document).ready(function(){
	console.log("We have connected the Main Bind JS file")

	var xMen = {
		data: [
			"Wolverine", 
			"Cyclops", 
			"Jean Grey", 
			"ShadowCat", 
			"Professor X", 
			"Gambit",
			"Rogue",
			"Nightcrawler",
			"Storm",
			"Angel",
			"Beast",
			"Colossus",
			"Jubilee"
		],
		clicker : function(event){
			console.log(this)
			var randomIndex = Math.floor((Math.random()*this.data.length-1))
			alert("Hello Your partner is " + this.data[randomIndex])
		}
	}


	// This will work. 
	// Why do you think this will still run?
	// From what we did in the earlier example when invoking "this" the button object should be passed to the callback
	
	// $("button").on("click", function(){
	// 	console.log(this)
	// 	xMen.clicker()
	// })

	// This will throw you an error
	// $("button").on("click", xMen.clicker)

	// We need to bind what we want to call
	$("button").on("click", xMen.clicker.bind(xMen))
})