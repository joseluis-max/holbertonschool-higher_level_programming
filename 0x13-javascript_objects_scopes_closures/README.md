# Javascript OOP

- **Why JavaScript programming is amazing**

    1. is a powerful programming language that can add interactivity to a website.
    2. is versatile and beginner-friendly.
    3. is relatively compact, yet very flexible.
    4. Developers have written a variety of tools on top of the core
        - API's
        - Frameworks and libraries

- **How to create an object in JavaScript**

    ```jsx
    const person = {};
    person.name = "José";
    person.age = 22;
    person.greet = ()=>{
     console.log("Hello, I am " + this.name);
    }

    const person = {
     name = "José",
     age = 22,
     greet = () => {
      console.log("Hello, I am " + this.name);
     }
    }
    ```

    JavaScript uses special functions called **constructor functions** to define and initialize objects and their features.

    ```jsx
    /* constructor functions returning a object */
    function CreateNewPerson(name) {
      const obj = {};
      obj.name = name;
      obj.greeting = function() {
        alert('Hi! I\'m ' + obj.name + '.');
      };
      return obj;
    }
    
    const salva = CreateNewPerson('Salva');
    salva.name;
    salva.greeting();
    
    /* constructor functions with this */
    function Person(name) {
      this.name = name;
      this.greeting = function() {
        alert('Hi! I\'m ' + this.name + '.');
      };
    }
    
    /* Object() constructor and Object.create() method */
    let person1 = new Object({
      name: 'Chris',
      age: 38,
      greeting: function() {
        alert('Hi! I\'m ' + this.name + '.');
      }
    });
    
    let person2 = Object.create(person1);
    ```

    Classes

    Classes are a template for creating objects. They encapsulate data with code to work on that data.

    Declarations

    One way to define a class is using a **class declaration**. To declare a class, you use the `class`keyword with the name of the class ("Rectangle" here).

    ```jsx
    class Rectangle {
      constructor(height, width) {
        this.height = height;
        this.width = width;
      }
    }
    ```

    Expressions

    A **class expression** is another way to define a class. Class expressions can be named or unnamed. The name given to a named class expression is local to the class's body. However, it can be accessed via the `name` property.

    ```jsx
    // unnamed
    let Rectangle = class {
      constructor(height, width) {
        this.height = height;
        this.width = width;
      }
    };
    console.log(Rectangle.name);
    // output: "Rectangle"
    
    // named
    let Rectangle = class Rectangle2 {
      constructor(height, width) {
        this.height = height;
        this.width = width;
      }
    };
    console.log(Rectangle.name);
    // output: "Rectangle2"
    ```

    Class body and method definitions

    The body of a class is the part that is in curly brackets `{}`. This is where you define class members, such as methods or constructor.

    The body id executed in strict mode for increased performance.

    The constructor method is a special method for creating and initializing an object created with a `class`. There can only be one special method with the name "constructor" in a class.

    A constructor can use the `super` keyword to call the constructor of the super class.

    Static initialization blocks

    Class static initialization blocks allow flexible initialization of class static properties including the evaluation of statements during initialization, and granting access to private scope.

    Multiple static blocks can be declared, and these can be interleaved with the declaration of static properties and methods (all static items are evaluated in declaration order).

    [Class static initialization blocks - JavaScript | MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/Class_static_initialization_blocks)

    Prototype methods

    ```jsx
    class Rectangle {
      constructor(height, width) {
        this.height = height;
        this.width = width;
      }
      // Getter
      get area() {
        return this.calcArea();
      }
      // Method
      calcArea() {
        return this.height * this.width;
      }
    }
    
    const square = new Rectangle(10, 10);
    
    console.log(square.area); // 100
    ```

    Generator methods

    ```jsx
    class Polygon {
      constructor(...sides) {
        this.sides = sides;
      }
      // Method
      *getSides() {
        for(const side of this.sides){
          yield side;
        }
      }
    }
    
    const pentagon = new Polygon(1,2,3,4,5);
    
    console.log([...pentagon.getSides()]); // [1,2,3,4,5]
    
    ```

    Static methods and properties

    The [static](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/static) keyword defines a static method or property for a class. Static members (properties and methods) are called without instantiating their class and **cannot** be called through a class instance.

    ```jsx
    class Point {
      constructor(x, y) {
        this.x = x;
        this.y = y;
      }
    
      static displayName = "Point";
      static distance(a, b) {
        const dx = a.x - b.x;
        const dy = a.y - b.y;
    
        return Math.hypot(dx, dy);
      }
    }
    
    const p1 = new Point(5, 5);
    const p2 = new Point(10, 10);
    p1.displayName; // undefined
    p1.distance;    // undefined
    p2.displayName; // undefined
    p2.distance;    // undefined
    
    console.log(Point.displayName);      // "Point"
    console.log(Point.distance(p1, p2)); // 7.0710678118654755
    ```

    [Classes - JavaScript | MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes)

- **What `this` means**

    The `this` keyword refers to the current object the code is being written inside.

- **What `undefined` means**

    `undefined` is a property of the *global object*. That is, it is a variable in global scope. The initial value of `undefined` is the primitive value `[undefined](https://developer.mozilla.org/en-US/docs/Glossary/undefined)`.

    A variable that has not been assigned a value is of type `undefined`. A method or statement also returns `undefined` if the variable that is being evaluated does not have an assigned value. A function returns `undefined` if a value was not

- **Why the variable type and scope is important**

    Define the behaviour of the variables in our program!

- **What is a closure**

    A **closure** is the combination of a function bundled together (enclosed) with references to its surrounding state (the **lexical environment**). In other words, a closure gives you access to an outer function’s scope from an inner function. In JavaScript, closures are created every time a function is created, at function creation time.

    ```jsx
    function makeFunc() {
      var name = 'Mozilla';
      function displayName() {
        alert(name);
      }
      return displayName;
    }
    
    var myFunc = makeFunc();
    myFunc();
    ```

- **What is a prototype**

    Prototypes are the mechanism by which JavaScript objects inherit features from one another.

- **How to inherit an object from another**

    The `extends` keyword can be used to subclass custom classes as well as built-in objects.

    The `.prototype` of the extension must be an `[Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object)` or `[null](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/null)`.

    ```jsx
    class Square extends Polygon {
      constructor(length) {
        // Here, it calls the parent class' constructor with lengths
        // provided for the Polygon's width and height
        super(length, length);
        // Note: In derived classes, super() must be called before you
        // can use 'this'. Leaving this out will cause a reference error.
        this.name = 'Square';
      }
    
      get area() {
        return this.height * this.width;
      }
    }
    ```

    Prototypes are the mechanism by which JavaScript objects inherit features from one another.

    ```jsx
    function Person(first, last, age, gender, interests) {
    
      // property and method definitions
      this.name = {
        'first': first,
        'last' : last
      };
      this.age = age;
      this.gender = gender;
      //...see link in summary above for full definition
    }
    let person1 = new Person('Bob', 'Smith', 32, 'male', ['music', 'skiing']);
    ```

    ![Screenshot 2021-12-14 at 11-13-05 Object prototypes - Learn web development MDN.png](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects/Object_prototypes/mdn-graphics-person-person-object-2.png)
