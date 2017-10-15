// Compare two arrays and return a new array with any items only found in one of the two given arrays,
// but not both. In other words, return the symmetric difference of the two arrays.

function diffArray(arr1, arr2) {
  var newArr = [];


  var newArr1= arr1.filter(function (value, index, self) {
                        return arr2.includes(value)===false;
                      });
   var newArr2= arr2.filter(function (value, index, self) {
                        return arr1.includes(value)===false;
                      });
   newArr = newArr1.concat(newArr2);

  return newArr;
}

diffArray([1, 2, 3, 5], [1, 2, 3, 4, 5]);
diffArray(["diorite", "andesite", "grass", "dirt", "pink wool", "dead shrub"], ["diorite", "andesite", "grass", "dirt", "dead shrub"]);
diffArray(["andesite", "grass", "dirt", "pink wool", "dead shrub"],["diorite", "andesite", "grass", "dirt", "dead shrub"]);
