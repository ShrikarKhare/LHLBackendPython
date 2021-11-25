const process = require('process');
let args = process['argv'].slice(2);
const sum = (numbers) => {
  let counter = 0;
  for (let i = 0; i < numbers.length; i++) {
    counter += Number(numbers[i]);
  }
  return counter;
};
console.log(sum(args));
