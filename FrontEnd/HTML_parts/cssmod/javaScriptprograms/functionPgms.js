var res=0;
function add(num1,num2){
    let res=num1+num2;
    // let res=num1+num2; if you dont wanna use the 'res' outside the function you can use 'let'
    //let is used for block level scope
    console.log(res)
}


add(10,20)
console.log(res)