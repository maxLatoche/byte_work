# Async Example

* Asynchronous JavaScript may be a little hard to wrap your head around in the beginning. 
* Within this folder is an example of reading multiple text files asynchronously 
* We will be using the `fs` library inside node to read these text files
* There are three books
	* Forty One Thieves txt file 
		* 4047 Lines
	* The Legends of King Arthur txt file
		* 9930 Lines
	* The Sense Of Wonder txt file
		* 1193 Lines
* Let's take a look at the `main.js` file

```
var fs = require('fs');

fs.readFile('Forty-One_Thieves.txt', function(err, data){
	if (err){
		return console.error(err);
	}
	console.log("We have finished reading Forty-One_Thieves, Asynchronously...")
});

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

console.log("FINISHED ALL THE BOOKS")
```
* Let's take a look at the file in order
	* We are requiring a node library. This is similar to importing in python
	* fs comes with a `readFile()` method that runs asynchronously
	* Async means that as the code reads top down, it will start the next statement even if the current function/s are not completed
	* A console.log at the bottom for good measure
* Now RUN YOUR CODE IN THE TERMINAL!!!! `node main.js`
* Notice the first line will be "FINISHED ALL THE BOOKS". even though this statement is the last statement in the file.
* Also the order the books are finished reading are not in the same order as we have it in the code.
* Feel free to move things around, the order will not follow the code top down. It will be console.logged as each process is finished
* Sometimes the book order may change. This is because the code is read top down but the readFile methods will run the moment it is read, and it will not wait for the previous statement to be completed. 