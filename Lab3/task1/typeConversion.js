let value = true;
alert(typeof value); // boolean

value = String(value); // now value is a string "true"
alert(typeof value); // string


alert( "6" / "2" ); // 3

let str = "123";
alert(typeof str); // string

let num = Number(str); // becomes a number 123

alert(typeof num); // number


let age = Number("an arbitrary string instead of a number");

alert(age); // NaN, conversion failed


alert( Number("   123   ") ); // 123
alert( Number("123z") );      // NaN (error reading a number at "z" - undefined)
alert( Number(true) );        // 1
alert( Number(false) );       // 0
alert( Number(null) );       // 0
