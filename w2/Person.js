class Person {
    constructor(name, quirkyFact) {
        this.name = name;
        this.quirkyFact = quirkyFact;
    
    }
    bio() {
        return `My name is ${this.name} and here's my quirky fact: ${this.quirkyFact}`;
    }
}

class Student extends Person {

    enroll(cohort) {
        this.cohort = cohort;
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

// var student = new Student('Backend Python');
// student = new Person('Shri', 'I like pineapple on pizza');
// // student.enroll('Backend Python');
// console.log(student)