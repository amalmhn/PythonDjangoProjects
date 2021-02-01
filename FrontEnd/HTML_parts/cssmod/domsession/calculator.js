function displayBox(number){
    let txt=document.querySelector('#inputs');
    txt.value+=number; //string cocation
}

function clearBox(){
    let txt = document.querySelector('#inputs').value=' ';

}

function calculate(){
    let expression = document.querySelector('#inputs').value;
    let result = eval(expression);
    document.querySelector('#inputs').value=result;
}