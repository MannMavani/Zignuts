class Shape {
    area() {
        return 0;
    }
}

class Circle extends Shape {
    constructor(radius) {
        super();
        this.radius = radius;
    }
    area() {
        return Math.PI * this.radius * this.radius;
    }
}

class Triangle extends Shape {
    constructor(base, height) {
        super();
        this.base = base;
        this.height = height;
    }
    area() {
        return 0.5 * this.base * this.height;
    }
}


const circle = new Circle(10);
console.log("Circle Area:", circle.area());

const triangle = new Triangle(4, 6);
console.log("Triangle Area:", triangle.area());
