# Sort By Example
---

* You will be given two values
	* An array of random integers
	* an array that will container the order of which you will sort the first array
* Write a function that will take in these two arrays. `arr` and `example_arr` and return `arr` sorted in the same format as `example_arr`
* Assume Example Array catalogs all elements possibly seen in the input Array.
* However, the input Array does not necessarily have to have all elements seen in the Example.
* Example:

```
arr = [1,3,4,4,4,4,5]
example_arr = [4,1,2,3,5]

print(exampleSort(arr, example_arr))

Result: [4,4,4,4,1,3,5]
```
