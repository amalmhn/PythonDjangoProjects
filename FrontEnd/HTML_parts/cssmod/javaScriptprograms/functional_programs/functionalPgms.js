//lambda=>arrow function
//map()
//filter
//reduce
//sort

//SORT fn
//******* */
// var arr=[5,6,3,11,12] // it will sort with the 1st digit. So we cant use this fnctn directly
// arr.sort()
// console.log(arr)


//ARROW fn BELOW
//***************
// function add(num1,num2){
//     return num1+num2
// }

// var add=(num1,num2)=>num1+num2
// var cube=num=>num**3
// var sub=(num1,num2)=>num1-num2

// //to call this fn
// var addres=add(10,20)

// console.log(addres)


//SORT fn for ascending and descending
// var arr=[6,5,4,2,11,12]
// arr.sort((num1,num2)=>num1-num2)// num1 must come before num2
// console.log(arr)


//MAP fn
// var arr=[6,5,4,2,11,12]
// var sq=arr.map(num=>num**2)
// console.log(sq)

//forloop fn

// var arr=[6,5,4,2,11,12]
// arr.map(num=>num**2).forEach(num=>console.log(num))// internal iteration

// for(let num of arr){
//     console.log(num) // extrenal iteration
// }

var arr=[6,5,4,2,11,12]

var total=arr.reduce((o1,o2)=>o1+o2)

var mx=arr.reduce((o1,o2)=>)