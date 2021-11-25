const nameInverter = (name) => {
  //undefined
  if (name === undefined) {
    return 'Error';
  }
  name = name.trim(); //.trim() removes whitespaces
  let namearray = name.split(' '); //split up individual words by spaces.
  let honorific = ['Mr.', 'Mrs.', 'Ms.', 'Dr.']; //assuming these are the only titles used.
  //Empty String
  if (name === '') {
    return '';
  }
  //first last to last first and does not have honorific
  if (namearray.length === 2 && honorific.includes(namearray[0]) === false) {
    return namearray[1] + ', ' + namearray[0];
  }
  //honorific first name
  if (namearray.length === 2 && honorific.includes(namearray[0])) {
    return namearray[0] + ' ' + namearray[1];
  }
  //honorific last name first name
  if (namearray.length > 2 && honorific.includes(namearray[0])) {
    return namearray[0] + ' ' + namearray[2] + ', ' + namearray[1];
  }
  //just honorific
  if (honorific.includes(namearray[0])) {
    return '';
  }
  //single name when passed a single name
  return name;
};
module.exports = nameInverter;