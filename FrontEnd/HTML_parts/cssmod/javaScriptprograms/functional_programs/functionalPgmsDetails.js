//lambda = arrow
//arrow
//map
//filter
//reduce
//sort


var add=(num1,num2)=>num1+num2;
var res=add(20,20)
console.log(res)

var sub=(num1,num2)=>num1-num2;
var resSub=sub(20,17)
console.log(resSub)

var cube=num=>num**3;
var resCube=cube(2);
console.log(resCube)

var arr=[5,6,3,11,12]
arr.sort((num1,num2)=>num1-num2);
console.log(arr)

console.log("******")

// var sqr = arr.map(num=>num**2);
// console.log(sqr)

arr.map(num=>num**2).forEach(num=>console.log(num));

