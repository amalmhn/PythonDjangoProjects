var employee={
    eid:1001,
    name:"ajay",
    desig:"developer",   
    salary:25000        
}

console.log(employee)
console.log(employee["name"])
console.log(employee['salary'])
// simple way below
console.log(employee.name)
console.log(employee.salary)

console.log('exp' in employee) // checking exp keyword in the employee object
                                // the keyword 'in' has different uses in array and object

if('exp' in employee==false){ // adding exp to this object
    employee['exp']=2
}
console.log(employee)