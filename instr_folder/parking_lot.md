# Parking Lot

### Class Notes

##### Methods - 

***Here is a list of some methods we have used in class. Look in the python docs for more details***

* `append` - add a value to the back of a list
* `split` - split a string and turn it into a list of values
* `join` - join the values of a list together and turn it into a string
* `len` - get the length of an iterable
* `str` - turn a data type into a string
* `int` - turn a data type into a integer
* `pop` - remove a value from a list
* `keys` - returns a list of all keys in a dictionary
* `values` - returns a list of all values in a dictionary
* `items` - returns a list where each index represents a key and value

##### String Concatenation

* There are various ways to combine strings. 
* My favorite way is to use the curly brackets so you can specify where each value will be injected into the string without having to worry about the positions you pass those values to the format method.

```
name = "Jason"
money = "10.45"

print("Hi " + name + " you owe me $" + money + " for lunch")
print("Hi %s you owe me $%s for lunch"%(name, money))
print("Hi {x} you owe me ${y} for lunch".format(x=name, y=money))
```

### Python REPL

* You can open the Python REPL in your terminal by just typing `python3`
* OR if you want to open a specific file in the Python REPL type `python3 -i file.py`
* To exit your REPL press "ctrl+d" or type "quit()"
* If you type `dir()` and pass a value into the parenthesis the REPL will return to you all the methods that value has access to
* You can also type `help()` and search for definitions of various vocabulary words and methods of different Python objects


### Keyboard Shortcuts
	
* cmd+tab === navigate between different programs
* cmd+` === navigate between windows of the same program 

### Sublime Text Shortcuts

* cmd+d === highlight the next occurance of the same word
* cmd+/ === comment in/out
* cmd+shift+(any directional arrow) === highlights all text to the top/right/bottom/left

### Emmet Shortcuts

* `!+tab` if you do this in html it will produce the boilerplate HTML file for you
* use a tab to complete your element

```
h1 + tab === <h1></h1>
``` 
* use an arrow to indicate nested element

```
div > h1 + tab === <div><h1></h1></div>
```
* use a * to indicate you want repeats of that element

```
ul>li*3 + tab ===

	<ul>
		<li></li>
		<li></li>
		<li></li>
	</ul>
```

* give an element an id or a class

```
div.blah + tab === <div class="blah"></div>
```



### Resources

* [http://caniuse.com/](http://caniuse.com/) - site that shows you what elements, css, and js is allowed in what browser versions
* [https://coolors.co/](https://coolors.co/) - A color scheme generator. Helps you decide on colors for a website and the like
* Emmet - A sublime text package for faster HTML coding
* Color Picker - A sublime text package that allows for you to pick hex colors
* [https://www.youtube.com/watch?v=8aGhZQkoFbQ](https://www.youtube.com/watch?v=8aGhZQkoFbQ) - What The Heck Is The Event Loop Anyway JSConf EU 2014
* [https://color.adobe.com/create/color-wheel/](https://color.adobe.com/create/color-wheel/) - adobe color picker. similar to color picker package for sublime.
* [https://philipwalton.github.io/solved-by-flexbox/](https://philipwalton.github.io/solved-by-flexbox/) - A resource for using flexbox
* [https://www.canva.com/font-combinations/](https://www.canva.com/font-combinations/) - help with fonts
* [http://typecast.com/blog/a-more-modern-scale-for-web-typography](http://typecast.com/blog/a-more-modern-scale-for-web-typography) - more help with fonts


### Best Practices

* Keep your workspace clean. Keep your tabs in sublime and google chrome to a minimum

### Food Places

* Chipotle - 
	* Madison Ave, btw 40th and 39th str
* Dig Inn - 
	* Madison Ave, btw 40th and 39th str
* Pret A Manger - Ready to go salads and wraps
	* Madison Ave, 39th str
* Cafe Zaiya - Japanese Cafe
	* 41st street between Madison and 5th
* Sunrise Mart - Japanese Cafe and Grocery Store
	* 41st street between Madison and 5th
* Mcdonalds - Doo Doo
	* Madison and 40th street
* Num Pang - Viet Sandwiches
	* 41st street between Lexington and 3rd
* Choza - Taqueria
	* 41st street between Park and Madison (Next Door)
* Shake Shack - American
	* 40th street and 3rd avenue
* Norikoh - Japanese
	* 39th street, between Madison and 5th ave
* Nirvana - Indian Buffet
	* Lexington between 40th and 39th street
* Hunan Manor - Chinese
	* Lexington between 40th and 39th street
* Rhong-Tiam - Thai
	* 39th street and Lexington
* Essen - American 
	* Madison Avenue between 41st and 40th
	