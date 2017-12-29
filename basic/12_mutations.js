// Mutations
// Return true if the string in the first element of the array contains all of the letters of the string in the second element of the array.

//For example, ["hello", "Hello"], should return true because all of the letters in the second string are present in the first, ignoring case.

//The arguments ["hello", "hey"] should return false because the string "hello" does not contain a "y".

//Lastly, ["Alien", "line"], should return true because all of the letters in "line" are present in "Alien".

function mutation(arr) {
  var array = [];
  var arr0 = arr[0].toLowerCase().split('');
  var arr1 = arr[1].toLowerCase().split('');

  var checkArr0 = arr0.filter(function(value, index, self) {
    // remove any duplicates
    return self.indexOf(value) === index;
  });
  var checkArr1 = arr1.filter(function(value, index, self) {
    // remove any duplicates
    return self.indexOf(value) === index;
  });
  checkArr0.sort();
  checkArr1.sort();
  if (checkArr0.length === checkArr1.length) {
    return true;
  }

  for (var i = 0; i < checkArr1.length; i++) {
    if (checkArr0.toString().indexOf(checkArr1[i], 0) === -1) {
      return false;
    }
  }
  return true;
}

//TESTS
mutation(['hello', 'hey']); //should return false.
mutation(['hello', 'Hello']); //should return true.
mutation(['zyxwvutsrqponmlkjihgfedcba', 'qrstu']); //should return true.
mutation(['Mary', 'Army']); //should return true.
mutation(['Mary', 'Aarmy']); //should return true.
mutation(['Alien', 'line']); //should return true.
mutation(['floor', 'for']); //should return true.
mutation(['hello', 'neo']); //should return false.
mutation(['voodoo', 'no']); //should return false.
