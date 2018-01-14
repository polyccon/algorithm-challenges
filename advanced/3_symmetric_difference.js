// Symmetric Difference
/*Create a function that takes two or more arrays and returns an array of the symmetric
difference (△ or ⊕) of the provided arrays.

Given two sets (for example set A = {1, 2, 3} and set B = {2, 3, 4}), the mathematical
term "symmetric difference" of two sets is the set of elements which are in either of the
two sets, but not in both (A △ B = C = {1, 4}).
For every additional symmetric difference you take (say on a set D = {2, 3}), you should get
the set with elements which are in either of the two the sets but not
both (C △ D = {1, 4} △ {2, 3} = {1, 2, 3, 4}).
*/

//Function taken from intermediate 2_diff_two_arrays.js
function diffArray(arr1, arr2) {
  var newArr = [];

  var newArr1 = arr1.filter(function(value, index, self) {
    return arr2.includes(value) === false;
  });
  var newArr2 = arr2.filter(function(value, index, self) {
    return arr1.includes(value) === false;
  });
  newArr = newArr1.concat(newArr2);

  return newArr;
}
function sym(args) {
  var arg = [].slice.call(arguments);
  return arg.reduce(diffArray, []).filter(function(value, index, self) {
    // remove any duplicates
    return self.indexOf(value) === index;
  });
}
