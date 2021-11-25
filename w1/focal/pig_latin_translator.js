let originalWords = process.argv.slice(2);
let pigLatinWords = [];

for (let i = 0; i < originalWords.length; i++) {
  console.log(translatetoPigLatin(originalWords[i]));
  pigLatinWords.push(translatetoPigLatin(originalWords[i]));
}

console.log(pigLatinWords.join(' '));

const translatetoPigLatin = (word) => {
  return word.slice(1,word.length) + word[0] + 'ay';
};
