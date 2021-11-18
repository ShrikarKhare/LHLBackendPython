class Pizza {
    constructor (size, crust) {
        this.size = size;
        this.crust = crust;
        this.toppings = ['Cheese'];
    }

    addTopping(topping){
        this.toppings.push(topping);
    }
}
let pizza = new Pizza('large', 'thin');
// let pizza1 = new Pizza();
// console.log(pizza1.toppings);
// pizza1.addTopping("mushroom");
// pizza1.addTopping("peppers");
// console.log(pizza1.toppings);
console.log(pizza);
// let pizza2 = new Pizza();
// console.log(pizza2.toppings);
// pizza2.addTopping('more cheese');
// console.log(pizza2.toppings);