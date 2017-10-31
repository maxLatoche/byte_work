var nums = [12,234,43,31,62,7,2,3,8,5,4];

var sum = nums.reduce(function(total, num){
		console.log(total)
    return total + num
}, 0)

console.log(sum)

// var nums = [12,234,43,31,62,7,2,3,8,5,4];

// var even = nums.filter(function(num){
//     return num%2 === 0
// })

// console.log(nums)   // [ 12, 234, 43, 31, 62, 7, 2, 3, 8, 5, 4 ]
// console.log(even)

// var x = [1,2,3,3,1,5,7,9,4]

// for(var i = 0; i<x.length; ++i){
// 	console.log(x[i]*2)
// }

// var y = 5;

// var newArr = x.map(function(val){

// 	if (val % 2 === 0){
// 		return val*y
// 	}
// 	return val
// })

// console.log(newArr)
// console.log(x)
