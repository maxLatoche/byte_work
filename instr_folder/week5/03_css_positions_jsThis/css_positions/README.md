# Put things where you want!

### Learning Objectives
***Students will be able to...***

* Utilize CSS display properties
* Utilize CSS position properties
* Diagram Normal Document Flow
* Use z-index

---
### Context

* HTML is cool and all, but to make things more beautiful we'll be using CSS

---
### Lesson

##### Part 1 - Different Display Types

* Before we talk about Normal Document Flow lets do a quick review of the two main display types for elements

***Inline***

* Inline Elements are usually those that define text and data. 
	* `a href`
	* `img` 
	* `span`
	* `strong`
	* `em`
	* `abbr`
* All of these elements will appear in the same line

***Block***

* Block elements will occupy the entire width of their parent container, even if they do not fill out the whole width.
* They are making BLOCKS inside the HTML 
* Almost all of these blocks will have a default padding around them for line breaks.
	* Remember the default style is determined by the browser
* Some block elements are
	* `div`
	* `h1 - h6`
	* `article`
	* `footer`
	* `section`

***BONUS: None and Inline-Block***

* What do you think will happen if we gave an element display none? Pretty much what it says. You're welcome.
	* Think about our script tags and head tags.
* Inline-block: You are now allowed to make block elements appear next to each other. Inline-Block display says "Make these elements inline and allow the user to set a width and a height"
* Look at the `inline-block` example exercise for an example to see how this works.

##### Part 2 - Normal Document Flow

* Now lets get back to topic of Normal Document Flow
* As we consistently mention, every browser interprets HTML elements differently. 
* Normal Document Flow is how the browser renders your HTML without any CSS or JS. 
* As we know things are read from top to bottom
* What type of displays the elements have also plays a hand in the Normal Document Flow
* The screen size also plays a part in how elements appear in the NDF
* [Check out this tutsplus blog for more info on NDF](http://webdesign.tutsplus.com/articles/quick-tip-utilizing-normal-document-flow--webdesign-8199)

##### Part 3 - Box Model Review

* How can we manipulate the position of elements?
* Remember the box model?	
![](http://www.turnwall.com/wp-content/uploads/2014/06/box-model-css.png?670861)

* We can also target all of these and change just one side using `top`, `right`, `bottom`, `left`


##### Part 4 - `%`, `px`, `em`, `rem`, and `auto`
  
* Before we continue lets talk briefly about the different css measurements
* `px`: is a static unit of measure and will stay the same no matter what screen size
* `em`: relative measurement. 1em = 16px. Elements with `em` will scale to the size of it's parent element
* `rem`: stands for `Root em` and is also a relative measurement. `rem` is almost the same as `em` except it is relative to the ROOT font size.
* `%`: always relative to the parent element. When measuring height, the height of the container MUST be set. There is always a default width to a screen size but not a default height
* `auto`: allows us to tell an element to resize itself with regards to it's content. A block level element 	with height auto will grow with more text. With margin auto it will increase it's margins to be centered with the y-axis

***Tips and Resources***

* [StackOverFlow meaning of Auto](http://stackoverflow.com/questions/4471850/what-is-the-meaning-of-auto-value-in-a-css-property)
* [em vs rem](https://j.eremy.net/confused-about-rem-and-em/)

##### Part 5 - Different Positions

* CSS gives us the `position` property to help us format out HTML better.
* They are:
	* `float`
	* `fixed`
	* `absolute`
	* `relative`
	* `static`

***STATIC***

* The default position
* Does not count as being positioned

***FLOATS***

* WE NEVER USE FLOATS
* Floats takes elements out of the NDF
* Take a look at the two examples below and how the text is forced to wrap around the image. 
    -  ```float: right```: ![](http://xhtml.com/510ACA5B-DC0D-4E03-B6BF-861FD62E91F3/float-right.gif)
    - ```float: left```: ![](http://xhtml.com/510ACA5B-DC0D-4E03-B6BF-861FD62E91F3/float-left.gif)

- Every HTML elements that follows a floating element will flow around it. For instance if you have a paragraph that extends longer than an image it will flow underneath it. To avoid this, use the `clear` property. 
- ```clear: left;``` will "turn off" the left floating of elements
* I WILL NOT BE DEMOING THIS BECAUSE WE WILL NEVER BE USING FLOATS

***FIXED***

* Fixed position will always be relative to the browser. 
* It will stay on the screen even if the user scrolls up or down

***ABSOLUTE***

* NEVER USE ABSOLUTE!!!
* It removes elements from the NDF
* If a child element has position absolute the parent will act as if the child is not there
* The element with position absolute will work relative to it's direct parent BUT the parent and all other elements will not recognize a element with position absolute
* Other elements collapse around it (and appear hidden "behind" the element that has absolute positioning). 

***RELATIVE***

* Elements that are relatively positioned will position itself according to where it should have been in the Normal Document Flow. 
* Other elements don't collapse around it. 
* It will act the same way as static positioning unless you add properties
* From [vanseodesign](http://vanseodesign.com/css/css-positioning/)

```
The relatively positioned element is taken out of the normal document flow, but still affects the elements around it. Those elements just act as though the positioned element is still in the normal document flow.
```

***Z-index***

* Assigns a layer number to an element. The higher numbers appear in front of the lower numbers.

##### Part 6 - All the exercise files