//REVERSE A string

//Reverse the provided string.
// You may need to turn the string into an array before you can reverse it.
// Your result must be a string.

function reverseString(str) {
  return str
    .split('')
    .reverse()
    .join('');
}

//OR
function reverseString(str) {
  var array = str.split('');
  var arrrev = [];
  var revstr = '';

  for (var i = array.length - 1; i >= 0; i--) {
    revstr += array[i];
  }
  return revstr;
}

//TESTS

reverseString('hello'); //should return a string.
reverseString('hello'); //should become "olleh".
reverseString('Howdy'); //should become "ydwoH".
reverseString('Greetings from Earth'); //should return "htraE morf sgniteerG".
