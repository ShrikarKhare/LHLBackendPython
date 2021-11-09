const process = require('process');
var args = process['argv'].slice(2);
function sum(numbers){
  var counter = 0
  for(let i = 0 ; i < numbers.length; i++){
    counter += Number(numbers[i])
  }
  return counter
}
console.log(sum(args))
