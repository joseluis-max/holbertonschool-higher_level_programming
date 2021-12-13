### Javascript Warm Up !
- **Why JavaScript programming is amazing ?**
    1. is a powerful programming language that can add interactivity to a website.
    2. is versatile and beginner-friendly.
    3. is relatively compact, yet very flexible.
    4. Developers have written a variety of tools on top of the core
        - API's
        - Frameworks and libraries
- **How to run a JavaScript script ?**
    
    Adding the shebang `#!/usr/bin/node` in the first line in the executable script. ****
    
- **How to create variables and constants ?**
    
    ```jsx
    let myVariable;
    var my_Variable;
    const MyVariable;
    ```
    
- **What are differences between `var`, `const` and `let`**
    
    `let` → declares a block-scoped local variable;
    
    allows you to declare variables that are limited to the scope of a [block](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/block) statement, or expression on which it is used
    
    `var` → declares a function-scoped or globally-scoped variable; 
    
    The scope of a variable declared with `var` is its current *execution context and closures thereof*, which is either the enclosing function and functions declared within it, or, for variables declared outside any function, global.
    
    `const` → is a constant variable;
    
- **What are all the data types available in JavaScript**
    
    Primitive Values: immutable datum represented directly at the lowest level of the language.
    
    `string`
    
    `number`
    
    `array` 
    
    `boolean`
    
    `object` → collection of properties.
    
    `null` → represent the intentional absence of any object value, is treated as false for boolean operations.
    
    `undefined` → A variable that has not been assigned a value has the value `undefined`.
    
    A method or statement also returns `undefined` if the variable that is being evaluated does not have an assigned value. 
    
    A function returns `undefined` if a value was not returned.
    
    Objects: collection of properties.
    
- **How to use the `if`, `if ... else` statements**
    
    ```jsx
    if (expression conditional){
    	//block code conditional true
    } else {
    	//block code conditional false
    }
    ```
    
- **How to use comments**
    
    ```jsx
    /* 
    	 this 
    	 a comment
    	 block
     */
    // this is a comment line
    ```
    
- **How to affect values to variables**
    
    ```jsx
    let name = "Luis";
    const id = 0150454320;
    ```
    
- **How to use `while` and `for` loops**
    
    ```jsx
    while (expression conditional){
    	// block code.
    }
    for (count, expression conditional, increment or decrement statement){
    	// block code.
    }
    ```
    
- **How to use `break` and `continue` statements**
    
    `break` → out of the current loop
    
    `continue` → jump to the next iteration
    
- **What is a function and how do you use functions**
    
    A way of packaging functionality that you wish to reuse.
    
    ```jsx
    function multiply(num1,num2) {
      let result = num1 * num2;
      return result;
    }
    ```
    
- **What does a function that does not use any `return` statement return**
    
    Return `undefined`
    
- **Scope of variables**
    
    `block scope`
    
    `function scope`
    
    `global scope`
    
- **What are the arithmetic operators and how to use them**
    
    [Operators](https://www.notion.so/ab89d9bf11f44b5d9785f712008dd01c)
    
- **How to manipulate dictionary**

```jsx
/* dot notation */
person.age = 45; 

/* bracket notation */
person['eyes'] = 'hazel';
```

- **How to import a file**
    
    We need require to include modules and modules use exports to make things available.
    
    ```jsx
    /* simplest module */
    require('./foo.js');
    
    /* P1: define a global */
    //foo.js
    foo = function () {
    	console.log('foo!');
    }
    
    // app.js
    require('./foo.js');
    foo();
    
    /* P2: export an anonymous function */
    //bar.js
    module.exports = function (){
    	console.log('bar!');
    }
    // apps.js
    var bar = require('./bar.js');
    bar();
    
    /* P3: export a named function */
    // fiz.js
    exports.fiz = function () {
      console.log('fiz!');
    }
    // app.js
    var fiz = require('./fiz.js').fiz;
    fiz();
    
    /* P4: export an anonymous object */
    // buz.js
        var Buz = function () {};
    
        Buz.prototype.log = function () {
          console.log('buz!');
        };
    
        module.exports = new Buz();
    // app.js
        var buz = require('./buz.js');
        buz.log();
    
    /* P5: export a named object */
    // baz.js
        var Baz = function () {};
    
        Baz.prototype.log = function () {
          console.log('baz!');
        };
    
        exports.Baz = new Baz();
    // app.js
        var baz = require('./baz.js').Baz;
        baz.log();
    
    /* P6: export an anonymous prototype */
    // doo.js
        var Doo = function () {};
    
        Doo.prototype.log = function () {
            console.log('doo!');
        }
    
        module.exports = Doo;
    // app.js
        var Doo = require('./doo.js');
        var doo = new Doo();
        doo.log();
    
    /* P7: export a named prototype */
    // qux.js
        var Qux = function () {};
    
        Qux.prototype.log = function () {
          console.log('baz!');
        };
    
        exports.Qux = Qux;
    // app.js
        var Qux = require('./qux.js').Qux;
        var qux = new Qux();
        qux.log();
    ```
    
    Pros and cons:
    
    Named exports - one module, many exported things
    
    Anonymous exports - simpler client interface
    
    exports VS module.exports:
    
    - exports is an alias to module.exports
        
        ```jsx
        > module.exports.fiz = "fiz";
        > exports.buz = "buz";
        > module.exports === exports;
        true
        ```
        
    - Assigning anything to exports directly will overwrite the exports alias.
        
        ```jsx
        > module.exports.qux = "qux";
        > exports
        { qux: "qux" }
        > exports === module.exports
        true
        > exports = "wobble wibble wubble!";
        > exports === module.exports
        false
        > exports
        "wobble wibble wubble!"
        > module.exports
        { qux: "qux" }
        // module.exports is canonical
        ```
        
    
    [Node.JS Module Patterns](http://darrenderidder.github.io/talks/ModulePatterns/#/)
    
    [GitHub - mbeaudru/modern-js-cheatsheet: Cheatsheet for the JavaScript knowledge you will frequently encounter in modern projects.](https://github.com/mbeaudru/modern-js-cheatsheet)
    
    [](https://github.com/standard/semistandard)