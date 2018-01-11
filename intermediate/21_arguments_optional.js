// Arguments optional
/* Create a function that sums two arguments together. If only one argument is provided,
then return a function that expects one argument and returns the sum.
 For example, addTogether(2, 3) should return 5, and addTogether(2) should return a function.
 Calling this returned function with a single argument will then return the sum:
 var sumTwoAnd = addTogether(2);
 sumTwoAnd(3) returns 5.
 If either argument isn't a valid number, return undefined.
*/

const typetester = array => array.every(element => typeof element === 'number');

function addTogether(args) {
  var args = [].slice.call(arguments);

  if (!typetester(args)) {
    return undefined;
  } else {
    if (args.length === 2) {
      return args[0] + args[1];
    } else {
      return function(n) {
        if (!typetester([n])) {
          return undefined;
        } else {
          return args[0] + n;
        }
      };
    }
  }
}

// TESTS
addTogether(2, 3); //Should return 5
addTogether(2)(3); //Should return 5
addTogether('http://bit.ly/IqT6zt'); //Should return undefined
addTogether(2, '3'); //Should return undefined
addTogether(2)([3]); //Should return undefined
