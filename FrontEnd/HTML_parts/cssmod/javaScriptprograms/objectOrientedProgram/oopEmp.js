class Employee{
    constructor(eid,name,salary,exp){
        this.eid=eid
        this.name=name
        this.salary=salary
        this.exp=exp
    }
    printData(){
        console.log(this.eid)
        console.log(this.name)
        console.log(this.salary)
        console.log(this.exp)
    }
}

var obj1=new Employee(100,"Ajay",2500,2);

obj1.printData()
