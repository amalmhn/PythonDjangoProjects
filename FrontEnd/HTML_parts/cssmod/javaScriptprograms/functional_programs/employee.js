var employee=[
    {eid:100,name:"ajay",salary:2500,exp:2},
    {eid:101,name:"vjay",salary:2500,exp:2},
    {eid:102,name:"jjay",salary:2500,exp:2},
    {eid:103,name:"xjay",salary:2500,exp:2},
    {eid:104,name:"bjay",salary:2500,exp:2},
    ] 

for(let emp of employee){
    console.log(emp.name)
}
console.log("*****************")

employee.forEach(emp=>console.log(emp.name))

// convert all employee name into uppercase
// print emplyee according with their salary


//document object model and AJAX is the imp things
//AJAX getting the data from the backend without redirecting or reloading the page 