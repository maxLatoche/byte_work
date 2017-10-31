# EXPRESS YOSELF!

* Regular expressions are patterns to match strings.
* To the naked eye it just looks like chuck norris showed up behind you and started slamming your head into the keyboard.
* BUT hopefully after this README it will all make sense
* Checkout [pythex](http://pythex.org/) and use it to test your regular expressions

##### Syntax

* Find a range of capital letters. Any one capital letter will match this pattern
	* `[A-Z]`
* Same thing with the range but add a condition. This condition states it has to be three characters or more
	* `[A-Z]{3,}`
* The first range tells us we can use any letter, capital, lowercase, or number. The condition is there has to be six characters that match
	* `[A-Za-z0-9]{6}`
* The ^ indicates the string must start with that first expression. Here it is LOL. \s means whitespace. It ends with a range of any letter lower or upper case. * means the range can be any length
	* `^LOL\s[A-Za-z]*`



```py
'LOL Hi' # Matches  
'LOL whatsupdog' # Matches  
'LOLyo' # doesn't match, no whitespace  
'LOL hey d00d' # doesnt match, only letters allowed  
'whats up' # doesn't match, must start with LOL  
```

***Now take a look at the below prompts and write your answers in the other markdown file***

#### Round 1: Name

Make a regex pattern that matches a properly written name, like the following:

Miley Cyrus  
Justin Bieber  
Katy Perry  

Notice the pattern - the first letter of the first name is capitalized, the rest is lower case. There is a space. The first letter of the last name is capitalized, the rest is lower case.

#### Round 2: Phone Number

Write a regex pattern that validates a correct phone number, like any of the following:

212-555-1023  
(917)888-2424  
5164329123  

Area codes cannot start with 0 or 1. There may be parentheses around the area code. There must be a set of 3 numbers (area code) a set of 3 numbers(city) and set of 4 numbers. There may be dashes between them. There must be 10 numbers in total, no more no less.

#### Round 3: Email Address

Write a regex pattern that validates a correct email address, like the following:

sales@somestore.com  
roger.smith@yahoo.net  
hi@my-domain.info  

#### Round 4: URL

Write a regex pattern to validate URLs, like the following:

http://www.google.com  
http://yahoo.net  
http://my-site.github.io

#### Round 5: grep with regex

Now use regex with grep to search files on your computer!

Search for all files that end in .py  
Search for all files that end in .jpg  
Search for all files that contain your name  

Have fun and sandbox.
