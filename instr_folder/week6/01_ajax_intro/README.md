# MOAR JAVASCRIPT

### Learning Objectives
***Students will be able to...***

* Use ajax calls to talk to api's

---
### Context

* All people care about is speed, lets give it to them.

---
### Lesson

#### Part 1 - AJAX Intro

- AJAX stands for Asynchronous JavaScript And XML
- Remember when we dealt with API's the responses that came back to us were either in `JSON` or `XML`
- `XML` format used to be what was widely used and therefore it fit into the `AJAX` acronym.  
- You can ignore the XML part for now because as you know we are ONLY dealing with JSON formatted data
- We will be able to make requests using JavaScript
- Yay single paged applications!
- Examples of AJAX in use:
  - Think about how your email updates your inbox without you refreshing the page?
  - The constant newsfeed scrolling down on Facebook, Twitter, Tumbler, and the like

***WHY IS THIS SO GREAT?!?!?!***

* Our server will have to do less.
* We are putting more items on the client side
* There is a clearer line between what the front end will do and what the back end will do
* The Asynchronous ability of AJAX will allow faster response times

***WHAT PROBLEMS MIGHT WE FACE***

* The back button and the refresh button don't work with Single Page Apps
* JavaScript can be disabled by people (This is a crazy thing to do, i don't care about people who choose to turn off JS)

#### Part 2 - Practice

* Let's make an API request and get back some data using AJAX
* Make an HTML and a JS file

```
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Document</title>
</head>
<body>

  <script src="main.js"></script>
</body>
</html>
```
* Run a console log in your js file to make sure it's connected

```
console.log("ELLO WARLD")
```
* Let's make a GET request to the OMDB api.
* Back to our go to movie. Grab the endpoint for top gun
* Now that its connected let's try this code in the JS file

```
console.log("ELLO WARLD")

  var request = new XMLHttpRequest();
  request.open('GET', 'http://www.omdbapi.com/?t=top+gun&y=&plot=short&r=json', true);

  request.onload = function() {
    // status codes below 200 and above 400 usually means there's an error
    if (request.status >= 200 && request.status < 400) {
      // If there was no error lets store the response and console log it
      var movie_response = request.responseText;
      console.log(movie_response);
    } else {
      // If we do get an error console log something to tell us
      console.log('SOMETHING IS WRONG!!!');
    }
  };

  request.onerror = function() {
    // Connection problem
    console.log('Dear client your connection sucks, get off comcast');
  };

  request.send();
```

***What the hell did we just do?***

* `request.open` - this takes three arguments.
  * `method` - first argument. What type of HTTP verb are we using?
  * `url` - second argument. What is the endpoint we are hitting
  * `async` - third argument. Is this call expected to be asynchronous
* When that request loads run the function
* Control flow statement to tell us if there is an error or not

#### Part 3 - jQuery AJAX

* What we just saw was how AJAX requests are made in Vanilla JavaScript

***Side Note***

* You should know how to do this or at least that it exists, there are many code challenges I know of that ask for things to be done in only Vanilla JS.

***Back to the lesson***

* WRAP IT IN CASH
* jQuery gives us several methods where we can shorten everything we did up top to one command.

```
$(document).ready(function(){
  console.log("ELLO WARLD")

  $.ajax({
    method: "GET",
    url:"http://www.omdbapi.com/?t=top+gun&y=&plot=short&r=json",
    success: function(result){
      console.log(result);
    }
  })
})
```

#### Part 4 - JSONP

* How does AJAX work with forms?
* What's this JSONP all about? [http://stackoverflow.com/questions/2067472/what-is-jsonp-all-about](http://stackoverflow.com/questions/2067472/what-is-jsonp-all-about)
* JSONP stands for "JSON with Padding"
* It is used to pass information between different domains
* Normally when making a request you will be crossing over to a different domain and that is usually a problem
* Example Below:

```
$(document).ready(function(){
  console.log("ELLO WARLD")

  $('#button').on('click', function(event){
    event.preventDefault();

    var movie_searched = $('input[name="movie"]').val().replace(" ", "+")
    console.log(movie_searched);

    $.ajax({
      method: "GET",
      url: "http://www.omdbapi.com/?t="+movie_searched,
      dataType: "jsonp",
      success:function(response){
        console.log(response)
        $('.blah').append(response.Title)
      }
    })
  })
})
```
* We are grabbing the button and applying a click event to it
* The `event.preventDefault()` helps us to prevent the form from actually submitting and re-rendering the template
* The variable grabs the value and edits it so we can plug it into the url
* Make the ajax call as usual
* Add a `dataType: "jsonp"`

#### HTTP CRUD

| HTTP Method | Action                        | Example URI                      |
|-------------|-------------------------------|----------------------------------|
| GET         | Grab data for ALL items       | http://movies.com/api/movies     |
| GET         | Grab data for a specific item | http://movies.com/api/movies/898 |
| POST        | Create a new item             | http://movies.com/api/movies     |
| PUT         | Update an existing item       | http://movies.com/api/movies/898 |
| DELETE      | Delete a specific item        | http://movies.com/api/movies/898 |

#### Postman

* This is an extension in chrome that allows you to make calls to an api to see what we can get. 
* It becomes handy when you want to test the other HTTP Methods on an API
* ***This is better than CURL***

#### Resources

* [https://developer.mozilla.org/en-US/docs/AJAX/Getting_Started](https://developer.mozilla.org/en-US/docs/AJAX/Getting_Started)
* [http://code.tutsplus.com/tutorials/24-best-practices-for-ajax-implementations--net-9180](http://code.tutsplus.com/tutorials/24-best-practices-for-ajax-implementations--net-9180)