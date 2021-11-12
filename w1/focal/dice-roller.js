//take user input
const numDice = Number(process.argv.slice(2));

//function to randomize dice rool within the bounds of 1 & 6
function Randominteger(min, max){
  min = Math.ceil(min);
  max = Math.floor(max);
  return Math.floor(Math.random()*(max-min+1)+min);
}
//function to handle dice roll depending on the number of dice. ceil and floor are used to prevent decimal values
function diceRoll(numDice){
  const result =[];
  for(let i = 0; i < numDice; i++){
    //a 6 sided die must roll between 1 and 6
    result.push(Randominteger(1,6));
  }
  return `Rolled ${numDice} dice: ${result.join(',')} `;
}
//calling event
diceRoll(numDice)
