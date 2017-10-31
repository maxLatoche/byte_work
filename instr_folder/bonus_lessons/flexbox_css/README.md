# What the FLEXBOX?!?!?!

### Learning Objectives

***Students Will Be Able To...***

* Use flex containers
* Style flex children

---
### Context

* Learn a new way to do some bad ass styling

---

### Lesson

##### Part 1 - What is flexbox?

* Flexbox is a layout mode provided in CSS3
* Since it's a newer functionality of CSS it will not be compatible with older browser versions
* We can also check out compatibility issues with [http://caniuse.com/](http://caniuse.com/)
* The Flexbox layout focuses on a X/Y Axis system, different from the CSS Grid systems we've studied of frameworks such as Materialize, Bootstrap, Foundation, and the like.

***NOTE***

* Flexbox is part of CSS. We do not have import any libraries or link any CDN's


##### Part 2 - Flex Containers and Flex Items

***Flex Containers***

* an element that has `display: flex`
* Tries to fill the available space given to it
* Has access to CSS properties to expand and shrink flex items easily inside of it

***Flex Items*** 

* All elements immediately nested inside of a Flex Container automatically become Flex Items

***Note***

* An element can be BOTH a Flex Container AND Flex Item

##### Part 3 - Flexbox Example Starter Code

* Open up the code in the example
* There is some starter code in there
* Here is the HTML file

```
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>FLEXING ALL DAY</title>
	<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/normalize/5.0.0/normalize.min.css">
	<link rel="stylesheet" href="style.css">
</head>
<body>
	<div class='container'>
		<div class="boxItem red">1: RED</div>
		<div class="boxItem green">2: GREEN</div>
		<div class="boxItem blue">3: BLUE</div>
		<div class="boxItem purple">4: PURPLE</div>
		<div class="boxItem pink">5: PINK</div>
	</div>
</body>
</html>
```
* And here is the CSS

```
.boxItem{
	font-size: 5em;
	text-align: center;
	color: white;
}

.red{background-color: red;}
.green{background-color: green;}
.blue{background-color: blue;}
.purple{background-color: purple;}
.pink{background-color: pink;}
```
* We have hooked up the `Normalize CDN` to our HTML file
* Our div with a class `container` will be our flex container
* The direct elements inside of it will be will be flex items

##### Part 4 - What Flexbox has to offer

***display:flex (apply to container)***

* Turns an element into a flex container
* By default will enable flex content to all of it's immediate children
* What happens when we apply `display: flex` to the div with class container?

***flex-direction (apply to container)***

* This will determine the main-axis of the flex container, and in doing so the direction the flex items will appear in. 
* The directions are
	* row - all flex items will appear left to right
	* row-reverse - flex items will appear right to left
	* column - flex items will appear top to bottom
	* column-reverse - flex items will appear bottom to top
* By default the flex direction will always be row
* What happens when we apply row-reverse to the container class? How about column?

***flex-wrap (apply to container)***

* Items that are not told to flex wrap may not reach their full size being stuck in a container
* Go ahead and add a large width to the `.boxItem` class. Maybe 500px to 1000px
* The items will stretch equally as far as they can to the parameters of their parent
* flex-wrap allows flex items to wrap automatically
* There are three choices
	* nowrap - default property
	* wrap
	* wrap-reverse
* Apply the `flex-wrap: wrap` property to the `.container` class while keeping the large set with on your `flex items`
* If your flex-direction was column and you apply a flex-wrap it will not do anything. UNLESS the flex-container has a set height, and the number of flex items inside of it will exceed the height of the container

***justify-content (apply to container)***

* Defines the alignment along the main axis (this is the row or column of the flex-direction)
* justify-content has five options
	* flex-start - items appear at the start of the axis 
	* flex-end - items appear at the end of the axis
	* center - center the items with regard to the main axis
	* space-between - items are distributed evenly on the main axis. first item at the start of the line and the last item on the end of the line
	* space-around - items are evenly distributed on the main axis with equal space around them

***align-items (apply to container)*** 

* Align Items helps us to define how the items will appear on the `cross` axis
* It is very similar to Justify Content but along the cross axis (NOT THE MAIN AXIS)
* The options for align items are
	* flex-start - items appear at the start of the cross axis
	* flex-end - items appear at the end of the cross axis
	* center - items appear center of the cross axis
	* baseline - looks at the text in your items and makes sure the bottom of the text is aligned with the main axis. This helps if your items have different sizes due to the text content
	* stretch - items are stretched to fill the container. this is the default functionality

***align-content (apply to container)***

* Align content works like justify content. 
* It will take the extra space on the cross axis (AXIS NOT FROM THE FLEX DIRECTION)
* Takes the following values
	* flex-start - items are packed to the beginning of the cross axis
	* flex-end - items are packed at the end of the cross axis
	* center - items are centered at the cross axis
	* space-between - items are pushed to the beginning and end of the cross axis and evenly spaced in between
	* space-around - items are evenly distributed
	* stretch - items stretch to cover remaining space. This is the default property

***TEN MINUTE EXERCISE!!!***

* Make a `index.html` file and `style.css`
* Link the files together
* There are two parts to this exercise
* FIRST:
	* Create a red box with the text "Hello World" inside centered both horizontally and vertically
	* Make that red box centered horizontally and vertically with the page 
* SECOND
	* Comment out the code from the first assignment
	* Make 10 divs, each with a different word inside
	* Apply a font-size of 2em to each word
	* Apply a background color to each div
	* Make these divs spread out to the entire width of the container with even spacing in between
* SECOND PART TWO
	* Comment out the CSS for the second section
	* Make the 10 divs spread out evenly from top to bottom

***align-self (apply to item)***

* If there is an item that you want to have a different `align-items` property to it's peers you can apply flex self to that individual item. 
* The values accepted are
	* auto
	* flex-start
	* flex-end
	* center
	* baseline
* Go ahead and add a `align-items: flex-start` to the container and then choose one item to add `align-self: flex-end`

***flex-grow (apply to item)***

* Allows us to grow an item if necessary and there is space. 
* flex-grow will take a number as it's value. By default this number is set to 1. 
* If all items are set to flex-grow 1, they will take up the space of their container evenly
* If one or more of those items have different and higher flex grow numbers, they will take up more of the space than the items with a lower flex-grow
* The size of growth is based off the amount of extra room left. 
	* Example: An item with `flex-grow:2` will take up twice as much of the extra space as `flex-grow:1`
* flex-grow by default is set to zero

***flex-shrink (apply to item)***

* Allows an item to shrink if necessary
* This will help in making your elements responsive to smaller screen sizes
* By default flex-shrink is set to 1
* An item with `flex-shrink:5` will shrink itself five times more than it's siblings without `flex-shrink`

***flex-basis (apply to item)***

* defines the default size of an element BEFORE the remaining space is distributed
* It can be length in percent, em, px, and the like

***flex (apply to item)***

* What to do when there is extra room or when there is no extra room.
* flex is a combination of `flex-grow` / `flex-shrink` / `flex-basis`
* `flex: 1`- scale the items size up or down based off the amount of space left
	* This is a shorthand for setting `flex-grow:1` and `flex-shrink:1`
* If you increase the number of a specific item or items, those elements will take up a larger space on the main axis
* Try adding `flex:2` to one of the flex items
* We can also be more specific by adding three values to flex to represent `flex-grow` / `flex-shrink` / `flex-basis`
* Try adding `flex: 10 5 500px` to one of the flex items

***TEN MINUTE EXERCISE***

* TIME TO DRAW
* Open the example folder and show off the html and corresponding css files. 
* Take two minutes to draw out what you think the html/css will show in the browser

##### Resources

* [http://flexboxfroggy.com/](http://flexboxfroggy.com/)
* [https://flexbox.io/](https://flexbox.io/)
* [https://css-tricks.com/snippets/css/a-guide-to-flexbox/](https://css-tricks.com/snippets/css/a-guide-to-flexbox/)