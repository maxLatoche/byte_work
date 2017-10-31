# Python with Comp Sci Part 2

### Learning Objectives 
***Students Will Be Able To...***

* Diagram the Binary Search and Linear Search concepts
* Pseudo Code the two sorting algorithms

---
### Context

* A continuation of computer science topics
* These are other sorting algorithms that will teach us how to think efficiently while programming

---
### Lesson


#### Part 1 - Bubble Sort

* Bubble sort is one of the simplest algorithms to program but also one of the slowest sorting methods with a "O(n^2)"
* It will iterate through an array/list multiple times and checks if the current value is greater than or less than the next value. If it is then switch the position, if it is not then the next value will now be the current value. 
* Rinse and Repeat

![https://upload.wikimedia.org/wikipedia/commons/c/c8/Bubble-sort-example-300px.gif](https://upload.wikimedia.org/wikipedia/commons/c/c8/Bubble-sort-example-300px.gif)


#### Part 2 - Insertion Sort

* Insertion sort is another sorting method with a "O(n^2)" but at the same time is more efficient than bubble sort. 
* With insertion we are iterating through the array/list and checking that current value against all the values that we have already passed (the sorted section)

![](https://upload.wikimedia.org/wikipedia/commons/0/0f/Insertion-sort-example-300px.gif)

***Five Min Exercise***

* Why is this still considered "O(n^2)"
* Pseudo code this insertion sort and explain


#### Part 3 - Binary Search and Linear Search

* Linear Search is easier to program
    * You are looping through an array one by one until you find what you are looking for
    * "O(n)" - going through each value
* Binary Search is harder to program but more efficient
    * This only works with a sorted array/list  
    * Identify where the middle is, cut this in half, search through that half
    * "O(log n)" - binary search way. this is usually the fastest


#### Part 4 - Benchmarking

* Benchmarking your code means to grab the execution time of your code
* Writing a benchmark function must have certain parameters
	* The function you want to benchmark
	* The amount of times you want it to run
* Your benchmark function should return the total amount of time it took to run.
* You can utilize the `timeit library` for this function.
	* You may also use the `datetime library` we studied earlier as well.  

***HINT***

* You might find an example of how to use `timeit` in the example code we did for Big O Notation

#### REQUIRED reading and watching

* [https://study.cs50.net/insertion_sort](https://study.cs50.net/insertion_sort)
* [https://study.cs50.net/bubble_sort](https://study.cs50.net/bubble_sort)
* [https://study.cs50.net/binary_search](https://study.cs50.net/binary_search)

#### Resources

* [Stack Wiki](https://en.wikipedia.org/wiki/Stack_(abstract_data_type)
* [Queue Wiki](https://en.wikipedia.org/wiki/Queue_(abstract_data_type)
* [Bubble Wiki](https://en.wikipedia.org/wiki/Bubble_sort)
* [Insertion Wiki](https://en.wikipedia.org/wiki/Insertion_sort)
