class Pizza {
    constructor (size, crust) {
        this.size = size;
        this.crust = crust;
        this.toppings = ['Cheese'];
    }
    get price() {
        const basePrice = 10;
        const toppingPrice = 2;
        return basePrice + (this.toppings.length * toppingPrice);
    }
    addTopping(topping) {
        this.toppings.push(topping);
    }
    set size(size) {
        if(size === 's' || size === 'm' || size === 'l'){
            this._size = size;
        }
    }
    getSize(size) {
        return this.size;
    }
}
//DRIVER CODE

let pizza = new Pizza('large', 'thin');
// let pizza1 = new Pizza();
// console.log(pizza1.toppings);
// pizza1.addTopping("mushroom");
// pizza1.addTopping("peppers");
// console.log(pizza1.toppings);
// let pizza2 = new Pizza();
// console.log(pizza2.toppings);
// pizza2.addTopping('more cheese');
// console.log(pizza2.toppings);
let pizza2 = new Pizza();
pizza2.size = 's';
pizza2.getSize();
pizza2.price;
console.log(pizza2.price);