# Phase 2 - Code Against Humanity!

#### Description

* Congratulations on making it to the end of phase 2. There's just one more hurdle you have to hop over (hopefully with ease). 
* After this you're off to your final project and then the start of an amazing technology career.
* In this assessment we're going to code our own version of [Cards Against Humanity](https://cardsagainsthumanity.com/). 

#### Rules of Cards Against Humanity

* In case you have never played the game here are the rules (For our dumbed down version)
* The user will be (The Judge)
* There will be five "Players"
* The Judge (the user) will get a "Black Card" which will contain a "fill in the blank" section
* Here is an example of a black card

```
________ gives me uncontrollable gas.

OR

The class field trip was completely ruined by _________.
```
* The other players will present one white card which represents their "answer" to the blank portion of the black card. 
* The Judge will select whichever white card they think is the funniest response to the black card they drew. 
* Some examples of white cards are

```
Sniffing Glue
Dick Cheney
2 year old Taco Bell burrito
```

#### Objective 1

* Using Flask or Django, we're going to seed a database full of Black Cards and White Cards. 
	* [Here is a textfile containing blackcards](http://www.cardsagainsthumanity.com/bcards.txt)
	* [Here is textfile containing whitecards](http://www.cardsagainsthumanity.com/wcards.txt)
	* [Here is an API endpoint of all black and white cards](http://www.crhallberg.com/cah/output.php)
* This is a very simple version of Cards Against Humanity
* There will be five "players" that will populate a random white card each. In this case the "players" are just whatever cards the computer randomly generates
* "The Judge" will be the user who clicks which white card goes with their black card. 
* Whichever card the user clicks, that "player" will be awarded a point

#### Objective 2 

* You will need three routes in this Project to populate the cards
	* "GET /" will return our main page.
	* "GET /blackcards" will return a JSON of a random Black Card from the database.
	* "GET /whitecards" will return a user a JSON response of 5 random white cards from the database.
* Your main page should have a button that makes an AJAX GET request to /blackcards that displays the ONE black card on the page. 
	* There will only ever be ONE black card on the page at a time. 
* There should be another button that makes an AJAX GET request to /whitecards that displays FIVE white cards on the page
	* * There will only ever be FIVE white cards on the page at the same time.
* The user (judge) will click on which white card they believe is the funniest to go with the black card
	* All the cards on the screen will go away
	* The only thing that should show is the combined text of both the white card and the black card
	* Award the player a point, keep a score board on the side of the page
		* This doesn't have to be an ajax request.
		* You could just have a score that is rendering through the JavaScript file
		* This means the score will always show Players 1 - 5 have ZERO every time the server or browser refreshes
* The user now has the option to continue playing by clicking the black card and white cards buttons

#### HINTS

* This will all be done on ONE project
* Seed the database of the project
* Have a template that will make the GET REQUEST to the endpoints
* You will need to use Mustache Templates or DOM Manipulation to eliminate and show new cards
* How will you write your code so the user (the judge) can pick which card is the winnder for that round? Will you assign each white card their own button or better yet, make the cards clickable?!?!?!

#### GOOD LUCK!

* Remember this is an open book assessment
* Feel free to refer back to your notes, we had many exercises with similar procedures
* Good luck!

#### BONUS 1

* Style your cards to make them look like the actual cards
* Once you have that working, style your White and Black cards. They should look as close as possible to what they actual cards look like - [see them here](http://s3.amazonaws.com/cah/CAH_MainGame.pdf)
* That font is Helvetica Bold 15pt. That's not a free font - try a lookalike like [Droid Sans](https://www.google.com/fonts#UsePlace:use/Collection:Droid+Sans) or [Open Sans](https://www.google.com/fonts#UsePlace:use/Collection:Open+Sans). Follow the directions on that page to link the font in your site. 
* Don't worry about the logo on the bottom of the cards - but DO worry about the black / white borders, card size / shape, and anything else you think makes your web implementation look like them.

#### BONUS 2

* Take that point system further
* Allow the user to give each player a name
* Those names and their points will be scored in a database
		
		
		
		
		
		
		