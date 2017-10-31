$(document).ready(function(){
	console.log("hello world")

	$('#search').on('submit', function(event){
		event.preventDefault();

		var omdb = "http://www.omdbapi.com/?t="
		var title = $('#title').val().replace(" ", "+")
// does replace replace all or just the first one it finds?
// maybe use split and then join
// maybe use a regex command


		var search = omdb+title

		$.ajax({
			method: "GET",
			url: search,
			success: function(result){
				console.log(result)
				var item = $('<li>')
				item.append(result.Title)
				item.addClass('collection-item')
				$('.collection').append(item)
				
				// how to break down the result so you can build a for loop to list out all the items
			}
		})

	})
})

// How do you use the endpoint for multiple movies, and then have each movie listed be clickable that lead to the single movie searching endpoint