# Python with Comp Sci

### Learning Objectives
***Students Will Be Able To...***

* Diagram the Linked List concepts
* Diagram Stacks and Queues
* Find out the Big O notation for various Comp Sci concepts

---
### Context

* We are covering some computer science topics to help us think efficiently while programming

---
### Lesson

#### Part 1 - Linked List

* The concept of Linked List is to have a list of values to search through. 
* This sounds similar to an array but it is very different, with it's own advantages and disadvantages
* A `Linked List` stores data in `nodes`
* Each node will contain two things. A `value` that node is storing, and a `pointer` that will point to the next node in the list
* The first node in a linked list is known as the `head`

***So how is this different from python list, or arrays in other languages?***

* With linked list we are not storing/declaring our data set initially. Instead we are only looking at one node at a time. This will save us memory. 
* The advantage to this versus an array/list is we will not use as much memory to navigate through a list of values. 
* Imagine if we had an extremely large data set. We wouldn't want to store it in memory just to loop through it. 
* The disadvantage to this is since we are not declaring all the values up front we do not have the ability to start a search at a specific point in time. We have to loop through every node until we find what we want. 
* We don't have to declare how big the linked list will be, unlike looping through an array

***Five Min Exercise***

* How do we add a new node in a linked list? 
* Draw a diagram with three nodes: A --> B --> C
* How would you enter a node called "X" in between A and B?

***Answer***

* Placing a node X between two nodes B and C
* Make the pointer on the X node point to the value in the C node 
* Make the B next pointer point to the X node

```
* temp  = A.next
* A.next = X
* X.next = temp

OR more simply

* X.next = B
* A.next = X
```
* The top way with `temp` takes into account how we have to loop through a linked list. The second set in the box is just for demonstration
* Remember that the only sense of direction we get in a linked list is through their `next` pointer. 
* Traveling through an entire linked list one by one is `Big O of n` or "O(n)"
* If a nodes next pointer is `null` we know we are at the end of the list


#### Part 2 - Big O Notation

* Big O Notation is a way to check/describe how efficient an algorithm is. That is how long it takes to run
* Looping through a list of items in a linear fashion will be a `O(n)`
* Having a loop nested inside of another loop will be an `O(n^2)`
* Using the Binary Search would be a `O(logn)`

***Five Min Exercise***

* What would be the Big O of the following three functions?

```
def the_names():
	for name in people:
		print name
	
	

def your_func():
	for num in numbers:
		print num
	
	for char in characters:
		print char
		
		
		
def my_func():
	for x in xyz:
		for a in abc:
			print x
			
	for i in j:
		print i

```
* We only use the most significant terms
	* If we had a function with two for loops(not nested) it would be `O(2n)`. However, we would drop the 2 from that equation because as n gets exponemtially larger the two doesn't matter. 
	* If we had a function with three loops, loop A was a stand alone, and loop C was nested in loop B it would be `O(n + n^2)`. We would drop the smaller n in this equation for the same reason as the previous example


#### Part 3 - Stacks

* Stacks are abstract data types. Like Linked List this is a concept that is programmable in multiple languages
* This follows the LIFO process. (Last In First Out)
* Every `node` holds a `value` and a `pointer` to the next node
* Imagine a list/array turned 90 degrees to be vertical, where the first element is on the bottom and the last element is on the top
* The main methods to quickly display stacks are `pop` and `append` (push in other lanuages)
* `pop` will remove the top node on the stack and return it to you
* `append` will add a node to the top of the stack

![](https://upload.wikimedia.org/wikipedia/commons/b/b4/Lifo_stack.png)


***Five Min Exercise***

* Without using the `reverse` method reverse the string "Hello World"



#### Part 4 - Queues

* Queues are also abstract data types, but they work in the opposite way of stacks. That is they follow the FIFO process (First In, First Out)
* Imagine an array/list normally (not turned 90 degrees like the stack diagram)
* `Enqueue` - add a node to the end of the queue
* `Dequeue` - to remove a node from the front of the queue

![https://upload.wikimedia.org/wikipedia/commons/thumb/5/52/Data_Queue.svg/405px-Data_Queue.svg.png](https://upload.wikimedia.org/wikipedia/commons/thumb/5/52/Data_Queue.svg/405px-Data_Queue.svg.png)




#### REQUIRED Reading and Watching

* [https://study.cs50.net/trees](https://study.cs50.net/trees)
* [https://study.cs50.net/linked_lists](https://study.cs50.net/linked_lists)
* [https://study.cs50.net/queues](https://study.cs50.net/queues)
* [https://study.cs50.net/stacks](https://study.cs50.net/stacks)

#### Videos and Tutorials

***Big O Notation***

* [Wiki](https://en.wikipedia.org/wiki/Binary_search_algorithm)
* [Interview Cake](https://www.interviewcake.com/article/python/big-o-notation-time-and-space-complexity)

***Linked Lists***

* [CS50 Youtube Video](https://www.youtube.com/watch?v=5nsKtQuT6E8)

***Linear and Binary Search***

* [Youtube Video on both](https://www.youtube.com/watch?v=wNVCJj642n4)
* [Just Binary Search](https://www.youtube.com/watch?v=JQhciTuD3E8)
* [Just Linear Search](https://www.youtube.com/watch?v=iwo5WAldDks)

***Assert Method***

* [Tutorials Point](http://www.tutorialspoint.com/python/assertions_in_python.htm)
