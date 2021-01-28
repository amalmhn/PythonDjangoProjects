// var clk=document.querySelector('#clk');
// clk.addEventListener("click",()=>{
//     clk.style.color='red'
//     clk.textContent="clicked"
// })

// var dbclk=document.querySelector('#dbclk');
// dbclk.addEventListener('dblclick',()=>{
//     dbclk.style.color="green"
// })


// var cl = document.querySelectorAll('h1');
// for(c of cl){
//     c.style.color='red'
// }

// var cl = document.querySelector('#clk');
// cl.style.color='red'

// var cl = document.querySelector("#clk");
// cl.textContent='clicked'
// cl.innerHTML='<em>clicked</em>'

var clk = document.querySelector('#clk');
clk.addEventListener('click',()=>{
    clk.style.color='red'
    clk.textContent='clicked'
})


// var hov = document.querySelector('#hov');
// hov.addEventListener("mouseover",function(){
//     hov.style.color='red'
// })

// var hov = document.querySelector('#hov');
// hov.addEventListener("mouseover", function(){
//     // highlight the mouseover target
//     hov.style.color = "orange";
  
//     // reset the color after a short delay
//     setTimeout(function() {
//       hov.style.color = "";
//     },500);
//   }, true);

var hov = document.querySelector('#hov');
hov.addEventListener("mouseover", function(){
    hov.setAttribute('style','color:blue;')
})
hov.addEventListener("mouseout", function(){
    hov.setAttribute('style','color:;')
})