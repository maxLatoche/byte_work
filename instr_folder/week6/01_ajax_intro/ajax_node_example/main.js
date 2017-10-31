var fs = require('fs');

fs.readFile('The_Legends_Of_King_Arthur_And_His_Knights.txt', function(err, data){
	if (err){
		return console.error(err);
	}
	console.log("We have finished reading King Arthur, Asynchronously...")
});


fs.readFile('The_Sense_Of_Wonder.txt', function(err, data){
	if (err){
		return console.error(err);
	}
	console.log("We have finished reading The_Sense_Of_Wonder, Asynchronously...")
});

fs.readFile('Forty-One_Thieves.txt', function(err, data){
	if (err){
		return console.error(err);
	}
	console.log("We have finished reading Forty-One_Thieves, Asynchronously...")
});

console.log("FINISHED ALL THE BOOKS")




