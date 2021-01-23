// var text="hello hai hello how"
// var word=text.split(' ')
// console.log(word)
// console.log(word.length)

// function count(str) {
//     var obj = {};
    
//     str.split(" ").forEach(function(el, i, arr) {
//       obj[el] = obj[el] ? ++obj[el] : 1;
//     });
    
//     return obj;
//   }
  
//   console.log(count("hello hai hello how"));

var text="hello hai hello how"
var word=text.split(' ')
var wcnt={}

for(let wrd of word){
  if(wrd in wcnt){
    wcnt[wrd]+=1
  }
  else{
    wcnt[wrd]=1
  }
}

console.log(wcnt)