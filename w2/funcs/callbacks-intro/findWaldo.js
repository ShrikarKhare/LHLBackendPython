// The second argument/parameter is expected to be a (callback) function
const findWaldo = function(names, found) {
    // for (let i = 0; i < names.length; i++) {
    //   let name = names[i];
    //   if (name === "Waldo") {
    //     found(i);   // execute callback
    //   }
    // }
    names.forEach( (name, i) => { //first arg will be each element of arr, 2nd is the index which is needed for the return statement.
        if(name === 'Waldo'){
            found(i);
        }
    })
  }

  const actionWhenFound = function(index) {
    console.log(`Found him at index ${index}!`);
  }

  findWaldo(["Alice", "Bob", "Waldo", "Winston"], actionWhenFound);
