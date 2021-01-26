class Person{
    constructor(age,name){
        this.age=age;
        this.name=name;
    }
    printPerson(){
        console.log(this.age)
        console.log(this.name)
    }
}

var obj1=new Person(25,"Ajay") //new keyword to create an object
// obj1.setPerson(25,"Ajay");
obj1.printPerson()


