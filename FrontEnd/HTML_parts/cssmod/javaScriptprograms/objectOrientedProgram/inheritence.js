class Parent{
    m1(){
        console.log("Inside parent")
    }
}
class Subchild extends Parent{
    m2(){
        console.log("inside subchild")
    }
}
class Child extends Subchild{ //extends keyword for inheritence
    m3(){
        console.log("inside child")
    }
}

var c=new Child();
c.m1()
console.log("Hi")


//hw employee data structure and bank application