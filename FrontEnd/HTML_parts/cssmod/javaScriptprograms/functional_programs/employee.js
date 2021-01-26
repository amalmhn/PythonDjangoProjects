var employee=[
    {eid:100,name:"ajay",salary:2500,exp:2},
    {eid:101,name:"vjay",salary:2300,exp:2},
    {eid:102,name:"jjay",salary:2800,exp:2},
    {eid:103,name:"xjay",salary:2400,exp:2},
    {eid:104,name:"bjay",salary:2700,exp:2},
    ] 

// for(let emp of employee){
//     console.log(emp.name)
// }
// console.log("*****************")

// employee.forEach(emp=>console.log(emp.name))

// convert all employee name into uppercase
// print emplyee according with their salary


//document object model and AJAX is the imp things
//AJAX getting the data from the backend without redirecting or reloading the page 

var maxsal=employee.map(obj=>obj.salary).reduce((o1,o2)=>o1>o2?o1:o2)
console.log(maxsal)

console.log('***************');

var empsort=employee.sort((o1,o2)=>o1.salary>o2.salary?-1:1)
        console.log(empsort)

console.log('***************');
//implmtn all qns we did in py
var emp=employee.filter(ob=>ob.salary>2500);
console.log(emp)

console.log('***************');

var selName= employee.filter(obj=>obj.name=='vjay');
console.log(selName);

console.log('***************');

console.log(employee)