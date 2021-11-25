class Person {
  constructor(first, last, age) {
    this.first = first;
    this.last = last;
    this.age = age;
  }

  fullName() {
    return `The full name is ${this.first} ${this.last}`;
  }
  displayAge() {
    return `${this.first} ${this.last} is ${this.age} years old`;
  }
    
}

let myPerson = new Person("John", "Smith", 24);
console.log(myPerson.fullName());
console.log(myPerson.displayAge());
