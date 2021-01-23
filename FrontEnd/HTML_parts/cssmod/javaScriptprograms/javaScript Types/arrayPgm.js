var arr=[10,20,"hello",10.5]
arr[0]=100;
// console.log(arr[0])

for(let i=0;i<arr.length;i++){// .length will define the length of the array
    console.log(arr[i])
}
console.log("**********")
for(let num of arr){ // you will get the contents
    console.log(num)
}
console.log("**********")
for(let num in arr){ // you will get the index values
    console.log(num)
}
console.log("**********")
arr.push(150)
console.log(arr)
console.log("**********")
arr.pop() // to remove the element from the array
console.log(arr)
console.log("**********")