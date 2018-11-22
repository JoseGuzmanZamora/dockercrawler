const myModule = require('./test');
let val = myModule.hello(); // val is "Hello"  

function tengoquesalir(q,w,e,r,t){
    console.log("dfa");
}

const mymodules = require('./test2');
let valu = mymodules.hellos(); // val is "Hellos"

const mymodulesy = require('./requiere2');
let valus = mymodulesy.hellom(); // val is "Hellos"

var hola = 1

for (let i = 0; i < a.length; i++) { 
    let x = a[i] 
} 
for (let i = 0; i < b.length; i++) { 
    let y = b[i]
} let callbacks = [] 
for (let i = 0; i <= 2; i++) { 
    callbacks[i] = function () { 
        return i * 2 } 
    } 

    class Point {
        constructor(x, y) {
            this.x = x;
            this.y = y;
        }
        toString() {
            return '(' + this.x + ', ' + this.y + ')';
        }
    }
    
    class ColorPoint extends Point {
        constructor(x,y,color) {
            super(x,y);
            this.color = color;
        }
        toString() {
            return super.toString() + ' in ' + this.color;
        }
    }
    
    let cp = new ColorPoint(25, 8, 'green');
    cp.toString(); // '(25, 8) in green'
    
    console.log(cp instanceof ColorPoint); // true
    console.log(cp instanceof Point); // true
    elementos.map(function(elemento){ 
        return elemento.length;
    });  // [8, 6, 7, 9]
    
    elementos.map((elemento) => {
      return elemento.length;
    }); // [8, 6, 7, 9]
    
    elementos.map(({length}) => length); // [8, 6, 7, 9]    

    elementos.map(function hola(elemento){ 
        return elemento.length;
    });  // [8, 6, 7, 9]


    export var hsola = 90;
    
    hola = (q,f,g,h) => {
        var holass = 9;
    }