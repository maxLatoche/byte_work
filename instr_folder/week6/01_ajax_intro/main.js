// // Example of XHR GET request talking to OMDB

// console.log("ELLO WARLD")

//   var xhr = new XMLHttpRequest();

//   xhr.open('GET', 'http://www.omdbapi.com/?t=top+gun&y=&plot=short&r=json', true);

//   xhr.onload = function() {
//    // status codes below 200 and above 400 usually means there's an error
//    console.log(xhr)
//     if (xhr.status >= 200 && xhr.status < 400) {
//      // If there was no error lets store the response and console log it
//       var movie_response = xhr.responseText;
//       // console.log(movie_response);
//     } else {
//       // If we do get an error console log something to tell us
//       console.log('SOMETHING IS WRONG!!!');
//     }
//   };

//   xhr.onerror = function() {
//     // Connection problem
//     console.log('Dear client your connection sucks, get off comcast');
//   };

//   xhr.send();









// Example of above but with jQuery AJAX method

// $(document).ready(function(){
//   console.log("ELLO WARLD")

//   $.ajax({
//     method: "GET",
//     url:"http://www.omdbapi.com/?t=top+gun&y=&plot=short&r=json",
//     success: function(result){
//       console.log(result);
//       console.log(result.Title);
//     }
//   })  
// })









// USING HTML FORM

$(document).ready(function(){
  console.log("ELLO WARLD")

  $('#button').on('click', function(event){
    console.log(event)
    event.preventDefault();

    var $movie_searched = $('input[name="movie"]').val().replace(" ", "+")
    console.log($movie_searched);

    $.ajax({
      method: "GET",
      url: "http://www.omdbapi.com/?t="+$movie_searched,
      dataType: "jsonp",
      success:function(response){
        console.log(response)
        $('.blah').append(response.Title)
      }
    })
  })
})











