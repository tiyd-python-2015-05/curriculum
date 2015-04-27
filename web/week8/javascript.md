# JavaScript!

---

## Big Differences vs Python

* Significant whitespace vs braces
* No namespacing
* No classes
* All numbers are floats
* No list comprehensions

---

## Small Differences vs Python

* `var` to declare variables
* `==` vs `===`
* `undefined` and `null` vs `None`
* dicts vs "objects"

---

## Using braces

```py
# Python
if name == "Sam":
    return "Hi, Sam!"
```

```js
// JavaScript
if (name === "Sam") {
    return "Hi, Sam!";
}
```

---

## Declaring functions

```py
# Python
def welcome(name):
    return "Hi, " + name
```

```js
// JavaScript
function welcome(name) {
    return "Hi, " + name;
}
```

---

## if-else

```javascript
if (answer === "1") {
    return "Right answer!"
} else if (answer === "2") {
    return "Wrong answer!"
} else {
    return "Invalid answer!"
}
```

---

## while

```py
# Python
num = 0
while num < 3:
    num += 1
    print(num)
```

```javascript
// JavaScript
var num = 0;
while (num < 3) {
    num++;
    console.log(num);
}
```

---

## for

```py
# Python
for n in range(3):
    print(n)
```

```javascript
// JavaScript
for (var n = 0; n < 3; n++) {
    console.log(n);
}
```

---

## Declaring variables

You must _always_ use `var` before declaring a variable the first time. If you don't, it will work, but not do what you expect.

```javascript
// Good
var x = 1;

// BAD
y = 1;
```

---

## What's this `===`?

JavaScript is not very strict about types, so `==` will say that many things are equal.

https://dorey.github.io/JavaScript-Equality-Table/

`===` does no conversions.

---

## Type coercion

```py
# Python
>>> 1 + ""
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for +: 'int' and 'str'
```

```js
// JavaScript
> 1 + ""
'1'
```

---

## More type coercion

```js
1 + ""     // => '1'
[] + 0     // => '0'
0 + {}     // => '0[object Object]'
{} + 0     // => 0
"" + false // => 'false'
0 + false  // => 0
0 + true   // => 1
[] + {}    // => '[object Object]'
{} + []    // => 0
```

---


## Functions are everything

Functions can be:

* assigned to variables
* passed as arguments
* returned from functions

This is not that different from Python, but often looks different.

---

## Anonymous Functions

```py
# Python
welcome = lambda thing: "Hello " + thing + "!"

welcome("class")
```

```javascript
// JavaScript
var welcome = function (thing) {
  return "Hello " + thing + "!";
}

welcome("class");
```

---

## Functions as arguments

```py
# Python
def print_cube(x):
    print(x * x * x)

for number in [1, 2, 3]:
    print_cube(number)
```

```javascript
// JavaScript
[1, 2, 3].forEach(function (number) {
  console.log(number * number * number);
});
```

---

## Returning functions

```javascript
function greet(greeting) {
  return function() {
    return greeting + " world!";
  };
}

var hello = greet("Hello");
var goodbye = greet("Goodbye");

hello(); // Hello world!
goodbye(); // Goodbye world!
```

---

## Map vs list comprehensions

```py
# Python
[x * 2 for x in [1, 2, 3, 4]]
```

```js
// JavaScript
[1, 2, 3, 4].map(function (x) { return x * 2 })
```

---

## Filter vs list comprehensions

```py
# Python
[x for x in [1, 2, 3, 4] if x % 2 == 0]
```

```js
// JavaScript
[1, 2, 3, 4].filter(function (x) { return x % 2 === 0 })
```

---

## Map and filter vs list comprehensions

```py
# Python
[x * 2 for x in [1, 2, 3, 4] if x % 2 == 0]
```

```js
// JavaScript
[1, 2, 3, 4].
    filter(function (x) { return x % 2 === 0 }).
    map(function (x) { return x * 2 })
```

---

## Objects

```js
var dog = {
    name: "Fido",
    talk: function () { return "bark" }
}

dog.name; // => "Fido"
dog['name']; // => "Fido"
dog.talk(); // => "bark"
dog['talk'](); // => "bark"
```

---

## JavaScript and the DOM

---

## The Document Object Model

HTML is read and turned into a tree of nodes. The DOM is that tree.

Each node has properties and methods accessible via JavaScript.

---

## `window` and `document`

These are always available in the DOM.

* `window` is the window containing the DOM document. It is the top-level object and everything on it is available globally.
* `document` is the DOM document. It is at the top of the tree and all DOM nodes are under it.

---

## Elements

Each HTML tag gets turned into an element. Some common attributes and methods:

* `.id`
* `.innerHTML`
* `.parent`
* `.children`
* `.addEventListener(eventType, callback)`

---

## Resources

* [REPLit](http://repl.it/)
* [JSBin](http://jsbin.com)
* [Mozilla Developer Network - JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
