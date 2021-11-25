class Person {
  constructor(name, quirkyFact, location) {
    this.name = name;
    this.quirkyFact = quirkyFact;
    this.location = location;
  }
  bio() {
    return `My name is ${this.name} and here's my quirky fact: ${this.quirkyFact}`;
  }
  city() {
    return `I am currently in ${this.location}`;
  }
}

class Student extends Person {

  enroll(cohort) {
    this.cohort = cohort;
  }
  bio() {
    return `I'm a student at Lighthouse Labs (aka Labber). ${super.bio()}`;
  }
}
class Instructor extends Person {
  goOnShift() {
    this.onShift = true;
  }
  goOffShift() {
    this.onShift = false;
  }
}
let student = new Student('Shri','I like pineapple on pizza', 'Kingston');
let myInstructor = new Instructor('John', 'I like to sing on the subway', 'Ottawa');
student.enroll('Backend Python');
myInstructor.goOnShift();
myInstructor.goOffShift();
console.log(student);
console.log(student.bio());
console.log(student.city());
console.log(myInstructor);
console.log(myInstructor.bio());
console.log(myInstructor.city());