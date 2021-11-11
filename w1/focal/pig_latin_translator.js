var originalWords = process.argv.slice(2);
var pigLatinWords = [];

for (let i = 0; i < originalWords.length; i++){
  console.log(translatetoPigLatin(originalWords[i]))
  pigLatinWords.push(translatetoPigLatin(originalWords[i]));
}

console.log(pigLatinWords.join(' '));

function translatetoPigLatin(word){
  return word.slice(1,word.length)+word[0] +'ay';
}
